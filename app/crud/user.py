from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate

# def get_user(db: Session, user_id: int):
#   user = db.query(User).filter(User.id == user_id).first()
#   if user is None:
#     raise HTTPException(status_code=404, detail="Usuario no encontrado")
#   return user

def get_user_by_email(db: Session, email: str):
  user = db.query(User).filter(User.email == email).first()
  if user is None:
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
  return user

# def get_users(db: Session, skip: int = 0, limit: int = 10):
#   return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
  fake_hashed_password = user.password + "notreallyhashed"
  db_user = User(
    username=user.username,
    email=user.email,
    password=fake_hashed_password,
  )
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user