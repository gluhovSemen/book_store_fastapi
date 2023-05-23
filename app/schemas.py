from typing import Optional

from pydantic import BaseModel
from pydantic.schema import datetime


class SalesSchema(BaseModel):
    id: int
    book_id: int
    user_id: int
    book_title: str
    author: str
    purchase_price: float
    purchase_quantity: int
    created_at: datetime


class SalesSchemaDisplay(BaseModel):
    id: int
    book_id: int
    user_id: int
    book_title: str
    author: str
    purchase_price: float
    purchase_quantity: int
    created_at: datetime

    class Config:
        orm_mode = True


class MostSoldBookSchema(BaseModel):
    book_id: int

    class Config:
        orm_mode = True


class MostSoldDaysSchema(BaseModel):
    day: str
    total_sales: int

    class Config:
        orm_mode = True


class SoldDaysSchema(BaseModel):
    day: str

    class Config:
        orm_mode = True
