# Generated by Django 5.0.3 on 2024-03-17 23:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CookingMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_name', models.CharField(max_length=50)),
                ('kor_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fullness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_name', models.CharField(max_length=50)),
                ('kor_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MeatType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_name', models.CharField(max_length=50)),
                ('kor_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Spicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_name', models.CharField(max_length=50)),
                ('kor_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_name', models.CharField(max_length=50)),
                ('kor_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_name', models.CharField(max_length=50)),
                ('kor_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MenuList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cooking_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.cookingmethod')),
                ('fullness', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.fullness')),
                ('meat_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.meattype')),
                ('spicy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.spicy')),
                ('temperature', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.temperature')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.type')),
            ],
        ),
    ]
