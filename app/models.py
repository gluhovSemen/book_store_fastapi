from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from app.database import Base

class Sales(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer)
    user_id = Column(Integer)
    book_title = Column(String)
    author = Column(String)
    purchase_price = Column(Float)
    purchase_quantity = Column(Integer)
    created_at = Column(DateTime)
