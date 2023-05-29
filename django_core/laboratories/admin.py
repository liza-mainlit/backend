from django.contrib import admin


from laboratories.models import (
    Laboratory,
    LaboratoryEmployee,
    SocialNetResource,
    LaboratorySolutionCards
)


class LaboratoryTeamMemberInline(admin.TabularInline):
    model = LaboratoryEmployee
    extra = 1
    max_num = 6


class LaboratorySocialNetsInline(admin.TabularInline):
    model = SocialNetResource
    extra = 1


class LaboratorySolutionCardInline(admin.TabularInline):
    model = LaboratorySolutionCards
    extra = 1


@admin.register(Laboratory)
class LaboratoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "title",
                    "type",
                    "header_image",
                    "description",
                    "solutions",
                    "get_frontend_url",
                    "slug",
                )
            },
        ),
        (
            "Команда",
            {
                "fields": (
                    "team_description",
                    "team_director_bio",
                    "team_director_position",
                    "team_director_image",
                )
            }
        ),
        (
            "Контакты",
            {
                "fields": (
                    "team_image",
                    "logo",
                    "contact_bio",
                    "contact_email",
                    "contact_phone_number",
                    "contact_other"
                )
            }
        )
    )
    readonly_fields = ("get_frontend_url",)
    inlines = (LaboratoryTeamMemberInline, LaboratorySocialNetsInline, LaboratorySolutionCardInline)
