from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import get_db
import app.crud.product as product_crud
import app.schemas.product as product_schemas

router = APIRouter()

@router.post("/products/", response_model=product_schemas.ProductResponse)
def create_product(product: product_schemas.ProductCreate, db: Session = Depends(get_db)):
  db_product = product_crud.create_product(db=db, product=product)
  if db_product is None:
    raise HTTPException(status_code=400, detail="Error al crear el producto")
  return db_product