# order-service/order/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name=_("Пользователь")
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Общая стоимость")
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', _("Ожидание")),
            ('confirmed', _("Подтверждён")),
            ('shipped', _("Отправлен")),
            ('delivered', _("Доставлен")),
            ('cancelled', _("Отменён")),
        ],
        default='pending',
        verbose_name=_("Статус")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Создан")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Обновлён")
    )

    def __str__(self):
        return f"Заказ {self.id} от {self.user.email}"

    class Meta:
        db_table = 'orders'
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")
        ordering = ['-created_at']