import pytest
from rest_framework.test import APIClient
from order.models import Order


@pytest.mark.django_db
def test_list_orders_unauthorized():
    client = APIClient()
    response = client.get('/api/orders/')
    assert response.status_code == 401


@pytest.mark.django_db
def test_jwt_auth_with_token():
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU3NzQyODg4LCJpYXQiOjE3NTc3MzkyODgsImp0aSI6IjAzYjUzNzEyODgwYjRhM2Q5ZWZkYzZkYzQ5NzE1MDYxIiwidXNlcl9pZCI6IjEifQ"
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
    
    response = client.get('/api/orders/')
    assert response.status_code == 200