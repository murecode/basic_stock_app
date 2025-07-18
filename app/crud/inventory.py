from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.inventory import InventoryMovement
from app.models.inventory import Inventory
from app.models.product import Product
from app.models.enums import MovementType
from app.models.user import User


def create_inventory_movement(db: Session, movement: InventoryMovement):
  db_movement = Inventory(
    product_id = movement.product_id,
    user_id = movement.user_id,
    movement_type = movement.movement_type,
    quantity = movement.quantity
  )
  # Verificar si el producto existe
  product = db.query(Product).filter(Product.id == movement.product_id).first()
  if not product:
    raise HTTPException(status_code=404, detail="Producto no encontrado")
  # Verificar si el usuario existe
  user = db.query(User).filter(User.id == movement.user_id).first()
  if not user:
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
  # Verifica si hay suficiente stock
  if product.current_stock < 0:
    raise HTTPException(status_code=400, detail="Stock insuficiente para la salida")
  # Actualizar stock en tiempo real
  if movement.movement_type == MovementType.ENTRADA:
    product.current_stock += movement.quantity
  elif movement.movement_type == MovementType.SALIDA:
    product.current_stock -= movement.quantity
  # Guardar movimiento en la base de datos
  db.add(db_movement)
  db.commit()
  db.refresh(db_movement)
  return db_movement

def get_movements_by_product(db: Session, product_id: int):
    return db.query(Inventory).filter(Inventory.product_id == product_id).all()

def get_inventory_movements(db: Session, skip: int = 0, limit: int = 10):
    return db.query(InventoryMovement).offset(skip).limit(limit).all()
