"""Authentication and user management API"""
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import Dict, Any
import json
from database import db
from models import ChatRequest


router = APIRouter()


@router.post("/auth/signup")
async def signup(request: Request):
    """Sign up a new user"""
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
            # Create a session token (simplified - in production you'd use JWT)
            session_token = f"session_{email}_{user['id']}"
            return JSONResponse({
                "user": {
                    "id": user["id"],
                    "email": user["email"],
                    "plan": user["plan"]
                },
                "session_token": session_token
            })
        else:
            raise HTTPException(status_code=400, detail="Failed to create user")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/auth/signin")
async def signin(request: Request):
    """Sign in existing user"""
    try:
        data = await request.json()
        email = data.get("email")
        password = data.get("password")
        
        if not email or not password:
            raise HTTPException(status_code=400, detail="Email and password are required")
        
        user = db.authenticate_user(email, password)
        if user:
            # Create a session token (simplified - in production you'd use JWT)
            session_token = f"session_{email}_{user['id']}"
            return JSONResponse({
                "user": {
                    "id": user["id"],
                    "email": user["email"],
                    "plan": user["plan"]
                },
                "session_token": session_token
            })
        else:
            raise HTTPException(status_code=401, detail="Invalid email or password")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/auth/signout")
async def signout(request: Request):
    """Sign out user"""
    # In a real implementation, you'd invalidate the session token
    return JSONResponse({"message": "Signed out successfully"})


@router.get("/auth/me")
async def get_current_user(request: Request):
    """Get current user info"""
    # In a real implementation, you'd validate the session token
    # For now, we'll return a mock response
    session_token = request.headers.get("authorization", "").replace("Bearer ", "")
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    # Extract email and user_id from token (simplified)
    try:
        parts = session_token.split("_")
        if len(parts) >= 3:
            email = parts[1]
            user_id = parts[2]
            
            user = db.get_user_by_email(email)
            if user and user["id"] == user_id:
                return JSONResponse({
                    "user": {
                        "id": user["id"],
                        "email": user["email"],
                        "plan": user["plan"]
                    }
                })
    except:
        pass
    
    raise HTTPException(status_code=401, detail="Invalid session token")


@router.get("/user/chats")
async def get_user_chats(request: Request):
    """Get user's chat history"""
    session_token = request.headers.get("authorization", "").replace("Bearer ", "")
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


@router.post("/user/chats")
async def save_user_chats(request: Request):
    """Save user's chat history"""
    session_token = request.headers.get("authorization", "").replace("Bearer ", "")
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    try:
        data = await request.json()
        chats = data.get("chats", [])
        
        # Extract user_id from token (simplified)
        parts = session_token.split("_")
        if len(parts) >= 3:
            email = parts[1]
            user_id = parts[2]
            
            user = db.get_user_by_email(email)
            if user and user["id"] == user_id:
                success = db.save_user_data(user_id, chats)
                if success:
                    return JSONResponse({"message": "Chats saved successfully"})
                else:
                    raise HTTPException(status_code=500, detail="Failed to save chats")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    raise HTTPException(status_code=401, detail="Invalid session token")


@router.post("/user/avatar")
async def update_avatar(request: Request):
    """Update user's avatar"""
    session_token = request.headers.get("authorization", "").replace("Bearer ", "")
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    try:
        data = await request.json()
        avatar_url = data.get("avatar_url")
        
        # Extract user_id from token (simplified)
        parts = session_token.split("_")
        if len(parts) >= 3:
            email = parts[1]
            user_id = parts[2]
            
            user = db.get_user_by_email(email)
            if user and user["id"] == user_id:
                success = db.update_avatar(user_id, avatar_url)
                if success:
                    return JSONResponse({"message": "Avatar updated successfully"})
                else:
                    raise HTTPException(status_code=500, detail="Failed to update avatar")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    raise HTTPException(status_code=401, detail="Invalid session token")


@router.get("/user/avatar")
async def get_avatar(request: Request):
    """Get user's avatar"""
    session_token = request.headers.get("authorization", "").replace("Bearer ", "")
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
                avatar_url = db.get_avatar(user_id)
                return JSONResponse({"avatar_url": avatar_url})
    except:
        pass
    
    raise HTTPException(status_code=401, detail="Invalid session token")


@router.post("/user/change-password")
async def change_password(request: Request):
    """Change user's password"""
    session_token = request.headers.get("authorization", "").replace("Bearer ", "")
    if not session_token or not session_token.startswith("session_"):
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    try:
        data = await request.json()
        current_password = data.get("current_password")
        new_password = data.get("new_password")
        
        # Extract user_id from token (simplified)
        parts = session_token.split("_")
        if len(parts) >= 3:
            email = parts[1]
            user_id = parts[2]
            
            # First verify current password by getting user and checking
            user = db.get_user_by_email(email)
            if user and user["id"] == user_id:
                # We need to verify the current password
                if db.verify_password(current_password, user["password_hash"]):
                    success = db.update_user_password(user_id, new_password)
                    if success:
                        return JSONResponse({"message": "Password changed successfully"})
                    else:
                        raise HTTPException(status_code=500, detail="Failed to update password")
                else:
                    raise HTTPException(status_code=400, detail="Current password is incorrect")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    raise HTTPException(status_code=401, detail="Invalid session token")


@router.post("/user/delete-account")
async def delete_account(request: Request):
    """Delete user account"""
    session_token = request.headers.get("authorization", "").replace("Bearer ", "")
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
                success = db.delete_user(user_id)
                if success:
                    return JSONResponse({"message": "Account deleted successfully"})
                else:
                    raise HTTPException(status_code=500, detail="Failed to delete account")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    raise HTTPException(status_code=401, detail="Invalid session token")


# Admin endpoints
@router.get("/admin/users")
async def get_all_users(request: Request):
    """Get all users (admin endpoint - simplified)"""
    # In a real implementation, you'd check admin privileges
    users = db.get_all_users()
    return JSONResponse({"users": users})


@router.post("/admin/set-plan")
async def set_user_plan(request: Request):
    """Set user plan (admin endpoint - simplified)"""
    # In a real implementation, you'd check admin privileges
    try:
        data = await request.json()
        target_user_id = data.get("user_id")
        new_plan = data.get("plan")
        
        success = db.update_user_plan(target_user_id, new_plan)
        if success:
            return JSONResponse({"message": "Plan updated successfully"})
        else:
            raise HTTPException(status_code=500, detail="Failed to update plan")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))