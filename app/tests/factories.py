from datetime import datetime
import factory
from app.models import Sales




class SalesFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Sales

    id = factory.Sequence(lambda n: n)
    book_id = factory.Sequence(lambda n: n + 1)
    user_id = factory.Sequence(lambda n: n + 2)
    book_title = factory.Faker("sentence")
    author = factory.Faker("name")
    purchase_price = factory.Faker("random_number", digits=2)
    purchase_quantity = factory.Faker("random_int", min=1, max=10)
    created_at = datetime.now()
