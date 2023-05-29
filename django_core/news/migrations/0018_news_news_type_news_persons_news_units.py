# Generated by Django 4.1 on 2022-10-22 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_person_unit_delete_newstype_newstype'),
        ('news', '0017_alter_news_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_type',
            field=models.ManyToManyField(to='tags.newstype', verbose_name='Рубрика'),
        ),
        migrations.AddField(
            model_name='news',
            name='persons',
            field=models.ManyToManyField(to='tags.person', verbose_name='Персоны'),
        ),
        migrations.AddField(
            model_name='news',
            name='units',
            field=models.ManyToManyField(to='tags.unit', verbose_name='Подразделения'),
        ),
    ]
