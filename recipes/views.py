from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from .serializer import FoodRecipesSerializer
from .models import FoodRecipes

class FoodRecipesListCreateAPIView(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser,)
    queryset = FoodRecipes.objects.all()
    serializer_class = FoodRecipesSerializer

class FoodRecipesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodRecipes.objects.all()
    serializer_class = FoodRecipesSerializer