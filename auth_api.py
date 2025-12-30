"""Authentication and user management API - FIXED VERSION"""

from fastapi import APIRouter, HTTPException, Request, Cookie, UploadFile
from fastapi.responses import JSONResponse, FileResponse, Response
from typing import Dict, Any, Optional
import json
import uuid
import os
import httpx
from database import db
from datetime import datetime

router = APIRouter()

@router.post("/register")
async def register(request: Request):
    """Register a new user"""
    try:
        data = await request.json()
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            raise HTTPException(status_code=400, detail="Email and password are required")

        existing_user = db.get_user_by_email(email)
        if existing_user:
            raise HTTPException(status_code=400, detail="User with this email already exists")

        user = db.create_user(email, password)
        if user:
            avatar_url = db.get_avatar(user["id"])
            user_data = {
                "id": user["id"],
                "email": user["email"],
                "plan": user["plan"]
            }
            if avatar_url:
                user_data["avatar"] = avatar_url

            session_token = f"session_{email}_{user['id']}"
            response = JSONResponse({"user": user_data})
            response.set_cookie("session_token", session_token, httponly=True, samesite="lax")
            return response
        else:
            raise HTTPException(status_code=400, detail="Failed to create user")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
async def login(request: Request):
    """Login existing user"""
    try:
        data = await request.json()
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            raise HTTPException(status_code=400, detail="Email and password are required")

        user = db.authenticate_user(email, password)
        if user:
            avatar_url = db.get_avatar(user["id"])
            user_data = {
                "id": user["id"],
                "email": user["email"],
                "plan": user["plan"]
            }
            if avatar_url:
                user_data["avatar"] = avatar_url

            session_token = f"session_{email}_{user['id']}"
            response = JSONResponse({"user": user_data})
            response.set_cookie("session_token", session_token, httponly=True, samesite="lax")
            return response
        else:
            raise HTTPException(status_code=401, detail="Invalid email or password")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/logout")
async def logout():
    """Sign out user"""
    response = JSONResponse({"message": "Signed out successfully"})
    response.set_cookie("session_token", "", expires=0)
    return response


@router.get("/session")
async def get_session(session_token: Optional[str] = Cookie(None)):
    """Get current session info"""
    if not session_token:
        return JSONResponse({"user": None})

    try:
        if session_token.startswith("session_"):
            parts = session_token.split("_")
            if len(parts) >= 3:
                email = parts[1]
                user_id = parts[2]
                user = db.get_user_by_email(email)
                if user and user["id"] == user_id:
                    avatar_url = db.get_avatar(user_id)
                    user_data = {
                        "id": user["id"],
                        "email": user["email"],
                        "plan": user["plan"]
                    }
                    if avatar_url:
                        user_data["avatar"] = avatar_url
                    return JSONResponse({"user": user_data})
    except Exception as e:
        print(f"Session validation error: {e}")

    return JSONResponse({"user": None})


@router.get("/chats")
async def get_user_chats(request: Request, session_token: Optional[str] = Cookie(None)):
    """Get user's chat history"""
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        parts = session_token.split("_")
        if len(parts) >= 3:
            email = parts[1]
            user_id = parts[2]
            user = db.get_user_by_email(email)
            if user and user["id"] == user_id:
                user_data = db.get_user_data(user_id)
                if user_data:
                    return JSONResponse({"chats": user_data["chats"]})
                else:
                    return JSONResponse({"chats": []})
    except:
        pass

    raise HTTPException(status_code=401, detail="Invalid session token")


@router.post("/chats")
async def create_chat(request: Request, session_token: Optional[str] = Cookie(None)):
    """Create a new chat"""
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        data = await request.json()
        title = data.get("title", "Новый чат")

        parts = session_token.split("_")
        if len(parts) < 3:
            raise HTTPException(status_code=401, detail="Invalid session token")

        email = parts[1]
        user_id = parts[2]
        user = db.get_user_by_email(email)
        if not (user and user["id"] == user_id):
            raise HTTPException(status_code=401, detail="Invalid session token")

        chat_id = str(uuid.uuid4())
        new_chat = {
            "id": chat_id,
            "title": title,
            "created_at": datetime.now().isoformat(),
            "messages": []
        }

        user_data = db.get_user_data(user_id)
        chats = user_data["chats"] if user_data else []
        chats.append(new_chat)

        success = db.save_user_data(user_id, chats)
        if success:
            return JSONResponse({"chat": new_chat})
        else:
            raise HTTPException(status_code=500, detail="Failed to save chat")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/avatar")
