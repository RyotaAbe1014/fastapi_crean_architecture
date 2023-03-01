from entities.user import User
from .input.user_input import UserInputData


class UserCreateInteractor:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def create_user(self, user: UserInputData) -> User:  
        return self.user_repo.create_user(user) 
