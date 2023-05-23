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
