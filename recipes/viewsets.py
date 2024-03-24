from rest_framework import status
from rest_framework.response import Response

from .serializer import FoodRecipesSerializer, ConvenienceRecipesSerializer, IngredientsSerializer, ConvenienceItemsSerializer
from .models import FoodRecipes, Ingredients, RecipeProcess, ConvenienceItems
from core.viewsets import BaseRecipesViewSet, BaseAbuotRecipesViewset
from core.serializers import RecipeProcessSerializer

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


### subViewSets ###
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
        serializer = self.get_serializer(data=request.data)
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