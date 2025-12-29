"""Authentication and user management API"""
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import Dict, Any
import json
import uuid
from database import db
from models import ChatRequest


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
        
        # Check if user already exists
        existing_user = db.get_user_by_email(email)
        if existing_user:
            raise HTTPException(status_code=400, detail="User with this email already exists")
        
        # Create new user
        user = db.create_user(email, password)
        if user:
            # Get avatar URL if it exists
            avatar_url = db.get_avatar(user["id"])
            user_data = {
                "id": user["id"],
                "email": user["email"],
                "plan": user["plan"]
            }
            if avatar_url:
                user_data["avatar"] = avatar_url
            
            # Create session token
            session_token = f"session_{email}_{user['id']}"
            response = JSONResponse({
                "user": user_data
            })
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
            # Get avatar URL if it exists
            avatar_url = db.get_avatar(user["id"])
            user_data = {
                "id": user["id"],
                "email": user["email"],
                "plan": user["plan"]
            }
            if avatar_url:
                user_data["avatar"] = avatar_url
            
            # Create session token
            session_token = f"session_{email}_{user['id']}"
            response = JSONResponse({
                "user": user_data
            })
            response.set_cookie("session_token", session_token, httponly=True, samesite="lax")
            return response
        else:
            raise HTTPException(status_code=401, detail="Invalid email or password")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/logout")
async def logout(response: JSONResponse):
    """Sign out user"""
    # Clear the session cookie
    response = JSONResponse({"message": "Signed out successfully"})
    response.set_cookie("session_token", "", expires=0)
    return response


from fastapi import Cookie
from typing import Optional

@router.get("/session")
async def get_session(session_token: Optional[str] = Cookie(None)):
    """Get current session info"""
    if not session_token:
        # Return no user if no session token
        return JSONResponse({"user": None})
    
    # In a real implementation, you'd validate the session token against the database
    # For now, we'll simulate by extracting user info from the token
    try:
        # Token format: session_{email}_{user_id}
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
    
    # Return no user if token is invalid
    return JSONResponse({"user": None})


@router.get("/chats")
async def get_user_chats(request: Request, session_token: Optional[str] = Cookie(None)):
    """Get user's chat history"""
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    # Extract user_id from token (simplified)
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
        
        # Extract user_id from token (simplified)
        parts = session_token.split("_")
        if len(parts) < 3:
            raise HTTPException(status_code=401, detail="Invalid session token")
        
        email = parts[1]
        user_id = parts[2]
        
        user = db.get_user_by_email(email)
        if not (user and user["id"] == user_id):
            raise HTTPException(status_code=401, detail="Invalid session token")
        
        # Create a new chat entry
        import uuid
        from datetime import datetime
        chat_id = str(uuid.uuid4())
        new_chat = {
            "id": chat_id,
            "title": title,
            "created_at": datetime.now().isoformat(),
            "messages": []
        }
        
        # Get existing user data and add the new chat
        user_data = db.get_user_data(user_id)
        chats = user_data["chats"] if user_data else []
        chats.append(new_chat)
        
        # Save updated chat list
        success = db.save_user_data(user_id, chats)
        if success:
            return JSONResponse({"chat": new_chat})
        else:
            raise HTTPException(status_code=500, detail="Failed to save chat")
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


import os
from fastapi import UploadFile
from fastapi.responses import FileResponse

@router.post("/avatar")
async def upload_avatar(request: Request, session_token: Optional[str] = Cookie(None)):
    """Upload user's avatar"""
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    # Extract user_id from token
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
        # Try to get file from form data
        form = await request.form()
        avatar_file = form.get("avatar")
        
        if avatar_file and isinstance(avatar_file, UploadFile):
            # In a real implementation, you'd save the file to a directory
            # For this implementation, we'll just save to a temp location
            import uuid
            file_extension = os.path.splitext(avatar_file.filename)[1]
            new_filename = f"{user_id}{file_extension}"
            
            # Create uploads directory if it doesn't exist
            os.makedirs("uploads", exist_ok=True)
            
            # Save the file
            file_path = f"uploads/{new_filename}"
            with open(file_path, "wb") as f:
                content = await avatar_file.read()
                f.write(content)
            
            # Update user's avatar in database
            avatar_url = f"/uploads/{new_filename}"
            success = db.update_avatar(user_id, avatar_url)
            
            if success:
                return JSONResponse({
                    "avatar_url": avatar_url
                })
            else:
                raise HTTPException(status_code=500, detail="Failed to update avatar in database")
        else:
            raise HTTPException(status_code=400, detail="No avatar file provided")
    except Exception as e:
        # If form parsing fails, try JSON
        try:
            data = await request.json()
            avatar_url = data.get("avatar_url")
            if avatar_url:
                # Update user's avatar in database
                success = db.update_avatar(user_id, avatar_url)
                if success:
                    return JSONResponse({
                        "avatar_url": avatar_url
                    })
                else:
                    raise HTTPException(status_code=500, detail="Failed to update avatar in database")
            else:
                raise HTTPException(status_code=400, detail="No avatar provided")
        except:
            raise HTTPException(status_code=400, detail=str(e))

