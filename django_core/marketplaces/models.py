import datetime
import re

from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from constance import config
from django.conf import settings
from django.db import models
from django.utils.html import format_html
from django_lifecycle import AFTER_CREATE, hook, LifecycleModel, BEFORE_CREATE, AFTER_UPDATE
from transliterate import translit
from tinymce.models import HTMLField

from django_core.settings import env
from marketplaces.choices import LicenseType, SolutionSourceLocationType
from marketplaces.tasks import handle_form
from tags.models import Tag, Unit, Technology


class Field(models.Model):
    title = models.CharField(max_length=255)


class FormTemplate(models.Model):
    title = models.CharField(max_length=255, unique=True)
    fields = models.ManyToManyField(Field)


class Notification(LifecycleModel):
    message = models.JSONField()
    form = models.ForeignKey(FormTemplate, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @hook(AFTER_CREATE)
    def send_email(self) -> None:
        email_subject = 'Marketplace order'
        from_email = settings.EMAIL_HOST_USER
        recipients = [config.MARKETPLACE_ORDER]
        handle_form.delay(self.message, email_subject, from_email, recipients)


class Solution(LifecycleModel):
    title = models.CharField(max_length=1023, verbose_name="Название")
    description = HTMLField(verbose_name="Описание")
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name="Подразделение", null=True)
    laboratory = models.CharField(max_length=255, verbose_name="Лаборатория", default="", blank=True)
    supervisor = models.CharField(max_length=128, verbose_name="Руководитель", default="")
    supervisor_contacts = models.CharField(max_length=128, verbose_name="Контакты руководителя", null=True, blank=True)

    header_image = models.ImageField(
        blank=True,
        null=True,
        upload_to="solutions_background_images",
        verbose_name="Картинка для шапки 1600x750",
    )
    header_color = ColorField(
        blank=True,
        null=True,
        verbose_name="Цвет кружка с категорией",
    )
    button_title = models.CharField(max_length=128, verbose_name="Надпись на кнопке", blank=True, null=True)
    button_url = models.URLField(max_length=512, verbose_name="Ссылка, куда ведет кнопка", blank=True, null=True)
    button_description = models.CharField(max_length=512, verbose_name="Пояснение к кнопке", blank=True, null=True)

    published_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата публикации",
        help_text="Устанавливается автоматически при создании решения",
    )
    technology: models.Manager[Technology] = models.ManyToManyField(
        to=Technology, verbose_name="Технология"
    )

    license = models.CharField(
        max_length=32,
        choices=LicenseType.choices,
        default=LicenseType.NON_PUBLIC,
        verbose_name='Категория'
    )
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL", null=True, blank=True)

    def get_frontend_url(self) -> str:
        frontend_news_base_url = f'{"https" if env.bool("USE_HTTPS") else "http"}://{env.str("HOST")}/solutions/'
        if self.pk:
            slug = re.sub(
                r'[^a-zA-Z0-9-_]+',  # оставляем все [a-zA-Z0-9-_] символы
                '',
                translit((self.slug or self.title), "ru", reversed=True)  # транслит заголовка
                .replace(" ", "-").lower()  # меняем пробелы на тире
            )
            frontend_url = frontend_news_base_url + slug
            return format_html(f"<a href='{frontend_url}'>{frontend_url}</a>")
        return ""

    get_frontend_url.short_description = "Ссылка на разработку на сайте"
    url = property(get_frontend_url)

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

    @hook(BEFORE_CREATE)
    def published_default_time(self):
        if not self.published_at:
            self.published_at = datetime.datetime.now()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Страница разработки"
        verbose_name_plural = "Страницы разработок"
        ordering = ["-published_at"]


class SolutionResourceButton(models.Model):
    image = models.ImageField(
        upload_to="solutions_resources_images",
        verbose_name="Обложка кнопки 40х40",
    )
    url = models.URLField(max_length=512, verbose_name="Ссылка, куда ведет кнопка")
    description = models.CharField(max_length=512, verbose_name="Пояснение к кнопке", blank=True, null=True)
    solution: Solution = models.ForeignKey(
        to=Solution, on_delete=models.CASCADE, verbose_name="Решение", related_name="resource_button"

    )

    class Meta:
        verbose_name = "Документы/ссылки"
        verbose_name_plural = "Документы/ссылки"


class DataSource(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    url = models.URLField(max_length=512, verbose_name="Ссылка", blank=True, default="")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Материалы"
        verbose_name_plural = "Материалы"


class DataSourceBlock(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название блока")
    location = models.CharField(
        max_length=6,
        choices=SolutionSourceLocationType.choices,
        default=SolutionSourceLocationType.LEFT,
        verbose_name='Расположение блока'
    )
    data_sources: DataSource = models.ManyToManyField(
        to=DataSource,
        verbose_name="Материалы",
        related_name="data_source_block",
    )
    solution: Solution = models.ForeignKey(
        to=Solution,
        verbose_name="Решение",
        related_name="data_source_block",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Материалы"
        verbose_name_plural = "Материалы"


class SolutionCard(models.Model):
    title = models.CharField(max_length=1023, verbose_name="Название")
    description = RichTextField(verbose_name="Описание")
    license = models.CharField(
        max_length=32,
        choices=LicenseType.choices,
        default=LicenseType.NON_PUBLIC,
        verbose_name='Категория'
    )
    technology: models.Manager[Technology] = models.ManyToManyField(
        to=Technology,
        verbose_name="Технология"
    )
    image = models.ImageField(
        upload_to="solution_card_background_images",
        verbose_name="Обложка (785x478)",
        blank=True,
        null=True,
    )
    color = ColorField(
        verbose_name="Колорчекер",
    )
    order = models.PositiveSmallIntegerField(verbose_name="Порядок отображения")
    is_hidden = models.BooleanField(verbose_name="Не отображать на главной витрине решений", default=False)
    # slug = models.SlugField(max_length=255, unique=True, verbose_name="URL", null=True, blank=True)
    url = models.URLField(verbose_name="Ссылка, куда ведет нажатие на карточку", blank=True, default="")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Карточка разработки"
        verbose_name_plural = "Карточки разработки"
