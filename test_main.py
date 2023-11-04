from fastapi.testclient import TestClient
from main import Item, app
import pytest

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": None}

def test_read_item_with_query():
    response = client.get("/items/1?q=foo")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": "foo"}

def test_update_item():
    item = Item(name="foo", price=1.0, is_offer=True)
    response = client.put("/items/1", json=item.dict())
    assert response.status_code == 200
    assert response.json() == {"item_name": "foo", "item_price": 1.0, "item_id": 1}


