from django.db import models


class ABSTag(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Tag(ABSTag):
    class Meta:
        verbose_name = "Тематика"
        verbose_name_plural = "Тематики"


class NewsType(ABSTag):
    class Meta:
        verbose_name = "Рубрика"
        verbose_name_plural = "Рубрики"


class Person(ABSTag):
    class Meta:
        verbose_name = "Персона"
        verbose_name_plural = "Персоны"


class Unit(ABSTag):
    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"


class Technology(ABSTag):
    class Meta:
        verbose_name = "Технология"
        verbose_name_plural = "Технологии"
