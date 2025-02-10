from fastapi import APIRouter
from mvc.services.user_service import UserService
from mvc.models.user_model import UserModel

router = APIRouter()

@router.get("/api/user")
async def get_user():
    """列出所有用戶資料"""
    return UserService.get_users()

@router.post("/api/user")
async def add_user(user: UserModel):
    """新增用戶資料"""
    return UserService.create_user(user)