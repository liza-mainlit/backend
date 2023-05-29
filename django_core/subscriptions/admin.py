from django.contrib import admin
from import_export.admin import ExportActionModelAdmin

from .models import Subscription


class SubscriptionAdmin(ExportActionModelAdmin):
    readonly_fields = ("created_at",)


admin.site.register(Subscription, SubscriptionAdmin)
