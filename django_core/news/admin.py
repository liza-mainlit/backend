from django.contrib import admin
from django.db import models

from .models import News, NewsImage, NewsPlacement, Registration, NewsSection
from registration_on_event.models import RegistrationForm


class NewsPlacementInline(admin.TabularInline):
    model = NewsPlacement
    extra = 1


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1


class NewsRegistrationInline(admin.StackedInline):
    model = Registration
    extra = 1


class NewsRegistrationFormInline(admin.TabularInline):
    model = RegistrationForm
    extra = 1


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "is_draft",
                    "short_description",
                    "description",
                    "source",
                    "news_type",
                    "tags",
                    "persons",
                    "units",
                    "show_in_feed",
                    "published_at",
                    "get_frontend_url",
                    "slug",
                )
            },
        ),
        ("Видео", {"fields": ("video", "video_link", "video_description")}),
        ("Фон", {"fields": ("background_image", "background_color")}),
    )
    readonly_fields = ("get_frontend_url",)
    inlines = (NewsPlacementInline, NewsImageInline, NewsRegistrationInline, NewsRegistrationFormInline)

    def get_queryset(self, request):
        queryset = News.objects.filter(is_deleted=False)
        return queryset

    def delete_queryset(self, request, queryset: models.QuerySet[News]):
        for news in queryset:
            news.is_deleted = True
            news.save()


@admin.register(NewsSection)
class NewsSectionAdmin(admin.ModelAdmin):
    pass
