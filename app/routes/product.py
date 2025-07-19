from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import get_db
import app.crud.product as product_crud
import app.schemas.product as product_schemas

router = APIRouter()

@router.get("/products/{product_id}", response_model=product_schemas.ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
  db_product = product_crud.get_product(db=db, product_id=product_id)
  if db_product is None:
    raise HTTPException(status_code=404, detail="Producto no encontrado")
  return db_product

@router.get("/products/", response_model=list[product_schemas.ProductResponse])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
  products = product_crud.get_products(db=db, skip=skip, limit=limit)
  return products

@router.post("/products/", response_model=product_schemas.ProductResponse)
def create_product(product: product_schemas.ProductCreate, db: Session = Depends(get_db)):
  db_product = product_crud.create_product(db=db, product=product)
  if db_product is None:
    raise HTTPException(status_code=400, detail="Error al crear el producto")
  return db_product

@router.put("/products/{product_id}", response_model=product_schemas.ProductResponse)
def update_product(product_id: int, product: product_schemas.ProductUpdate, db: Session = Depends(get_db)):
  db_product = product_crud.update_product(db=db, product_id=product_id, product=product)
  if db_product is None:
    raise HTTPException(status_code=404, detail="Producto no encontrado")
  return db_product

@router.delete("/products/{product_id}", response_model=product_schemas.ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
  db_product = product_crud.delete_product(db=db, product_id=product_id)
  if db_product is None:
    raise HTTPException(status_code=404, detail="Producto no encontrado")
  return db_product