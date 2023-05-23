from fastapi import APIRouter, status, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from app import services, schemas
from app import database
from app.database import get_db

router = APIRouter(prefix="/api")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_sale(
    request: schemas.SalesSchema, database: Session = Depends(database.get_db)
):
    new_sale = await services.create_sale(request, database)
    return new_sale


@router.get("/sales", response_model=List[schemas.SalesSchemaDisplay])
def get_all_sales(database: Session = Depends(database.get_db)):
    return services.all_sales(database)


@router.get("/sales/most_expensive", response_model=schemas.SalesSchemaDisplay)
def get_most_expensive_sale(database: Session = Depends(get_db)):
    return services.most_expensive_sale(database)


@router.get(
    "/sales/most_sold_book_by_quantity", response_model=schemas.MostSoldBookSchema
)
def get_most_sold_book_by_quantity(database: Session = Depends(get_db)):
    return services.most_sold_book_by_quantity(database)


@router.get("/sales/most_sold_book_by_price", response_model=schemas.MostSoldBookSchema)
def get_most_sold_book_by_price(database: Session = Depends(get_db)):
    return services.most_sold_book_by_price(database)


@router.get("/sales/user/{user_id}", response_model=List[schemas.SalesSchemaDisplay])
def get_sales_by_user(user_id: int, database: Session = Depends(get_db)):
    return services.sales_by_user(database, user_id)


@router.get("/sales/date", response_model=List[schemas.SalesSchemaDisplay])
def get_sales_by_day(day: str = Query(...), database: Session = Depends(get_db)):
    return services.sales_by_date(database, day)


@router.get("/sales/most_sold_days", response_model=List[schemas.MostSoldDaysSchema])
def get_most_sold_days(database: Session = Depends(get_db)):
    most_sold_days = services.most_sold_days(database)
    return [
        {"day": str(day), "total_sales": total_sales}
        for day, total_sales in most_sold_days
    ]


@router.get("/sales/book/{book_id}/sold_days", response_model=List[str])
def get_sold_days_for_book(book_id: int, database: Session = Depends(get_db)):
    sold_days = services.sold_days_for_book(database, book_id)
    return [str(day[0]) for day in sold_days]
