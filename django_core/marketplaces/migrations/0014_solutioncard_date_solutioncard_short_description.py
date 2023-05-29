# Generated by Django 4.1 on 2022-12-02 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("marketplaces", "0013_delete_mainpageheader"),
    ]

    operations = [
        migrations.AddField(
            model_name="solutioncard",
            name="date",
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name="solutioncard",
            name="short_description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Краткая информация"
            ),
        ),
    ]