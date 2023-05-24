import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.tests.conftests import test_app, sales
from app.tests.factories import SalesFactory



def test_sales(test_app):
    response = test_app.get("api/sales")
    assert response.status_code == 200


def test_sales_create(test_app, sales):
    response = test_app.get("api/sales")
    assert response.status_code == 200
