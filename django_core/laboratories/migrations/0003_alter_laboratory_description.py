# Generated by Django 4.1 on 2023-04-17 14:02

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratories', '0002_alter_laboratorysolutioncards_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratory',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Описание'),
        ),
    ]