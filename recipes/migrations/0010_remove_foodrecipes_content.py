# Generated by Django 5.0.3 on 2024-03-20 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_rename_author_foodrecipes_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodrecipes',
            name='content',
        ),
    ]