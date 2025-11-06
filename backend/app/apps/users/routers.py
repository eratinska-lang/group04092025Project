from fastapi import APIRouter, status

from apps.users.schemas import UserBaseFieldsSchema, RegisterUserSchema
from auth.password_handler import PasswordHandler

users_router = APIRouter()


@users_router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(user_data: RegisterUserSchema) -> UserBaseFieldsSchema:
    """create user based on name email password"""
    print(await PasswordHandler.get_password_hash(user_data.password))
    print(await PasswordHandler.get_password_hash(user_data.password))
    print(await PasswordHandler.get_password_hash(user_data.password))
    print(await PasswordHandler.get_password_hash(user_data.password))
    print(await PasswordHandler.get_password_hash(user_data.password))
    print(await PasswordHandler.get_password_hash(user_data.password))

    return user_data