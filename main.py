from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "KPA Backend is running"}

# Create Item
@app.post("/items/", response_model=schemas.ItemOut)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

# Read all items
@app.get("/items/", response_model=list[schemas.ItemOut])
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

# Read item by ID
@app.get("/items/{item_id}", response_model=schemas.ItemOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# Update item
@app.put("/items/{item_id}", response_model=schemas.ItemOut)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.update_item(db, item_id=item_id, item=item)

# Delete item
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crud.delete_item(db, item_id=item_id)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)