# Generated by Django 4.1 on 2022-08-28 17:50

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0004_news_show_in_feed"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="background_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                help_text="Используется при отсутствии фонового изображения",
                image_field=None,
                max_length=18,
                null=True,
                samples=None,
                verbose_name="Цвет фона",
            ),
        ),
        migrations.AddField(
            model_name="news",
            name="background_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="news_background_images",
                verbose_name="Фоновое изображение",
            ),
        ),
    ]
