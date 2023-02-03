from sqlalchemy.orm import Session
from infrastructure.schemas.user_schema import UserRequestSchema as RequestSchema
from infrastructure.schemas.user_schema import UserResponseSchema as ResponseSchema
from infrastructure.databases.models.user import User

class UserRepository:
  def __init__(self, session: Session):
    self.session = session

  def create_user(self, input: RequestSchema) -> ResponseSchema:
    user = User(name=input.name, email=input.email, password=input.password)
    self.session.add(user)
    self.session.commit()
    self.session.refresh(user)
    return user