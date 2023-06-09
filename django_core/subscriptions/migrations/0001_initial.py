# Generated by Django 4.1 on 2022-08-28 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Subscription",
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
                    "email",
                    models.EmailField(
                        max_length=254, verbose_name="Адрес электронной почты"
                    ),
                ),
            ],
            options={
                "verbose_name": "Подписка на рассылку",
                "verbose_name_plural": "Подписки на рассылку",
            },
        ),
    ]