async def upload_avatar(request: Request, session_token: Optional[str] = Cookie(None)):
    """Upload user's avatar"""
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        parts = session_token.split("_")
        if len(parts) < 3:
            raise HTTPException(status_code=401, detail="Invalid session token")

        email = parts[1]
        user_id = parts[2]
        user = db.get_user_by_email(email)
        if not (user and user["id"] == user_id):
            raise HTTPException(status_code=401, detail="Invalid session token")
    except:
        raise HTTPException(status_code=401, detail="Invalid session token")

    try:
        form = await request.form()
        avatar_file = form.get("avatar")

        if avatar_file and isinstance(avatar_file, UploadFile):
            file_extension = os.path.splitext(avatar_file.filename)[1]
            new_filename = f"{user_id}{file_extension}"
            os.makedirs("uploads", exist_ok=True)
            file_path = f"uploads/{new_filename}"
            
            with open(file_path, "wb") as f:
                content = await avatar_file.read()
                f.write(content)

            avatar_url = f"/uploads/{new_filename}"
            success = db.update_avatar(user_id, avatar_url)

            if success:
                return JSONResponse({"avatar_url": avatar_url})
            else:
                raise HTTPException(status_code=500, detail="Failed to update avatar in database")
        else:
            raise HTTPException(status_code=400, detail="No avatar file provided")
    except Exception as e:
        try:
            data = await request.json()
            avatar_url = data.get("avatar_url")
            if avatar_url:
                success = db.update_avatar(user_id, avatar_url)
                if success:
                    return JSONResponse({"avatar_url": avatar_url})
                else:
                    raise HTTPException(status_code=500, detail="Failed to update avatar in database")
            else:
                raise HTTPException(status_code=400, detail="No avatar provided")
        except:
            raise HTTPException(status_code=400, detail=str(e))


@router.get("/avatar/{filename}")
async def serve_avatar(filename: str):
    """Serve user's avatar"""
    file_path = f"uploads/{filename}"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        return Response(content="", status_code=404)


@router.put("/password")
async def change_password(request: Request, session_token: Optional[str] = Cookie(None)):
    """Change user's password"""
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        parts = session_token.split("_")
        if len(parts) < 3:
            raise HTTPException(status_code=401, detail="Invalid session token")

        email = parts[1]
        user_id = parts[2]
        user = db.get_user_by_email(email)
        if not (user and user["id"] == user_id):
            raise HTTPException(status_code=401, detail="Invalid session token")

        data = await request.json()
        new_password = data.get("new_password")

        if not new_password:
            raise HTTPException(status_code=400, detail="New password is required")

        success = db.update_user_password(user_id, new_password)
        if success:
            return JSONResponse({"message": "Password updated successfully"})
        else:
            raise HTTPException(status_code=500, detail="Failed to update password")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/account")
async def delete_account(request: Request, session_token: Optional[str] = Cookie(None)):
    """Delete user account"""
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        parts = session_token.split("_")
        if len(parts) < 3:
            raise HTTPException(status_code=401, detail="Invalid session token")

        email = parts[1]
        user_id = parts[2]
        user = db.get_user_by_email(email)
        if not (user and user["id"] == user_id):
            raise HTTPException(status_code=401, detail="Invalid session token")

        success = db.delete_user(user_id)
        if success:
            return JSONResponse({"message": "Account deleted successfully"})
        else:
            raise HTTPException(status_code=500, detail="Failed to delete account")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/chats/{chat_id}/messages")
