from fastapi import HTTPException
from sqlalchemy.orm import Session
import models, schemas

def create_inventory_movement(db: Session, movement: schemas.inventory_movement.InventoryMovementCreate):
  db_movement = models.InventoryMovement(
    product_id = movement.product_id,
    user_id = movement.user_id,
    movement_type = movement.movement_type,
    quantity = movement.quantity
  )

  # Verificar si el producto existe
  product = db.query(models.Products).filter(models.Products.id == movement.product_id).first()
  if not product:
    raise HTTPException(status_code=404, detail="Producto no encontrado")
  
  # Verifica si hay suficiente stock
  if product.current_stock < 0:
    raise HTTPException(status_code=400, detail="Stock insuficiente para la salida")
  
  # Actualizar stock en tiempo real
  if movement.movement_type == models.MovementType.entrada:
    product.current_stock += movement.quantity
  elif movement.movement_type == models.MovementType.salida:
    product.current_stock -= movement.quantity
  

  db.add(db_movement)
  db.commit()
  db.refresh(db_movement)
  return db_movement


def get_movements_by_product(db: Session, product_id: int):
    return db.query(models.InventoryMovement).filter(models.InventoryMovement.product_id == product_id).all()


def get_inventory_movements(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.InventoryMovement).offset(skip).limit(limit).all()
