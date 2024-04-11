from rest_framework import status
from rest_framework.response import Response

from .serializer import FoodRecipesSerializer, ConvenienceRecipesSerializer, IngredientsSerializer, ConvenienceItemsSerializer, RecipeImageSerializer
from .models import FoodRecipes, Ingredients, RecipeProcess, ConvenienceItems, RecipeImage
from core.viewsets import BaseRecipesViewSet, BaseAbuotRecipesViewset, RecipeImageViewset
from core.serializers import RecipeProcessSerializer

# FoodRecipes
class FoodRecipesViewSet(BaseRecipesViewSet):
    categoryCD='food_recipe'
    queryset = FoodRecipes.objects.filter(categoryCD=categoryCD)
    serializer_class = FoodRecipesSerializer
    
    def perform_create(self, serializer):
        serializer.save(categoryCD=self.categoryCD)
        return super().perform_create(serializer)
    
# BroadcastRecipes
class BroadcastRecipesViewSet(BaseRecipesViewSet):
    categoryCD='broadcast_recipe'
    queryset = FoodRecipes.objects.filter(categoryCD=categoryCD)
    serializer_class = FoodRecipesSerializer
    
    def perform_create(self, serializer):
        serializer.save(categoryCD=self.categoryCD)
        return super().perform_create(serializer)

# seasoning_recipe
class SeasoningRecipesViewSet(BaseRecipesViewSet):
    categoryCD='seasoning_recipe'
    queryset = FoodRecipes.objects.filter(categoryCD=categoryCD)
    serializer_class = FoodRecipesSerializer
    
    def perform_create(self, serializer):
        serializer.save(categoryCD=self.categoryCD)
        return super().perform_create(serializer)

# ConvenienceRecipes
class ConvenienceRecipesViewSet(BaseRecipesViewSet):
    categoryCD='convenience_store_combination'
    queryset = FoodRecipes.objects.filter(categoryCD=categoryCD)
    serializer_class = ConvenienceRecipesSerializer
    
    def perform_create(self, serializer):
        serializer.save(categoryCD=self.categoryCD)
        return super().perform_create(serializer)

### subViewSets ###
class RecipeImageViewset(RecipeImageViewset):
    queryset = RecipeImage.objects.all()
    serializer_class = RecipeImageSerializer

class IngredientsViewset(BaseAbuotRecipesViewset):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer

class RecipeProcessViewset(BaseAbuotRecipesViewset):
    queryset = RecipeProcess.objects.all()
    serializer_class = RecipeProcessSerializer

class ConvenienceItemsViewset(BaseAbuotRecipesViewset):
    queryset = ConvenienceItems.objects.all()
    serializer_class = ConvenienceItemsSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        price = instance.price
        foodrecipe = instance.foodrecipe
        tot_price = foodrecipe.tot_price - price

        foodrecipe.tot_price = tot_price
        foodrecipe.save()

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def create_response(self, serializer, instance):
        response = super().create_response(serializer, instance)
        price = serializer.data['price']
        instance.tot_price += price
        instance.save()
        return response
### end subViewSets ###