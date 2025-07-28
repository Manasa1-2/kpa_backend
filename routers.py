from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import get_db

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)

@router.post("/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@router.get("/", response_model=list[schemas.Item])
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

@router.get("/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crud.delete_item(db, item_id)
