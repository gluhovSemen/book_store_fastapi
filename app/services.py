from sqlalchemy import func

from . import models


async def create_sale(request, database):
    # Create a new instance of the Sales model using the request data
    new_sale = models.Sales(
        book_id=request.book_id,
        user_id=request.user_id,
        book_title=request.book_title,
        author=request.author,
        purchase_price=request.purchase_price,
        purchase_quantity=request.purchase_quantity,
    )

    # Add the new sale to the session
    database.add(new_sale)
    database.commit()
    database.refresh(new_sale)

    return new_sale


def all_sales(database):
    sales = database.query(models.Sales).all()
    return sales


def most_expensive_sale(database):
    sale = (
        database.query(models.Sales)
        .order_by(models.Sales.purchase_price.desc())
        .first()
    )
    return sale


def most_sold_book_by_quantity(database):
    book_id = (
        database.query(
            models.Sales.book_id,
            func.sum(models.Sales.purchase_quantity).label("total_sales"),
        )
        .group_by(models.Sales.book_id)
        .order_by(func.sum(models.Sales.purchase_quantity).desc())
        .first()
    )
    return book_id


def most_sold_book_by_price(database):
    book_id = (
        database.query(
            models.Sales.book_id,
            func.sum(
                models.Sales.purchase_price * models.Sales.purchase_quantity
            ).label("total_value"),
        )
        .group_by(models.Sales.book_id)
        .order_by(
            func.sum(
                models.Sales.purchase_price * models.Sales.purchase_quantity
            ).desc()
        )
        .first()
    )
    return book_id


def sales_by_user(database, user_id):
    sales = database.query(models.Sales).filter(models.Sales.user_id == user_id).all()
    return sales


def sales_by_date(database, day):
    sales = (
        database.query(models.Sales)
        .filter(func.date(models.Sales.created_at) == day)
        .all()
    )
    return sales


def most_sold_days(database):
    most_sold_days = (
        database.query(
            func.date(models.Sales.created_at).label("day"),
            func.sum(models.Sales.purchase_quantity).label("total_sales"),
        )
        .group_by(func.date(models.Sales.created_at))
        .order_by(func.sum(models.Sales.purchase_quantity).desc())
        .all()
    )
    return most_sold_days


def sold_days_for_book(database, book_id):
    sold_days = (
        database.query(func.date(models.Sales.created_at).label("day"))
        .filter(models.Sales.book_id == book_id)
        .group_by(func.date(models.Sales.created_at))
        .all()
    )
    return sold_days
