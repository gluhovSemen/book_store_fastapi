from pydantic import BaseModel, validator
from pydantic.schema import datetime


class BaseSalesSchema(BaseModel):
    book_id: int
    user_id: int
    book_title: str
    author: str
    purchase_price: float
    purchase_quantity: int

    @validator("book_id", "user_id")
    def validate_ids(cls, value):
        if value < 0:
            raise ValueError("IDs must not be less than 0")
        return value


class SalesSchemaDisplay(BaseSalesSchema):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class MostSoldBookSchema(BaseModel):
    book_id: int

    class Config:
        orm_mode = True


class SoldDaysSchema(BaseModel):
    day: str

    class Config:
        orm_mode = True


class MostSoldDaysSchema(SoldDaysSchema):
    total_sales: int

    class Config:
        orm_mode = True
