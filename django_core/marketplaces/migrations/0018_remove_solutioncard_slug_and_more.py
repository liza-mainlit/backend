# Generated by Django 4.1 on 2023-04-05 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("marketplaces", "0017_solutioncard_solution"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="solutioncard",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="solutioncard",
            name="solution",
        ),
        migrations.AddField(
            model_name="solutioncard",
            name="is_hidden",
            field=models.BooleanField(
                default=False, verbose_name="Не отображать на главной витрине решений"
            ),
        ),
        migrations.AddField(
            model_name="solutioncard",
            name="url",
            field=models.URLField(
                blank=True,
                default="",
                verbose_name="Ссылка, куда ведет нажатие на карточку",
            ),
        ),
        migrations.AlterField(
            model_name="datasource",
            name="url",
            field=models.URLField(
                blank=True, default="", max_length=512, verbose_name="Ссылка"
            ),
        ),
        migrations.AlterField(
            model_name="solution",
            name="laboratory",
            field=models.CharField(
                blank=True, default="", max_length=255, verbose_name="Лаборатория"
            ),
        ),
    ]