from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
  username: str
  email: EmailStr

class UserCreate(UserBase):
  password: str

# class UserUpdate(BaseModel):
#   username: Optional[str] = None
#   email: Optional[EmailStr] = None
#   password: Optional[str] = None
#   is_active: Optional[bool] = None  

class UserResponse(UserBase):
  id: int
  is_active: bool
  created_at: datetime

  # convierte el modelo a un diccionario
  class Config:
    from_attributes = True # Permite que Pydantic trabaje con modelos de SQLAlchemy