# Serve uploaded avatars
@router.get("/avatar/{filename}")
async def serve_avatar(filename: str):
    """Serve user's avatar"""
    file_path = f"uploads/{filename}"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        # Return a default avatar if file doesn't exist
        from fastapi.responses import Response
        return Response(content="", status_code=404)


# We don't need a separate get avatar endpoint since it's included in the user object


@router.put("/password")
async def change_password(request: Request, session_token: Optional[str] = Cookie(None)):
    """Change user's password"""
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    try:
        # Extract user_id from token
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
        
        # Update password in database
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
    
    # Extract user_id from token (simplified)
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
# Chat messages endpoints
@router.get("/chats/{chat_id}/messages")
async def get_chat_messages(chat_id: str, request: Request, session_token: Optional[str] = Cookie(None)):
    """Get messages for a specific chat"""
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    # Extract user_id from token (simplified)
    try:
        parts = session_token.split("_")
        if len(parts) < 3:
            raise HTTPException(status_code=401, detail="Invalid session token")
        
        email = parts[1]
        user_id = parts[2]
        
        user = db.get_user_by_email(email)
        if not (user and user["id"] == user_id):
            raise HTTPException(status_code=401, detail="Invalid session token")
        
        # Get user's chat data and find the specific chat
        user_data = db.get_user_data(user_id)
        if user_data and "chats" in user_data:
            for chat in user_data["chats"]:
                if chat["id"] == chat_id:
                    # Return the messages from this chat
                    return JSONResponse({"messages": chat.get("messages", [])})
        
        # Chat not found for this user
        raise HTTPException(status_code=404, detail="Chat not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chats/{chat_id}/messages")
async def add_chat_message(chat_id: str, request: Request, session_token: Optional[str] = Cookie(None)):
    """Add a message to a specific chat"""
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    try:
        # Extract user_id from token
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
        reasoning_enabled = data.get("reasoning_enabled", False)
        
        if not content:
            raise HTTPException(status_code=400, detail="Message content is required")
        
        # Get user's chat data and find the specific chat
        user_data = db.get_user_data(user_id)
        if not user_data or "chats" not in user_data:
            raise HTTPException(status_code=404, detail="Chat not found")
        
        chat_found = False
        for chat in user_data["chats"]:
            if chat["id"] == chat_id:
                # Add user message to chat
                from datetime import datetime
                user_message = {
                    "id": str(uuid.uuid4()),
                    "role": "user",
                    "content": content,
                    "timestamp": datetime.now().isoformat()
                }
                chat.setdefault("messages", []).append(user_message)
                
                # Here we would normally call the AI to generate a response
                # For now, we'll just echo the message back as a simple response
                assistant_message = {
                    "id": str(uuid.uuid4()),
                    "role": "assistant",
                    "content": f"Echo: {content}",
                    "timestamp": datetime.now().isoformat()
                }
                chat["messages"].append(assistant_message)
                
                # Save updated chat data
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
    
    # Extract user_id from token (simplified)
    try:
        parts = session_token.split("_")
        if len(parts) < 3:
            raise HTTPException(status_code=401, detail="Invalid session token")
        
        email = parts[1]
        user_id = parts[2]
        
        user = db.get_user_by_email(email)
        if not (user and user["id"] == user_id):
            raise HTTPException(status_code=401, detail="Invalid session token")
        
        # Get user's chat data and remove the specific chat
        user_data = db.get_user_data(user_id)
        if user_data and "chats" in user_data:
            updated_chats = [chat for chat in user_data["chats"] if chat["id"] != chat_id]
            
            # Save updated chat list
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

# Export chat history endpoint
@router.get("/export")
async def export_chat_history(request: Request, session_token: Optional[str] = Cookie(None)):
    """Export user's chat history"""
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    # Extract user_id from token (simplified)
    try:
        parts = session_token.split("_")
        if len(parts) < 3:
            raise HTTPException(status_code=401, detail="Invalid session token")
        
        email = parts[1]
        user_id = parts[2]
        
        user = db.get_user_by_email(email)
        if not (user and user["id"] == user_id):
            raise HTTPException(status_code=401, detail="Invalid session token")
        
        # Get user's chat data
        user_data = db.get_user_data(user_id)
        if user_data:
            return JSONResponse({"chats": user_data["chats"]})
        else:
            return JSONResponse({"chats": []})
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Admin endpoints (simplified for this implementation)
@router.get("/admin/users")
async def get_all_users(request: Request):
    """Get all users (admin endpoint - simplified)"""
    # In a real implementation, you'd check admin privileges
    # For now, return a mock response
    return JSONResponse({"users": []})


@router.post("/admin/set-plan")
async def set_user_plan(request: Request):
    """Set user plan (admin endpoint - simplified)"""
    # In a real implementation, you'd check admin privileges
    try:
        data = await request.json()
        target_user_id = data.get("user_id")
        new_plan = data.get("plan")
        
        # For now, return success
        # In a real implementation, you'd update the database
        return JSONResponse({"message": "Plan updated successfully"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))