import json
import os
from mvc.models.user_model import UserModel

DATA_FILE = "mvc/data.json"

class UserDAO:
    @staticmethod
    def load_users():
        """讀取 data.json 並回傳用戶列表"""
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return[]
        
    @staticmethod
    def save_users(users):
        """將用戶寫入 data.json"""
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(users, f, indent=4, ensure_ascii=False)

    @staticmethod
    def get_all_users():
        """取得所有用戶資料"""
        return UserDAO.load_users()
    
    @staticmethod
    def add_users(user: UserModel):
        """新增用戶資料"""
        users = UserDAO.load_users()
        users.append(user.dict())
        UserDAO.save_users(users)
