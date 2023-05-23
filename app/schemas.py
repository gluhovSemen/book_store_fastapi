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
