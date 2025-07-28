from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True


# ✅ Add these Item schemas 👇
class ItemBase(BaseModel):
    title: str
    description: str

class ItemCreate(ItemBase):
    pass

class ItemOut(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

