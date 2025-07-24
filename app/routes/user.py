from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm as OAuth2Form
from sqlalchemy.orm import Session

from app.database import get_db
import app.crud.user as user_crud
from app.schemas.token import Token
import app.schemas.user as user_schemas
from app.crud.user import authenticate_user
from app.utils.jwt import create_access_token

router = APIRouter()

@router.post("/register/", response_model=user_schemas.UserResponse)
def user_registration(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
  db_user = user_crud.create_user(db=db, user=user)
  if db_user is None:
    raise HTTPException(status_code=400, detail="Error al crear el usuario")
  return db_user


@router.post("/login/", response_model=Token)
def user_login(email: str, form_data: OAuth2Form = Depends(), db: Session = Depends(get_db)):
  user = authenticate_user(db, form_data.username, form_data.password)
  if not user:
    raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
  access_token = create_access_token(data={"sub": user.id})
  return {"access_token": access_token, "token_type": "bearer"}