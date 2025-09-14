# payment-service/payment/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext as _
from .models import Payment
from .serializers import PaymentSerializer


class ProcessPaymentView(APIView):
    """
    Обработка платежа
    """

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            # Имитация обработки
            payment = serializer.save(status='success', transaction_id=f"txn_{Payment.objects.count() + 1}")
            return Response({
                "success": True,
                "message": _("Платёж успешно обработан"),
                "data": PaymentSerializer(payment).data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "success": False,
            "message": _("Ошибка при обработке платежа"),
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class PaymentDetailView(APIView):
    def get_object(self, pk):
        try:
            return Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return None

    def get(self, request, pk):
        payment = self.get_object(pk)
        if not payment:
            return Response({"error": _("Платёж не найден")}, status=status.HTTP_404_NOT_FOUND)
        return Response({
            "success": True,
            "data": PaymentSerializer(payment).data
        })