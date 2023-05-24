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
    total_sales = func.sum(models.Sales.purchase_quantity).label("total_sales")

    book_id = (
        database.query(models.Sales.book_id, total_sales)
        .group_by(models.Sales.book_id)
        .order_by(total_sales.desc())
        .first()
    )

    return book_id


def most_sold_book_by_price(database):
    total_value = func.sum(
        models.Sales.purchase_price * models.Sales.purchase_quantity
    ).label("total_value")

    book_id = (
        database.query(models.Sales.book_id, total_value)
        .group_by(models.Sales.book_id)
        .order_by(total_value.desc())
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
    day_label = func.date(models.Sales.created_at).label("day")
    total_sales_label = func.sum(models.Sales.purchase_quantity).label("total_sales")

    most_sold_days = (
        database.query(day_label, total_sales_label)
        .group_by(day_label)
        .order_by(total_sales_label.desc())
        .all()
    )

    return most_sold_days


def sold_days_for_book(database, book_id):
    day_label = func.date(models.Sales.created_at).label("day")

    sold_days = (
        database.query(day_label)
        .filter(models.Sales.book_id == book_id)
        .group_by(day_label)
        .all()
    )

    return sold_days
