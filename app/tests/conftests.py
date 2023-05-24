import pytest
from starlette.testclient import TestClient

from app.tests.factories import SalesFactory
from main import app
from pytest_postgresql import factories



@pytest.fixture
def test_app():
    client = TestClient(app)
    return client

@pytest.fixture
def sales(test_app):
    # client = TestClient(app)
    return SalesFactory.create()
