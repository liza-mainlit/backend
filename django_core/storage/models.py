from django.db import models
from django.utils.html import format_html
from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save
from django_core.settings import env


class File(models.Model):
    file = models.FileField(upload_to="storage/", verbose_name="Файл")
    created_at = models.DateTimeField(auto_now_add=True)

    def get_url(self) -> str:
        frontend_storage_url = f'{"https" if env.bool("USE_HTTPS_STORAGE") else "http"}://{env.str("HOST")}/media/storage/'
        if self.pk:
            frontend_url = frontend_storage_url + str(self.name())
            return format_html(f"<a href='{frontend_url}'>{frontend_url}</a>")
        return ""

    get_url.short_description = "Ссылка на файл"

    def name(self) -> str:
        return self.file.name["storage/".__len__():]

    name.short_description = "Имя файла"

    def __str__(self) -> str:
        return self.file.name

    class Meta:
        verbose_name = "Файл в хранилище"
        verbose_name_plural = "Файлы в хранилище"


@receiver(post_delete, sender=File)
def clean_file(sender, instance, *args, **kwargs):
    """ Clean Deleted File """
    try:
        instance.file.delete(save=False)
    except:
        pass


@receiver(pre_save, sender=File)
def clean_old_file(sender, instance, *args, **kwargs):
    """ Rewrite Old File """
    try:
        old_file = File.objects.get(pk=instance.pk).file
        if old_file != instance.file:
            old_file.delete(save=False)
    except:
        pass
