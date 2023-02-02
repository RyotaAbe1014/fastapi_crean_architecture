from ..usecase.user_usecase import UserUsecase
from ..infrastructure.schemas.user_schema import UserRequestSchema as RequestSchema
from ..infrastructure.schemas.user_schema import UserResponseSchema as ResponseSchema


class UserController:
    def __init__(self, user_usecase):
        self.user_usecase = user_usecase

    def create_user(self, user: RequestSchema) -> ResponseSchema:
        return self.user_usecase.create_user(user)