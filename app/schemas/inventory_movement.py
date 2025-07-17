from time import timezone
from pydantic import BaseModel, Field
from datetime import datetime
from app.models.enums import MovementType
from app.schemas.product import ProductResponse
from app.schemas.user import UserResponse

class InventoryMovementBase(BaseModel):
  movement_type: MovementType = Field(..., description="Tipo de movimiento")
  quantity: int = Field(..., gt=0, description="Cantidad del movimiento")
    

class InventoryMovementCreate(InventoryMovementBase):
  product_id: int = Field(..., description="ID del producto asociado")
  user_id: int = Field(..., description="ID del usuario responsable")


class InventoryMovementResponse(InventoryMovementBase):
  id: int = Field(..., description="ID único del movimiento")
  product: ProductResponse
  user: UserResponse
  movement_type: MovementType
  quantity: int
  movement_timestamp: datetime = Field(
    default_factory=lambda: datetime.now(timezone.utc),
    description="Fecha y hora del movimiento"
  )
  class Config:
    from_attributes = True