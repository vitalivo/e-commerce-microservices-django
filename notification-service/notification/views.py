from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.translation import gettext as _
from .models import Notification
from .serializers import NotificationSerializer

class NotifyView(APIView):
    """
    Принимает уведомление и сохраняет в БД
    """

    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            notification = serializer.save()
            return Response({
                "success": True,
                "message": _("Уведомление успешно создано"),
                "data": NotificationSerializer(notification).data
            }, status=201)
        return Response({
            "success": False,
            "message": _("Ошибка при создании уведомления"),
            "errors": serializer.errors
        }, status=400)