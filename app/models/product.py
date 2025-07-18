from sqlalchemy import Column, Integer, String, DateTime, Text, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.models.base import Base

class Product(Base):
  __tablename__ = "products"
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  description = Column(Text, nullable=True)
  sku = Column(String, unique=True, index=True)
  sale_price = Column(Float, nullable=False)
  purchase_price = Column(Float, nullable=False)
  current_stock = Column(Integer, default=0)
  min_stock = Column(Integer, default=0)
  last_updated = Column(DateTime(timezone=True), server_default=func.now())

  # Relaciones
  inventory = relationship("Inventory", back_populates="product")




## Documentation:

# server_default=func.now() -> Establece que, al crear un nuevo registro,
# esta columna tendrá como valor por defecto la hora actual del servidor.

# onupdate=func.now() -> Cada vez que el registro sea modificado, last_updated
# se actualizará automáticamente con la nueva fecha/hora de edición.
# Muy útil para seguimiento de cambios y trazabilidad.