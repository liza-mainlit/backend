from django.contrib import admin
from tinymce.widgets import TinyMCE

from marketplaces.models import Solution, SolutionResourceButton, DataSourceBlock, DataSource, SolutionCard


class PageAdmin(admin.ModelAdmin):
    formfield_overrides = {
        'widget': {'widget': TinyMCE()},
    }


class SolutionResourceButtonInline(admin.TabularInline):
    model = SolutionResourceButton
    extra = 1


class DataSourceBlockInline(admin.TabularInline):
    model = DataSourceBlock
    extra = 1


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Основная информация',
            {
                "fields": (
                    "title",
                    "license",
                    "technology",
                    "unit",
                    "laboratory",
                    "supervisor",
                    "supervisor_contacts",
                    "description",
                    "get_frontend_url",
                    "slug",
                )
            },
        ),
        ("Шапка", {"fields": ("header_image", "header_color")}),
        ("Кнопка \"Перейти к ...\"", {"fields": ("button_title", "button_url", "button_description")}),
    )
    readonly_fields = ("get_frontend_url",)
    inlines = (SolutionResourceButtonInline, DataSourceBlockInline)


@admin.register(DataSource)
class DataSourceAdmin(admin.ModelAdmin):
    pass


@admin.register(SolutionCard)
class SolutionCardAdmin(admin.ModelAdmin):
    pass
