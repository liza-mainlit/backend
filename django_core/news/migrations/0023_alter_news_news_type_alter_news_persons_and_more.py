# Generated by Django 4.1 on 2022-11-20 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tags", "0004_technology"),
        ("news", "0022_alter_news_news_type_alter_news_persons_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="news_type",
            field=models.ManyToManyField(to="tags.newstype", verbose_name="Рубрика"),
        ),
        migrations.AlterField(
            model_name="news",
            name="persons",
            field=models.ManyToManyField(to="tags.person", verbose_name="Персоны"),
        ),
        migrations.AlterField(
            model_name="news",
            name="tags",
            field=models.ManyToManyField(to="tags.tag", verbose_name="Тематика"),
        ),
        migrations.AlterField(
            model_name="news",
            name="units",
            field=models.ManyToManyField(to="tags.unit", verbose_name="Подразделения"),
        ),
    ]
