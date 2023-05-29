# Generated by Django 4.1 on 2022-11-20 20:11

import ckeditor.fields
import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tags", "0004_technology"),
        ("marketplaces", "0010_alter_solution_license_alter_solution_solution_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="DataSource",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("url", models.URLField(max_length=512, verbose_name="Ссылка")),
            ],
            options={
                "verbose_name": "Материалы",
                "verbose_name_plural": "Материалы",
            },
        ),
        migrations.AlterModelOptions(
            name="solution",
            options={
                "ordering": ["-published_at"],
                "verbose_name": "Страница разработки",
                "verbose_name_plural": "Страницы разработок",
            },
        ),
        migrations.RemoveField(
            model_name="solution",
            name="background_color",
        ),
        migrations.RemoveField(
            model_name="solution",
            name="background_image",
        ),
        migrations.RemoveField(
            model_name="solution",
            name="is_deleted",
        ),
        migrations.RemoveField(
            model_name="solution",
            name="is_draft",
        ),
        migrations.RemoveField(
            model_name="solution",
            name="solution_type",
        ),
        migrations.RemoveField(
            model_name="solution",
            name="tags",
        ),
        migrations.AddField(
            model_name="solution",
            name="button_description",
            field=models.CharField(
                blank=True, max_length=512, null=True, verbose_name="Пояснение к кнопке"
            ),
        ),
        migrations.AddField(
            model_name="solution",
            name="button_title",
            field=models.CharField(
                blank=True, max_length=128, null=True, verbose_name="Надпись на кнопке"
            ),
        ),
        migrations.AddField(
            model_name="solution",
            name="button_url",
            field=models.URLField(
                blank=True,
                max_length=512,
                null=True,
                verbose_name="Ссылка, куда ведет кнопка",
            ),
        ),
        migrations.AddField(
            model_name="solution",
            name="header_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=18,
                null=True,
                samples=None,
                verbose_name="Цвет кружка с категорией",
            ),
        ),
        migrations.AddField(
            model_name="solution",
            name="header_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="solutions_background_images",
                verbose_name="Картинка для шапки 1600x750",
            ),
        ),
        migrations.AddField(
            model_name="solution",
            name="laboratory",
            field=models.CharField(
                default="", max_length=255, verbose_name="Лаборатория"
            ),
        ),
        migrations.AddField(
            model_name="solution",
            name="slug",
            field=models.SlugField(
                blank=True, max_length=255, null=True, unique=True, verbose_name="URL"
            ),
        ),
        migrations.AddField(
            model_name="solution",
            name="supervisor",
            field=models.CharField(
                default="", max_length=128, verbose_name="Руководитель"
            ),
        ),
        migrations.AddField(
            model_name="solution",
            name="supervisor_contacts",
            field=models.CharField(
                blank=True,
                max_length=128,
                null=True,
                verbose_name="Контакты руководителя",
            ),
        ),
        migrations.AddField(
            model_name="solution",
            name="technology",
            field=models.ManyToManyField(
                to="tags.technology", verbose_name="Технология"
            ),
        ),
        migrations.AddField(
            model_name="solution",
            name="unit",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="tags.unit",
                verbose_name="Подразделение",
            ),
        ),
        migrations.AlterField(
            model_name="solution",
            name="license",
            field=models.CharField(
                choices=[
                    ("Open source", "Open source"),
                    ("Non-public license", "Non-public license"),
                ],
                default="Non-public license",
                max_length=32,
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="solution",
            name="title",
            field=models.CharField(max_length=1023, verbose_name="Название"),
        ),
        migrations.CreateModel(
            name="SolutionResourceButton",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="solutions_resources_images",
                        verbose_name="Обложка кнопки 40х40",
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        max_length=512, verbose_name="Ссылка, куда ведет кнопка"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        max_length=512,
                        null=True,
                        verbose_name="Пояснение к кнопке",
                    ),
                ),
                (
                    "solution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resource_button",
                        to="marketplaces.solution",
                        verbose_name="Решение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Документы/ссылки",
                "verbose_name_plural": "Документы/ссылки",
            },
        ),
        migrations.CreateModel(
            name="SolutionCard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=1023, verbose_name="Название")),
                ("description", ckeditor.fields.RichTextField(verbose_name="Описание")),
                (
                    "license",
                    models.CharField(
                        choices=[
                            ("Open source", "Open source"),
                            ("Non-public license", "Non-public license"),
                        ],
                        default="Non-public license",
                        max_length=32,
                        verbose_name="Категория",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        null=True,
                        upload_to="solution_card_background_images",
                        verbose_name="Обложка (785x478)",
                    ),
                ),
                (
                    "color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF",
                        image_field=None,
                        max_length=18,
                        samples=None,
                        verbose_name="Колорчекер",
                    ),
                ),
                (
                    "order",
                    models.PositiveSmallIntegerField(
                        verbose_name="Порядок отображения"
                    ),
                ),
                (
                    "solution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="solution_card",
                        to="marketplaces.solution",
                        verbose_name="Разработка",
                    ),
                ),
                (
                    "technology",
                    models.ManyToManyField(
                        to="tags.technology", verbose_name="Технология"
                    ),
                ),
            ],
            options={
                "verbose_name": "Карточка разработки",
                "verbose_name_plural": "Карточки разработки",
            },
        ),
        migrations.CreateModel(
            name="DataSourceBlock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Название блока"),
                ),
                (
                    "location",
                    models.CharField(
                        choices=[("Right", "Right"), ("Left", "Left")],
                        default="Left",
                        max_length=6,
                        verbose_name="Расположение блока",
                    ),
                ),
                (
                    "data_sources",
                    models.ManyToManyField(
                        related_name="data_source_block",
                        to="marketplaces.datasource",
                        verbose_name="Материалы",
                    ),
                ),
                (
                    "solution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="data_source_block",
                        to="marketplaces.solution",
                        verbose_name="Решение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Материалы",
                "verbose_name_plural": "Материалы",
            },
        ),
    ]