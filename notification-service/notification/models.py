from django.db import models
from django.utils.translation import gettext_lazy as _

class Notification(models.Model):
    user_id = models.IntegerField(verbose_name=_("ID пользователя"))
    event_type = models.CharField(
        max_length=50,
        verbose_name=_("Тип события"),
        help_text=_("Например: order_created, payment_success")
    )
    message = models.TextField(verbose_name=_("Сообщение"))
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Отправлено"))

    def __str__(self):
        return f"{self.event_type} → {self.user_id}"

    class Meta:
        db_table = 'notifications'
        verbose_name = _("Уведомление")
        verbose_name_plural = _("Уведомления")
        ordering = ['-sent_at']