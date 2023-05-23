from sqlalchemy.orm import Session

from .models import Sales
from .schemas import SalesSchema


def create_sale(db: Session, sale: SalesSchema):
    # Create a new instance of the Sales model using the request data
    new_sale = Sales(
        book_id=sale.book_id,
        user_id=sale.user_id,
        book_title=sale.book_title,
        author=sale.author,
        purchase_price=sale.purchase_price,
        purchase_quantity=sale.purchase_quantity,
        created_at=sale.created_at
    )

    # Add the new sale to the session
    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)

    return new_sale
