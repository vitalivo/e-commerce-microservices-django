import pytest
from rest_framework.test import APIClient
from product.models import Product, Category  # Абсолютный импорт


@pytest.mark.django_db
def test_list_products():
    client = APIClient()
    response = client.get('/api/products/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.django_db
def test_create_product_unauthorized():
    client = APIClient()
    data = {
        "name": "Test Product",
        "price": "99.99",
        "stock": 10,
        "category_id": None
    }
    response = client.post('/api/products/', data)
    assert response.status_code == 401