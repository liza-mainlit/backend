import re

from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField
from transliterate import translit

from tags.models import Tag, NewsType, Person, Unit
from django_core.settings import env


class NewsSection(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Раздел новостей"
        verbose_name_plural = "Разделы новостей"


class News(models.Model):
    title = models.CharField(max_length=1023, verbose_name="Заголовок новости")

    short_description = models.TextField(verbose_name="Краткая информация")

    description = HTMLField(verbose_name="Общая информация")

    is_draft = models.BooleanField(default=False, verbose_name="Черновик?")

    show_in_feed = models.BooleanField(
        default=True,
        verbose_name="Отображать в ленте новостей",
        help_text="Влияет только на опубликованные новости",
    )

    video = models.FileField(
        blank=True, null=True, upload_to="news_videos", verbose_name="Видео"
    )

    video_link = models.TextField(
        blank=True, null=True, verbose_name="Ссылка на видео (YouTube)"
    )

    video_description = models.TextField(
        blank=True, null=True, verbose_name="Подпись к видео"
    )

    published_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата публикации",
        help_text=(
            "Устанавливается автоматически при сохранении новости,"
            " которая не является черновиком"
        ),
    )

    source = models.CharField(
        max_length=127, default="Редакция сайта", verbose_name="Источник новости"
    )

    tags: models.Manager[Tag] = models.ManyToManyField(
        to=Tag, verbose_name="Тематика", blank=True
    )

    news_type: models.Manager[NewsType] = models.ManyToManyField(
        to=NewsType, verbose_name="Рубрика", blank=True
    )

    persons: models.Manager[Person] = models.ManyToManyField(
        to=Person, verbose_name="Персоны", blank=True
    )

    units: models.Manager[Unit] = models.ManyToManyField(
        to=Unit, verbose_name="Подразделения", blank=True
    )

    background_image = models.ImageField(
        blank=True,
        null=True,
        upload_to="news_background_images",
        verbose_name="Фоновое изображение",
    )

    background_color = ColorField(
        blank=True,
        null=True,
        verbose_name="Цвет фона",
    )

    is_deleted = models.BooleanField(default=False, verbose_name="Удалено")

    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL", null=True, blank=True)

    placements: models.QuerySet

    def clean(self):
        slugged_text = self.slug if self.slug else self.title
        field = "slug" if self.slug else "title"
        self.slug = re.sub(
            r'[^a-zA-Z0-9-_]+',  # оставляем все [a-zA-Z0-9-_] символы
            '',
            translit(slugged_text, "ru", reversed=True)  # транслит заголовка
            .replace(" ", "-").lower()  # меняем пробелы на тире
        )
        if News.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            raise ValidationError(
                {f"{field}": [f'Please make {field} more unique because slug: "{self.slug}" already exists']})

    def get_frontend_url(self) -> str:
        frontend_news_base_url = f'{"https" if env.bool("USE_HTTPS") else "http"}://{env.str("HOST")}/publications/'
        if self.pk and not self.is_draft:
            frontend_url = frontend_news_base_url + str(self.slug)
            return format_html(f"<a href='{frontend_url}'>{frontend_url}</a>")
        return ""

    get_frontend_url.short_description = "Ссылка на новость на сайте"

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-published_at"]


class NewsPlacement(models.Model):
    section: NewsSection = models.ForeignKey(
        to=NewsSection, on_delete=models.CASCADE, verbose_name="Раздел"
    )

    order = models.PositiveSmallIntegerField(verbose_name="Порядок отображения")

    news: News = models.ForeignKey(
        to=News,
        on_delete=models.CASCADE,
        verbose_name="Новость",
        related_name="placements",
    )

    def __str__(self) -> str:
        return f"{self.news} в {self.section}"

    class Meta:
        verbose_name = "Размещение новости"
        verbose_name_plural = "Размещения новостей"


class NewsImage(models.Model):
    image = models.ImageField(upload_to="news_images/", verbose_name="Изображение")

    news: News = models.ForeignKey(
        to=News, on_delete=models.CASCADE, verbose_name="Новость", related_name="images"
    )

    def __str__(self) -> str:
        return self.image.name

    class Meta:
        verbose_name = "Изображение новости"
        verbose_name_plural = "Изображения новостей"


class Registration(models.Model):
    news: News = models.OneToOneField(
        to=News, on_delete=models.CASCADE, verbose_name="Mероприятие", related_name="registration"

    )
    title = models.CharField(
        blank=True, null=True, max_length=255, verbose_name="Название мероприятия"
    )
    start_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата и время начала"
    )
    ends_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата и время окончания"
    )
    place = models.CharField(
        blank=True, null=True, max_length=255, verbose_name="Место проведения"
    )
    contact_number = models.CharField(
        blank=True, null=True, max_length=255, verbose_name="Телефон организатора"
    )
    contact_email = models.EmailField(
        blank=True, null=True, max_length=255, verbose_name="Почта организатора"
    )
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to="registration_images",
        verbose_name="Изображение в форме регистрации",
    )

    color = ColorField(
        blank=True,
        null=True,
        verbose_name="Цвет",
    )

    consent = models.FileField(
        blank=True, null=True, upload_to="consent_on_data_processing", verbose_name="файл согласия на обработку данных"
    )

    class Meta:
        verbose_name = "Регистрация"
        verbose_name_plural = "Регистрация"
