import time
from bson import ObjectId
from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class ProductCategory(str, Enum):
    electronics = "Electronics",
    clothing = "Clothing"
    stationary = "Stationary"
    sports = "Sports"
    furniture = "Furniture"

class Image(BaseModel):
    url: str
    altText: str

class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=250)
    price: float = Field(..., gt=0)
    stockAvailable: int = Field(..., gt=0)
    category: ProductCategory
    isAvailableForSale: bool
    images: List[Image]
    specification: Dict

class Product(ProductBase):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")

class ProductCreate(Product):
    createdAt: int = Field(default_factory=lambda: int(time.time()), alias="createdAt")

class ProductUpdate(Product):
    updatedAt: int = Field(default_factory=lambda: int(time.time()), alias="updatedAt")
