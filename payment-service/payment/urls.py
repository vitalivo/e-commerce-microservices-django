# payment-service/payment/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('payments/process/', views.ProcessPaymentView.as_view(), name='process-payment'),
    path('payments/<int:pk>/', views.PaymentDetailView.as_view(), name='payment-detail'),
]