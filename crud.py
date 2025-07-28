from sqlalchemy.orm import Session
from app import models, schemas

# Create Item
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Read all Items
def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Item).offset(skip).limit(limit).all()

# Read single Item
def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

# Delete Item
def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
