# Generated by Django 4.1 on 2022-12-03 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("marketplaces", "0015_remove_solutioncard_short_description_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="solutioncard",
            name="date",
        ),
    ]
