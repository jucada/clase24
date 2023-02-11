# Generated by Django 4.1.5 on 2023-01-25 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profesor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=40)),
                ("apellido", models.CharField(max_length=40)),
                ("email", models.EmailField(max_length=254)),
                ("profesion", models.CharField(max_length=35)),
            ],
        ),
    ]
