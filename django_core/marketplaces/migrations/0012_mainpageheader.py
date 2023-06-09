# Generated by Django 4.1 on 2022-11-20 22:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("marketplaces", "0011_datasource_alter_solution_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="MainPageHeader",
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
                    "header_text",
                    ckeditor.fields.RichTextField(
                        verbose_name="Текст в шапке страницы solutions"
                    ),
                ),
            ],
            options={
                "verbose_name": "Шапка страницы solutions",
                "verbose_name_plural": "Шапка страницы solutions",
            },
        ),
    ]
