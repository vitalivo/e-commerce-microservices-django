# order-service/order/serializers.py
from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'user_email',
            'total_price',
            'status',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'user_email']

    def validate_total_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(_("Стоимость должна быть больше 0"))
        return value