# Generated by Django 4.1 on 2022-10-11 14:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplaces', '0004_solution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Описание'),
        ),
    ]