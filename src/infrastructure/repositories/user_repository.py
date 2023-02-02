from sqlalchemy.orm import Session
from infrastructure.schemas.user_schema import UserRequestSchema as RequestSchema
from infrastructure.schemas.user_schema import UserResponseSchema as ResponseSchema

class UserRepository:
  def __init__(self, session: Session):
    self.session = session

  def create_user(self, user: RequestSchema) -> ResponseSchema:
    self.session.add(user)
    self.session.commit()
    self.session.refresh(user)
    return user