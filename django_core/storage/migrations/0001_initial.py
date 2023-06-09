# Generated by Django 4.1 on 2022-10-22 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='storage/', verbose_name='Файл')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Файл в хранилище',
                'verbose_name_plural': 'Файлы в хранилище',
            },
        ),
    ]
