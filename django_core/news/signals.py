from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

from .models import News


@receiver(pre_save, sender=News)
def set_published_at(sender, instance: News, **kwargs) -> None:
    if not instance.published_at and not instance.is_draft:
        instance.published_at = timezone.now()
