from django.db import models


class FoodRecipes(models.Model):
    title = models.CharField(max_length=300)