from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse


def get_product(db: Session, product_id: int):
  product = db.query(Product).filter(Product.id == product_id).first()
  if product is None:
      raise HTTPException(status_code=404, detail="Producto no encontrado")
  return product

def get_products(db: Session, skip: int = 0, limit: int = 10):
  return db.query(Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: ProductCreate):
  db_product = Product(
    title=product.title,
    description=product.description,
    sku=product.sku,
    sale_price=product.sale_price,
    purchase_price=product.purchase_price,
    current_stock=product.current_stock or 0,
    min_stock=product.min_stock or 0
  )
  db.add(db_product)
  db.commit()
  db.refresh(db_product)
  return db_product

def update_product(db: Session, product_id: int, product: ProductUpdate):
  db_product = db.query(Product).filter(Product.id == product_id).first()
  if db_product is None:
      raise HTTPException(status_code=404, detail="Producto no encontrado")
  for key, value in product.dict(exclude_unset=True).items():
      setattr(db_product, key, value)
  db.commit()
  db.refresh(db_product)
  return db_product

def delete_product(db: Session, product_id: int):
  db_product = db.query(Product).filter(Product.id == product_id).first()
  if db_product is None:
      raise HTTPException(status_code=404, detail="Producto no encontrado")
  db.delete(db_product)
  db.commit()
  return db_product