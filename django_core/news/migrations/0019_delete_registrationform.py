# Generated by Django 4.1 on 2022-10-22 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0018_registrationform_registration"),
    ]

    operations = [
        migrations.DeleteModel(
            name="RegistrationForm",
        ),
    ]
