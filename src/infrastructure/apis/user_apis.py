from fastapi import APIRouter, Depends, HTTPException
from ..schemas.user_schema import UserRequestSchema as RequestSchema
from ..schemas.user_schema import UserResponseSchema as ResponseSchema
from controller.user_controller import UserController
from usecase.user_usecase import UserUsecase
from ..repositories.user_repository import UserRepositorys

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/")
async def create_user(input: RequestSchema)-> ResponseSchema:
    user_repository = 
    user_usecase = UserUsecase(user_repository)
    user_controller = UserController(user_usecase)
    return user_controller.create_user(input)
    