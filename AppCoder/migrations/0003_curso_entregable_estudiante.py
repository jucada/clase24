# Generated by Django 4.1.5 on 2023-01-25 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppCoder", "0002_profesor_edad"),
    ]

    operations = [
        migrations.CreateModel(
            name="Curso",
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
                ("camada", models.IntegerField()),
                ("comision", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Entregable",
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
                ("fecha", models.DateField()),
                ("entregado", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Estudiante",
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
            ],
        ),
    ]
