# Generated by Django 4.1 on 2022-10-11 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplaces', '0002_notification_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formtemplate',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
