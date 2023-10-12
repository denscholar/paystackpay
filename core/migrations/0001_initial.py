# Generated by Django 4.2.6 on 2023-10-12 09:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                ("amount", models.PositiveIntegerField()),
                ("ref", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("verified", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ("-created",),
            },
        ),
    ]
