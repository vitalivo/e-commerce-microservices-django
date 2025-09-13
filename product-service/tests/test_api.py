import pytest
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Product, Category

@pytest.mark.django_db
def test_product_list():
    client = APIClient()
    response = client.get('/api/products/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)