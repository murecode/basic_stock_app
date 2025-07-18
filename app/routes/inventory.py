from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.inventory import create_inventory_movement
from app.schemas.inventory import InventoryMovement, InventoryResponse

router = APIRouter()

@router.post("/inventory/movements/", response_model=InventoryResponse)
def new_inventory_movement(movement: InventoryMovement, db: Session = Depends(get_db)):
  db_movement = create_inventory_movement(db=db, movement=movement)
  if db_movement is None:
    raise HTTPException(status_code=400, detail="Error al crear el movimiento de inventario")
  return db_movement