# Generated by Django 5.0.3 on 2024-03-15 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0002_recipeprocess"),
    ]

    operations = [
        migrations.CreateModel(
            name="ConvenienceItems",
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
                ("name", models.CharField(max_length=50)),
                ("price", models.IntegerField()),
                (
                    "foodrecipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipes.foodrecipes",
                    ),
                ),
            ],
        ),
    ]
