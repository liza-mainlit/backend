import re

from django.db import models
from django.utils.html import format_html
from transliterate import translit
from django_lifecycle import AFTER_CREATE, hook, LifecycleModel, AFTER_UPDATE
from tinymce.models import HTMLField

from django_core.settings import env
from marketplaces.models import SolutionCard


class Laboratory(LifecycleModel):
    title = models.CharField(max_length=255, verbose_name="Название")
    type = models.CharField(max_length=255, verbose_name="Тип лаборатории")
    header_image = models.ImageField(
        upload_to="laboratories_images",
        verbose_name="Фото в верхней части страницы 16x9",
    )
    description = HTMLField(verbose_name="Описание")
    solutions = models.TextField(verbose_name="Решения")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL", null=True, blank=True)

    def get_frontend_url(self) -> str:
        frontend_laboratories_base_url = (
            f'{"https" if env.bool("USE_HTTPS") else "http"}://'
            f'{env.str("HOST")}/laboratories/'
        )
        if self.pk:
            slug = re.sub(
                r"[^a-zA-Z0-9-_]+",  # оставляем все [a-zA-Z0-9-_] символы
                "",
                translit((self.slug or self.title), "ru", reversed=True)  # транслит заголовка
                .replace(" ", "-").lower()  # меняем пробелы на тире
            )
            frontend_url = frontend_laboratories_base_url + slug
            return format_html(f"<a href='{frontend_url}'>{frontend_url}</a>")
        return ""

    get_frontend_url.short_description = "Ссылка на лабораторию на сайте"
    laboratory_url = property(get_frontend_url)

    # --- Команда разработки ---
    team_description = models.CharField(max_length=255, verbose_name="Описание команды")
    team_director_bio = models.CharField(max_length=255, verbose_name="ФИО руководителя")
    team_director_position = models.CharField(max_length=100, verbose_name="Должность руководителя")
    team_director_image = models.ImageField(
        upload_to="laboratories_directors_images",
        verbose_name="Фото руководителя",
        blank=True,
        null=True
    )

    # --- Контакты лаборатории ---
    team_image = models.ImageField(
        upload_to="laboratory_team_images",
        verbose_name="Фото команды",
        blank=True,
        null=True
    )
    logo = models.ImageField(
        upload_to="laboratories_logo_images",
        verbose_name="Логотип лаборатории",
        blank=True,
        null=True
    )
    contact_bio = models.CharField(
        max_length=100,
        verbose_name="ФИО контактного лица",
        blank=True,
        null=True
    )
    contact_email = models.EmailField(verbose_name="Контактный email", blank=True, null=True)
    contact_phone_number = models.CharField(
        max_length=11,
        verbose_name="Контактный номер телефона",
        blank=True,
        null=True
    )
    contact_other = models.CharField(max_length=255, verbose_name="Другое", blank=True, null=True)

    class Meta:
        verbose_name = "Лаборатория"
        verbose_name_plural = "Лаборатории"

    def __generate_slug_by_title(self) -> str:
        return re.sub(
            r"[^a-zA-Z0-9-_]+",  # оставляем все [a-zA-Z0-9-_] символы
            "",
            translit(self.title, "ru", reversed=True)  # транслит заголовка
            .replace(" ", "-").lower()  # меняем пробелы на тире
        )

    @hook(AFTER_UPDATE, when="slug", is_now=None)
    @hook(AFTER_CREATE)
    def generate_slug(self) -> None:
        if not self.slug:
            self.slug = self.__generate_slug_by_title()
            self.save()

    def __str__(self) -> str:
        return self.title


class LaboratoryEmployee(models.Model):
    bio = models.CharField(max_length=255, verbose_name="ФИО сотрудника")
    position = models.CharField(max_length=100, verbose_name="Должность сотрудника")
    image = models.ImageField(
        upload_to="laboratories_employees_images",
        verbose_name="Фото сотрудника",
        blank=True,
        null=True
    )

    laboratory: Laboratory = models.ForeignKey(
        to=Laboratory,
        on_delete=models.CASCADE,
        verbose_name="Лаборатория",
        related_name="employees"
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class SocialNetResource(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    url = models.URLField(max_length=512, verbose_name="Ссылка")

    laboratory: Laboratory = models.ForeignKey(
        to=Laboratory,
        on_delete=models.CASCADE,
        verbose_name="Лаборатория",
        related_name="social_nets"
    )

    def __str__(self) -> str:
        return f"{self.laboratory.title} : {self.title}"

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"


class LaboratorySolutionCards(models.Model):
    laboratory: Laboratory = models.ForeignKey(
        to=Laboratory,
        on_delete=models.CASCADE,
        verbose_name="Лаборатория",
        related_name="solution_cards"
    )
    solution: SolutionCard = models.ForeignKey(
        to=SolutionCard,
        on_delete=models.CASCADE,
        verbose_name="Карточка разработки",
        related_name="laboratories"
    )

    class Meta:
        verbose_name = "Карточка разработки"
        verbose_name_plural = "Карточки разработок"
