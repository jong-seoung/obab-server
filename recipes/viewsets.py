from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializer import FoodRecipesSerializer, ConvenienceRecipesSerializer, IngredientsSerializer, RecipeProcessSerializer
from core.viewsets import BaseRecipesViewSet
from .models import FoodRecipes, Ingredients, RecipeProcess


# FoodRecipes
class FoodRecipesViewSet(BaseRecipesViewSet):
    queryset = FoodRecipes.objects.filter(categoryCD='food_recipe')
    serializer_class = FoodRecipesSerializer

# BroadcastRecipes
class BroadcastRecipesViewSet(BaseRecipesViewSet):
    queryset = FoodRecipes.objects.filter(categoryCD='broadcast_recipe')
    serializer_class = FoodRecipesSerializer

# seasoning_recipe
class SeasoningRecipesViewSet(BaseRecipesViewSet):
    queryset = FoodRecipes.objects.filter(categoryCD='seasoning_recipe')
    serializer_class = FoodRecipesSerializer

# ConvenienceRecipes
class ConvenienceRecipesViewSet(BaseRecipesViewSet):
    queryset = FoodRecipes.objects.filter(categoryCD='convenience_store_combination')
    serializer_class = ConvenienceRecipesSerializer


class IngredientsViewset(CreateModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer

class RecipeProcessViewset(CreateModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = RecipeProcess.objects.all()
    serializer_class = RecipeProcessSerializer
