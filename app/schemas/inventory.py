from pydantic import BaseModel
from datetime import datetime

from app.models.enums import MovementType


class InventoryBase(BaseModel):
  movement_type: MovementType
  quantity: int
    
class InventoryMovement(InventoryBase):
  product_id: int 
  user_id: int

  model_config = {
    "json_schema_extra": {
      "example": {
        "product_id": 1,
        "user_id": 1,
        "movement_type": MovementType.ENTRADA,
        "quantity": 50
      }
    }
  }

class InventoryResponse(InventoryBase):
  id: int
  movement_type: MovementType
  quantity: int
  movement_timestamp: datetime

  class Config:
    from_attributes = True