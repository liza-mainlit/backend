# Generated by Django 4.1 on 2022-08-31 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0008_rename_newscategory_newstag_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="published_at",
            field=models.DateTimeField(
                blank=True,
                help_text="Устанавливается автоматически при сохранении новости, которая не является черновиком",
                null=True,
                verbose_name="Дата публикации",
            ),
        ),
    ]