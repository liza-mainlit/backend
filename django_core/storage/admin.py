from django.contrib import admin

from .models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "get_url")
    readonly_fields = ("get_url",)
    search_fields = ("file",)
    list_filter = ("created_at",)
