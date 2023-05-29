from django.db import models
from news.models import News


# Create your models here.
class RegistrationForm(models.Model):
    news: News = models.ForeignKey(
        to=News, on_delete=models.CASCADE, verbose_name="Новость", related_name="registration_form"
    )
    name = models.CharField(
        max_length=255, verbose_name="Имя"
    )
    second_name = models.CharField(
        max_length=255, verbose_name="Фамилия"
    )
    number = models.CharField(
        max_length=255, verbose_name="Телефон"
    )
    email = models.EmailField(
        max_length=255, verbose_name="Почта"
    )
    work_or_study_place = models.CharField(
        max_length=255, verbose_name="Место работы/учёбы"
    )
    comment = models.CharField(
        blank=True, null=True, max_length=255, verbose_name="Комментарий"
    )

    class Meta:
        verbose_name = "Регистрация на мероприятие"
        verbose_name_plural = "Регистрации на мероприятие"
