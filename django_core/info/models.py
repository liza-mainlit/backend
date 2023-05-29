from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название вкладки')
    url = models.URLField(verbose_name='Ссылка куда ведет кнопка')
    order = models.PositiveIntegerField(verbose_name='Порядок отображения', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вкладка информации'
        verbose_name_plural = 'Вкладки информации'
        ordering = ['order']
