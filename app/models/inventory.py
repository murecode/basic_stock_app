from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models.base import Base
from app.models.enums import MovementType

class Inventory(Base):
  __tablename__ = "inventory"
  id = Column(Integer, primary_key=True, index=True)
  product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  movement_type = Column(Enum(MovementType), nullable=False)
  quantity = Column(Integer, nullable=False)
  movement_timestamp = Column(DateTime(timezone=True), server_default=func.now())

  # Relaciones
  user = relationship("User", back_populates="inventory")
  product = relationship("Product", back_populates="inventory")