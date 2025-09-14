# order-service/order/urls.py
from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('orders/', views.OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
]