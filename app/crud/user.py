from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.password import verify_password, hash_password


def get_user(db: Session, user_id: int):
  user = db.query(User).filter(User.id == user_id).first()
  if user is None:
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
  return user


def get_users(db: Session, skip: int = 0, limit: int = 10):
  return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
  hashed_password = hash_password(user.password)
  db_user = User(
    username=user.username,
    email=user.email,
    password=hashed_password,
  )
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user


def authenticate_user(db: Session, email: str, password: str):
  user = db.query(User).filter(User.email == email).first()
  if not user or not verify_password(password, user.password):
    raise HTTPException(status_code=401, detail="Credenciales incorrectas")
  return user


# def get_user_by_email(db: Session, email: str):
#   user = db.query(User).filter(User.email == email).first()
#   if user is None:
#     raise HTTPException(status_code=404, detail="Usuario no encontrado")
#   return user