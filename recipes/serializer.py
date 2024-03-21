from rest_framework import serializers

from core.serializers import BaseRecipeSerializer
from recipes.models import FoodRecipes, Ingredients, RecipeProcess, ConvenienceItems


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'

class RecipeProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeProcess
        fields = '__all__'

class ConvenienceItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConvenienceItems
        fields = '__all__'

class FoodRecipesSerializer(BaseRecipeSerializer):
    ingredients = serializers.SerializerMethodField()
    recipeprocess = serializers.SerializerMethodField()

    class Meta:
        model = FoodRecipes
        fields = ['id', 'user', 'profile', 'title', 'thumnail', 'categoryCD', 'intro', 'time', 'video',
                 'people_num', 'difficulty', 'created_at', 'updated_at', 'ingredients', 'recipeprocess', 'comments']

    def get_ingredients(self, data):
        ingredient = Ingredients.objects.filter(foodrecipe=data.id)
        serializer = IngredientsSerializer(ingredient, many=True)
        return serializer.data
    
    def get_recipeprocess(self, data):
        recipeprocess = RecipeProcess.objects.filter(foodrecipe=data.id)
        serializer = RecipeProcessSerializer(recipeprocess, many=True)
        return serializer.data
    
class ConvenienceRecipesSerializer(BaseRecipeSerializer):
    class Meta:
        model = FoodRecipes
        fields = ['id', 'user', 'profile', 'title', 'thumnail', 'categoryCD', 'tot_price', 'intro', 'time', 'video',
                'difficulty', 'created_at', 'updated_at']