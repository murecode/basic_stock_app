from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
import app.crud.user as user_crud
import app.schemas.user as user_schemas

router = APIRouter()

@router.post("/users/", response_model=user_schemas.UserResponse)
def new_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
  db_user = user_crud.create_user(db=db, user=user)
  if db_user is None:
    raise HTTPException(status_code=400, detail="Error al crear el usuario")
  return db_user
