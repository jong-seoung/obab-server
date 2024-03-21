from core.serializers import BaseRecipeSerializer
from recipes.models import FoodRecipes

class FoodRecipesSerializer(BaseRecipeSerializer):
    class Meta:
        model = FoodRecipes
        fields = ['id', 'user', 'profile', 'title', 'thumnail', 'categoryCD', 'intro', 'time', 'video',
                 'people_num', 'difficulty', 'created_at', 'updated_at', 'comments']


class ConvenienceRecipesSerializer(BaseRecipeSerializer):
    class Meta:
        model = FoodRecipes
        fields = ['id', 'user', 'profile', 'title', 'thumnail', 'categoryCD', 'tot_price', 'intro', 'time', 'video',
                'difficulty', 'created_at', 'updated_at']
