from datetime import datetime

import sqlalchemy
from fastapi_sqlalchemy import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette import status
from starlette.testclient import TestClient
from sqlalchemy_utils import database_exists, drop_database

from app import models
from app.database import get_db
from app.models import Sales
from app.settings import setting
from main import app

DATABASE_USERNAME = setting.DATABASE_USERNAME
DATABASE_PASSWORD = setting.DATABASE_PASSWORD
DATABASE_HOST = setting.DATABASE_HOST
DATABASE_NAME = setting.TEST_BASE_NAME

SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = sqlalchemy.orm.declarative_base()


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

session = TestingSessionLocal()
session.query(Sales).delete()
session.commit()
session.close()


def test_sales_create():
    response = client.post(
        "api/",
        json={
            "book_id": 0,
            "user_id": 0,
            "book_title": "string",
            "author": "string",
            "purchase_price": 0,
            "purchase_quantity": 0,
        },
    )
    assert response.status_code == status.HTTP_201_CREATED, response.text


def test_get_most_expensive_sale():
    # Create some sample sales records in the test database
    response = client.post(
        "api/",
        json={
            "book_id": 1,
            "user_id": 1,
            "book_title": "Book 1",
            "author": "Author 1",
            "purchase_price": 9.99,
            "purchase_quantity": 1,
        },
    )
    response = client.post(
        "api/",
        json={
            "book_id": 2,
            "user_id": 2,
            "book_title": "Book 2",
            "author": "Author 2",
            "purchase_price": 19.99,
            "purchase_quantity": 1,
        },
    )
    # Send a GET request to the endpoint
    response = client.get("api/sales/most-expensive")

    assert response.status_code == 200
    data = response.json()
    assert data["book_id"] == 2


def test_get_most_sold_book_by_quantity():
    # Create some sample sales records in the test database
    response = client.post(
        "api/",
        json={
            "book_id": 1,
            "user_id": 1,
            "book_title": "Book 1",
            "author": "Author 1",
            "purchase_price": 9.99,
            "purchase_quantity": 2,
        },
    )
    response = client.post(
        "api/",
        json={
            "book_id": 2,
            "user_id": 2,
            "book_title": "Book 2",
            "author": "Author 2",
            "purchase_price": 19.99,
            "purchase_quantity": 1,
        },
    )
    # Send a GET request to the endpoint
    response = client.get("api/sales/most-sold-book-by-quantity")

    assert response.status_code == 200
    data = response.json()
    assert data["book_id"] == 1

def test_get_most_sold_book_by_price():
    # Create some sample sales records in the test database
    response = client.post(
        "api/",
        json={
            "book_id": 1,
            "user_id": 1,
            "book_title": "Book 1",
            "author": "Author 1",
            "purchase_price": 10,
            "purchase_quantity": 5,
        },
    )
    response = client.post(
        "api/",
        json={
            "book_id": 2,
            "user_id": 2,
            "book_title": "Book 2",
            "author": "Author 2",
            "purchase_price": 100,
            "purchase_quantity": 2,
        },
    )
    # Send a GET request to the endpoint
    response = client.get("api/sales/most-sold-book-by-price")

    assert response.status_code == 200
    data = response.json()
    assert data["book_id"] == 2

def test_get_sales_by_user():
    # Create some sample sales records in the test database
    response = client.post(
        "api/",
        json={
            "book_id": 1,
            "user_id": 3,
            "book_title": "Book 1",
            "author": "Author 1",
            "purchase_price": 10,
            "purchase_quantity": 5,
        },
    )
    response = client.post(
        "api/",
        json={
            "book_id": 2,
            "user_id": 4,
            "book_title": "Book 2",
            "author": "Author 2",
            "purchase_price": 100,
            "purchase_quantity": 2,
        },
    )
    response = client.post(
        "api/",
        json={
            "book_id": 2,
            "user_id": 3,
            "book_title": "Book 2",
            "author": "Author 2",
            "purchase_price": 100,
            "purchase_quantity": 2,
        },
    )
    # Send a GET request to the endpoint
    response = client.get("api/sales/user/4")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["user_id"] == 4
    assert data[0]["book_id"] == 2
