"""Local SQLite database module to replace Supabase functionality"""
import sqlite3
import hashlib
import secrets
from datetime import datetime
from typing import Optional, List, Dict, Any
import json
import os


class Database:
    def __init__(self, db_path: str = "local_chat.db"):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        """Initialize the database with required tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                plan TEXT DEFAULT 'free'
            )
        """)
        
        # Create user_data table for storing chat history
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id TEXT PRIMARY KEY,
                chats TEXT DEFAULT '[]',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        
        # Create avatars table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS avatars (
                user_id TEXT PRIMARY KEY,
                avatar_url TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        
        conn.commit()
        conn.close()
    
    def hash_password(self, password: str) -> str:
        """Hash password using SHA-256 with salt"""
        salt = secrets.token_hex(16)
        pwd_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        return f"{pwd_hash}:{salt}"
    
    def verify_password(self, password: str, stored_hash: str) -> bool:
        """Verify password against stored hash"""
        try:
            pwd_hash, salt = stored_hash.split(':')
            return pwd_hash == hashlib.sha256((password + salt).encode()).hexdigest()
        except:
            return False
    
    def create_user(self, email: str, password: str) -> Optional[Dict[str, Any]]:
        """Create a new user"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            user_id = f"user_{secrets.token_hex(16)}"
            password_hash = self.hash_password(password)
            
            cursor.execute("""
                INSERT INTO users (id, email, password_hash)
                VALUES (?, ?, ?)
            """, (user_id, email, password_hash))
            
            # Create empty user data entry
            cursor.execute("""
                INSERT INTO user_data (user_id, chats)
                VALUES (?, ?)
            """, (user_id, "[]"))
            
            conn.commit()
            
            return {
                "id": user_id,
                "email": email,
                "plan": "free",
                "created_at": datetime.now().isoformat()
            }
        except sqlite3.IntegrityError:
            # Email already exists
            return None
        finally:
            conn.close()
    
    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        """Get user by email"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, email, password_hash, plan, created_at
            FROM users
            WHERE email = ?
        """, (email,))
        
        row = cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "email": row[1],
                "password_hash": row[2],
                "plan": row[3],
                "created_at": row[4]
            }
        
        conn.close()
        return None
    
    def authenticate_user(self, email: str, password: str) -> Optional[Dict[str, Any]]:
        """Authenticate user with email and password"""
        user = self.get_user_by_email(email)
        if user and self.verify_password(password, user["password_hash"]):
            # Remove password hash from returned data
            del user["password_hash"]
            return user
        return None
    
    def update_user_plan(self, user_id: str, plan: str) -> bool:
        """Update user plan"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE users
            SET plan = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (plan, user_id))
        
        conn.commit()
        success = cursor.rowcount > 0
        conn.close()
        return success
    
    def update_user_password(self, user_id: str, new_password: str) -> bool:
        """Update user password"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        password_hash = self.hash_password(new_password)
        
        cursor.execute("""
            UPDATE users
            SET password_hash = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (password_hash, user_id))
        
        conn.commit()
        success = cursor.rowcount > 0
        conn.close()
        return success
    
    def delete_user(self, user_id: str) -> bool:
        """Delete user and all related data"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Delete user data
        cursor.execute("DELETE FROM user_data WHERE user_id = ?", (user_id,))
        # Delete avatar
        cursor.execute("DELETE FROM avatars WHERE user_id = ?", (user_id,))
        # Delete user
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        
        conn.commit()
        success = cursor.rowcount > 0
        conn.close()
        return success
    
    def get_user_data(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Get user's chat data"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT chats, updated_at
            FROM user_data
            WHERE user_id = ?
        """, (user_id,))
        
        row = cursor.fetchone()
        if row:
            try:
                chats = json.loads(row[0]) if row[0] else []
            except:
                chats = []
            
            return {
                "chats": chats,
                "updated_at": row[1]
            }
        
        conn.close()
        return None
    
    def save_user_data(self, user_id: str, chats: List[Dict]) -> bool:
        """Save user's chat data"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        chats_json = json.dumps(chats)
        
        cursor.execute("""
            INSERT OR REPLACE INTO user_data (user_id, chats, updated_at)
            VALUES (?, ?, CURRENT_TIMESTAMP)
        """, (user_id, chats_json))
        
        conn.commit()
        success = cursor.rowcount > 0
        conn.close()
        return success
    
    def update_avatar(self, user_id: str, avatar_url: str) -> bool:
        """Update user's avatar"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT OR REPLACE INTO avatars (user_id, avatar_url, updated_at)
            VALUES (?, ?, CURRENT_TIMESTAMP)
        """, (user_id, avatar_url))
        
        conn.commit()
        success = cursor.rowcount > 0
        conn.close()
        return success
    
    def get_avatar(self, user_id: str) -> Optional[str]:
        """Get user's avatar URL"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT avatar_url
            FROM avatars
            WHERE user_id = ?
        """, (user_id,))
        
        row = cursor.fetchone()
        conn.close()
        return row[0] if row else None
    
    def get_all_users(self) -> List[Dict[str, Any]]:
        """Get all users (for admin panel)"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, email, plan, created_at
            FROM users
            ORDER BY email
        """)
        
        rows = cursor.fetchall()
        users = []
        for row in rows:
            users.append({
                "id": row[0],
                "email": row[1],
                "plan": row[2],
                "created_at": row[3]
            })
        
        conn.close()
        return users


# Global database instance
db = Database()