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
from ddgs import DDGS

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

# Подключение роутера и планировщика аналитики
app.include_router(analytics_router)
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
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Generated Image - {uid}</title>
            <style>
                * {{ margin: 0; padding: 0; box-sizing: border-box; }}
                body {{
                    font-family: 'Segoe UI', sans-serif;
                    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
                    min-height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 20px;
                }}
                .container {{
                    max-width: 1200px;
                    width: 100%;
                    background: rgba(255, 255, 255, 0.05);
                    backdrop-filter: blur(10px);
                    border-radius: 20px;
                    padding: 30px;
                    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                }}
                h1 {{
                    color: #00d4ff;
                    text-align: center;
                    margin-bottom: 10px;
                    font-size: 2em;
                }}
                .prompt {{
                    color: #a0a0a0;
                    text-align: center;
                    margin-bottom: 30px;
                    font-style: italic;
                }}
                .image-wrapper {{
                    position: relative;
                    width: 100%;
                    border-radius: 15px;
                    overflow: hidden;
                    box-shadow: 0 10px 40px rgba(0, 212, 255, 0.3);
                }}
                .image-wrapper img {{
                    width: 100%;
                    height: auto;
                    display: block;
                }}
                .loader {{
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    width: 50px;
                    height: 50px;
                    border: 5px solid rgba(0, 212, 255, 0.2);
                    border-top-color: #00d4ff;
                    border-radius: 50%;
                    animation: spin 1s linear infinite;
                }}
                @keyframes spin {{
                    to {{ transform: translate(-50%, -50%) rotate(360deg); }}
                }}
                .info {{
                    margin-top: 20px;
                    padding: 15px;
                    background: rgba(255, 255, 255, 0.03);
                    border-radius: 10px;
                    color: #c0c0c0;
                    font-size: 0.9em;
                }}
                .info strong {{ color: #00d4ff; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🎨 AI Generated Image</h1>
                <p class="prompt">Prompt: {clean_prompt}</p>
                <div class="image-wrapper">
                    <div class="loader" id="loader"></div>
                    <img id="genImage" src="{image_url}" alt="Generated image" style="display:none;" onload="document.getElementById('loader').style.display='none'; this.style.display='block';">
                </div>
                <div class="info">
                    <strong>UID:</strong> {uid} | <strong>Model:</strong> Flux | <strong>Resolution:</strong> 1024x1024 | <strong>Seed:</strong> {seed}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    except Exception as e:
        logger.error(f"Image generation failed: {e}")
        return f"<html><body><h1>Error generating image</h1><p>{str(e)}</p></body></html>"

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
