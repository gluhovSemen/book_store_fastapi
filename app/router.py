from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from typing import List
from app import services, schemas
from app import database
from app.database import get_db
from app.models import Sales
from app.schemas import SalesSchema, SalesSchemaDisplay

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
