from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app import database

router = APIRouter(prefix="/api")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_sale(
    request: schemas.SalesSchema, database: Session = Depends(database.get_db)
):
    new_sale = await crud.create_sale(request, database)
    return new_sale
