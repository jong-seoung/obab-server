from rest_framework import serializers
from .models import FoodRecipes


class FoodRecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRecipes
        fields = ('id', 'title')