import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mvc.dao.user_dao import UserDAO
from mvc.models.user_model import UserModel

class UserService:
    @staticmethod
    def get_users():
        """取得所有用戶資料"""
        return UserDAO.get_all_users()
    
    @staticmethod
    def create_user(user:UserModel):
        """新增用戶"""
        UserDAO.add_users(user)
        return "資料新增成功"