from fastapi import FastAPI

from app.routes import user as user_routes
from app.routes import product as product_routes

from app.database import engine
from app.models.base import Base

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Crear la instancia de FastAPI
app = FastAPI(
  title="BasicStock App",
  description="Sistema de gestion básico de inventario",
  version="1.0.0",
)

app.include_router(user_routes.router, prefix="/api", tags=["users"])
app.include_router(product_routes.router, prefix="/api", tags=["products"])







# @app.get("/products/{product_id}", response_model=product.ProductResponse)
# def read_product(product_id: int, db: Session = Depends(get_db)):
#   db_product = product.get_product(db=db, product_id=product_id)
#   if db_product is None:
#     raise HTTPException(status_code=404, detail="Producto no encontrado")
#   return db_product


# @app.get("/products/", response_model=list[product.ProductResponse])
# def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#   products = product.get_products(db=db, skip=skip, limit=limit)
#   return products


# @app.put("/products/{product_id}", response_model=product.ProductResponse)
# def update_product(product_id: int, product: product.ProductUpdate, db: Session = Depends(get_db)):
#   db_product = crud.update_product(db=db, product_id=product_id, product=product)
#   if db_product is None:
#     raise HTTPException(status_code=404, detail="Producto no encontrado")
#   return db_product


# @app.delete("/products/{product_id}", response_model=product.ProductResponse)
# def delete_product(product_id: int, db: Session = Depends(get_db)): 
#   db_product = crud.delete_product(db=db, product_id=product_id)
#   if db_product is None:
#     raise HTTPException(status_code=404, detail="Producto no encontrado")
#   return db_product
