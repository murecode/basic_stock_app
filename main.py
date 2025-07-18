from fastapi import FastAPI

from app.routes import user as user_routes
from app.routes import product as product_routes
from app.routes import inventory as inventory_routes

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
app.include_router(inventory_routes.router, prefix="/api", tags=["inventory"])