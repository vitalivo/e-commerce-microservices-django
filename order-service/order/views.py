from rest_framework.views import APIView
# order-service/order/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from .models import Order
from .serializers import OrderSerializer

def post(self, request):
    user = request.user  # ← из JWT
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save(user=user)  # ← привязываем
        return Response(...)
    
class OrderListCreateView(APIView):
    """
    GET: Получить список всех заказов
    POST: Создать новый заказ
    """

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response({
            "success": True,
            "message": _("Заказы успешно получены"),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response({
                "success": True,
                "message": _("Заказ успешно создан"),
                "data": OrderSerializer(order).data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "success": False,
            "message": _("Ошибка при создании заказа"),
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(APIView):
    """
    GET / PATCH / DELETE для конкретного заказа
    """

    def get_object(self, pk):
        return get_object_or_404(Order, pk=pk)

    def get(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response({
            "success": True,
            "message": _("Информация о заказе получена"),
            "data": serializer.data
        })

    def patch(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": _("Заказ успешно обновлён"),
                "data": serializer.data
            })
        return Response({
            "success": False,
            "message": _("Ошибка при обновлении заказа"),
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = self.get_object(pk)
        order.delete()
        return Response({
            "success": True,
            "message": _("Заказ успешно удалён")
        }, status=status.HTTP_204_NO_CONTENT)