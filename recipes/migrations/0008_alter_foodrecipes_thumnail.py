# Generated by Django 5.0.3 on 2024-03-19 16:42

import core.functions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_foodrecipes_content_alter_foodrecipes_thumnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodrecipes',
            name='thumnail',
            field=models.ImageField(blank=True, null=True, upload_to=core.functions.upload_user_directory),
        ),
    ]