async def get_chat_messages(chat_id: str, request: Request, session_token: Optional[str] = Cookie(None)):
    """Get messages for a specific chat"""
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        parts = session_token.split("_")
        if len(parts) < 3:
            raise HTTPException(status_code=401, detail="Invalid session token")

        email = parts[1]
        user_id = parts[2]
        user = db.get_user_by_email(email)
        if not (user and user["id"] == user_id):
            raise HTTPException(status_code=401, detail="Invalid session token")

        user_data = db.get_user_data(user_id)
        if user_data and "chats" in user_data:
            for chat in user_data["chats"]:
                if chat["id"] == chat_id:
                    return JSONResponse({"messages": chat.get("messages", [])})

        raise HTTPException(status_code=404, detail="Chat not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ===== ИСПРАВЛЕНО: РЕАЛЬНЫЙ AI ВЫЗОВ =====
@router.post("/chats/{chat_id}/messages")
async def add_chat_message(chat_id: str, request: Request, session_token: Optional[str] = Cookie(None)):
    """Add a message to a specific chat with REAL AI RESPONSE"""
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        parts = session_token.split("_")
        if len(parts) < 3:
            raise HTTPException(status_code=401, detail="Invalid session token")

        email = parts[1]
        user_id = parts[2]
        user = db.get_user_by_email(email)
        if not (user and user["id"] == user_id):
            raise HTTPException(status_code=401, detail="Invalid session token")

        data = await request.json()
        content = data.get("content")
        coding_enabled = data.get("coding_enabled", False)

        if not content:
            raise HTTPException(status_code=400, detail="Message content is required")

        user_data = db.get_user_data(user_id)
        if not user_data or "chats" not in user_data:
            raise HTTPException(status_code=404, detail="Chat not found")

        chat_found = False
        for chat in user_data["chats"]:
            if chat["id"] == chat_id:
                user_message = {
                    "id": str(uuid.uuid4()),
                    "role": "user",
                    "content": content,
                    "timestamp": datetime.now().isoformat()
                }
                chat.setdefault("messages", []).append(user_message)

                # ===== РЕАЛЬНЫЙ ВЫЗОВ OPENROUTER =====
                from config import API_KEY, OPENROUTER_URL, SITE_NAME, REFERER, FALLBACK_MODELS, DEFAULT_CODING_MODEL
                
                model = DEFAULT_CODING_MODEL if coding_enabled else FALLBACK_MODELS[0]
                
                # Формируем историю сообщений
                messages = []
                for msg in chat["messages"]:
                    messages.append({
                        "role": msg["role"],
                        "content": msg["content"]
                    })

                payload = {
                    "model": model,
                    "messages": messages,
                    "stream": False,
                }

                headers = {
                    "Authorization": f"Bearer {API_KEY}",
                    "HTTP-Referer": REFERER,
                    "X-Title": SITE_NAME,
                }

                async with httpx.AsyncClient(timeout=120.0) as client:
                    response = await client.post(OPENROUTER_URL, json=payload, headers=headers)
                    response.raise_for_status()
                    ai_data = response.json()
                    
                    ai_content = ai_data["choices"][0]["message"]["content"]

                assistant_message = {
                    "id": str(uuid.uuid4()),
                    "role": "assistant",
                    "content": ai_content,
                    "timestamp": datetime.now().isoformat()
                }
                chat["messages"].append(assistant_message)

                # Сохраняем в БД
                success = db.save_user_data(user_id, user_data["chats"])
                if success:
                    return JSONResponse({
                        "response": assistant_message["content"],
                        "message": assistant_message
                    })
                else:
                    raise HTTPException(status_code=500, detail="Failed to save message")

                chat_found = True
                break

        if not chat_found:
            raise HTTPException(status_code=404, detail="Chat not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/chats/{chat_id}")
async def delete_chat(chat_id: str, request: Request, session_token: Optional[str] = Cookie(None)):
    """Delete a specific chat"""
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        parts = session_token.split("_")
        if len(parts) < 3:
            raise HTTPException(status_code=401, detail="Invalid session token")

        email = parts[1]
        user_id = parts[2]
        user = db.get_user_by_email(email)
        if not (user and user["id"] == user_id):
            raise HTTPException(status_code=401, detail="Invalid session token")

        user_data = db.get_user_data(user_id)
        if user_data and "chats" in user_data:
            updated_chats = [chat for chat in user_data["chats"] if chat["id"] != chat_id]
            success = db.save_user_data(user_id, updated_chats)
            if success:
                return JSONResponse({"message": "Chat deleted successfully"})
            else:
                raise HTTPException(status_code=500, detail="Failed to delete chat")

        raise HTTPException(status_code=404, detail="Chat not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/export")
async def export_chat_history(request: Request, session_token: Optional[str] = Cookie(None)):
    """Export user's chat history"""
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        parts = session_token.split("_")
        if len(parts) < 3:
            raise HTTPException(status_code=401, detail="Invalid session token")

        email = parts[1]
        user_id = parts[2]
        user = db.get_user_by_email(email)
        if not (user and user["id"] == user_id):
            raise HTTPException(status_code=401, detail="Invalid session token")

        user_data = db.get_user_data(user_id)
        if user_data:
            return JSONResponse({"chats": user_data["chats"]})
        else:
            return JSONResponse({"chats": []})
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/admin/users")
async def get_all_users(request: Request):
    """Get all users (admin endpoint)"""
    return JSONResponse({"users": []})


@router.post("/admin/set-plan")
async def set_user_plan(request: Request):
    """Set user plan (admin endpoint)"""
    try:
        data = await request.json()
        return JSONResponse({"message": "Plan updated successfully"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
