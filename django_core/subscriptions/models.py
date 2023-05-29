from django.db import models


class Subscription(models.Model):

    email = models.EmailField(verbose_name="Адрес электронной почты")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = "Подписка на рассылку"
        verbose_name_plural = "Подписки на рассылку"
