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
### end subViewSets ###