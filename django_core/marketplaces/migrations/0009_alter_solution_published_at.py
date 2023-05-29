# Generated by Django 4.1 on 2022-10-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplaces', '0008_alter_solution_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='published_at',
            field=models.DateTimeField(blank=True, help_text='Устанавливается автоматически при создании решения', null=True, verbose_name='Дата публикации'),
        ),
    ]