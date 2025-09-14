# payment-service/payment/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _

class Payment(models.Model):
    order_id = models.IntegerField(verbose_name=_("ID заказа"))
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Сумма"))
    payment_method = models.CharField(
        max_length=50,
        choices=[
            ('card', _('Карта')),
            ('paypal', 'PayPal'),
            ('apple_pay', 'Apple Pay'),
        ],
        verbose_name=_("Способ оплаты")
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', _('Ожидание')),
            ('success', _('Успешно')),
            ('failed', _('Ошибка')),
            ('refunded', _('Возврат'))
        ],
        default='pending',
        verbose_name=_("Статус")
    )
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Платёж {self.id} за заказ {self.order_id}"

    class Meta:
        db_table = 'payments'
        verbose_name = _("Платёж")
        verbose_name_plural = _("Платежи")