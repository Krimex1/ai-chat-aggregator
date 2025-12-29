# main.py
import json
import logging
import uvicorn
import time
import urllib.parse
import random
from typing import List, Optional, AsyncGenerator
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import httpx
from duckduckgo_search import DDGS

# Импорты из новых модулей
from config import (
    PORT,
    API_KEY,
    OPENROUTER_URL,
    SITE_NAME,
    REFERER,
    FALLBACK_MODELS,
    DEFAULT_CODING_MODEL
)
from models import Message, ChatRequest
from templates import INDEX_HTML

# Интеграция аналитики (без изменений)
from analytics import router as analytics_router, init_analytics_scheduler

# Authentication and database API
from auth_api import router as auth_router

# --- LOGGING SETUP ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ChatApp")

# --- APP SETUP ---
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров и планировщика аналитики
app.include_router(analytics_router)
app.include_router(auth_router, prefix="/api")
init_analytics_scheduler(app)

# --- SEARCH LOGIC ---
def perform_search(query: str) -> str:
    try:
        logger.info(f"Searching DDG for: {query}")
        results = DDGS().text(query, max_results=5)
        if not results:
            return "No search results found."
        formatted_results = "Web Search Results:\n\n"
        for i, res in enumerate(results, 1):
            formatted_results += f"{i}. Title: {res['title']}\n   URL: {res['href']}\n   Snippet: {res['body']}\n\n"
        return formatted_results
    except Exception as e:
        logger.error(f"Search failed: {e}")
        return f"Search failed: {str(e)}"

# --- IMAGE GENERATION LOGIC ---
def generate_pollinations_html(prompt: str) -> str:
    try:
        triggers = ["нарисуй", "сгенерируй", "создай", "draw", "generate", "create", "image of", "picture of", "/img"]
        clean_prompt = prompt.lower()
        for t in triggers:
            clean_prompt = clean_prompt.replace(t, "")
        clean_prompt = clean_prompt.strip()
        if not clean_prompt:
            clean_prompt = "masterpiece"
        
        enhanced_prompt = f"{clean_prompt}, hyperrealistic, 8k, highly detailed, raw photo, cinematic lighting"
        encoded_prompt = urllib.parse.quote(enhanced_prompt)
        seed = random.randint(0, 1000000)
        uid = f"gen_{seed}_{int(time.time())}"
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&seed={seed}&model=flux&nologo=true&enhance=true"
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Generated Image</title>
            <style>
                body {{ margin: 0; padding: 20px; background: #0a0a0a; color: #fff; font-family: Arial; }}
                .container {{ max-width: 1200px; margin: 0 auto; }}
                img {{ max-width: 100%; border-radius: 8px; box-shadow: 0 4px 16px rgba(0,0,0,0.5); }}
                .info {{ margin-top: 20px; padding: 15px; background: #1a1a1a; border-radius: 8px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <img src="{image_url}" alt="Generated image" id="{uid}">
                <div class="info">
                    <strong>Prompt:</strong> {clean_prompt}<br>
                    <strong>Model:</strong> Flux<br>
                    <strong>Seed:</strong> {seed}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    except Exception as e:
        return f"<html><body><h2>Image generation failed:</h2><pre>{str(e)}</pre></body></html>"

# --- STREAMING RESPONSE LOGIC ---
async def stream_response(request: ChatRequest) -> AsyncGenerator[str, None]:
    # Обработка веб-поиска
    if request.web_search and request.messages:
        last_user_msg = next((m for m in reversed(request.messages) if m.role == "user"), None)
        if last_user_msg:
            search_results = perform_search(last_user_msg.content)
            request.messages.append(Message(role="system", content=f"Web search context:\n{search_results}"))
    
    # Выбор модели
    if request.coding_mode:
        model = request.coding_model
    elif request.model == "auto":
        model = FALLBACK_MODELS[0]
    else:
        model = request.model
    
    # Формирование сообщений для API
    messages = [{"role": m.role, "content": m.content} for m in request.messages]
    
    payload = {
        "model": model,
        "messages": messages,
        "stream": True,
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": REFERER,
        "X-Title": SITE_NAME,
    }
    
    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            async with client.stream("POST", OPENROUTER_URL, json=payload, headers=headers) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    if line.startswith("data: "):
                        line = line[6:]
                    if line.strip() == "[DONE]":
                        break
                    try:
                        chunk = json.loads(line)
                        if "choices" in chunk and len(chunk["choices"]) > 0:
                            delta = chunk["choices"][0].get("delta", {})
                            content = delta.get("content", "")
                            if content:
                                yield f"data: {json.dumps({'content': content})}\n\n"
                    except json.JSONDecodeError:
                        continue
    except Exception as e:
        logger.error(f"Streaming error: {e}")
        yield f"data: {json.dumps({'error': str(e)})}\n\n"

# --- ROUTES ---
@app.get("/", response_class=HTMLResponse)
async def index():
    return INDEX_HTML

@app.post("/chat")
async def chat(request: ChatRequest):
    return StreamingResponse(stream_response(request), media_type="text/event-stream")

@app.get("/generate_image", response_class=HTMLResponse)
async def generate_image(prompt: str):
    return generate_pollinations_html(prompt)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
