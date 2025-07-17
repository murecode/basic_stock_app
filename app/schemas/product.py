from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
  title: str
  description: Optional[str] = None
  sku: str

class ProductCreate(ProductBase):
  sale_price: float
  purchase_price: float
  current_stock: Optional[int] = 0
  min_stock: Optional[int] = 0

  model_config = {
    "json_schema_extra": {
      "example": {
        "title": "SikaTop107",
        "description": "Mortero de alta compresion",
        "sku": "sk107",
        "sale_price": 254.0,
        "purchase_price": 330.2,
        "current_stock": 100,
        "min_stock": 10
      }
    }
  }

class ProductUpdate(ProductBase):
  title: Optional[str] = None
  description: Optional[str] = None
  sku: Optional[str] = None
  sale_price: Optional[float] = None  
  purchase_price: Optional[float] = None
  current_stock: Optional[int] = None
  min_stock: Optional[int] = None

class ProductResponse(ProductBase):
  id: int
  title: str
  description: Optional[str]
  sku: str
  sale_price: float
  purchase_price: float
  current_stock: int
  min_stock: int
  last_updated: datetime

  class Config:
    from_attributes = True