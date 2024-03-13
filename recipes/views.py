from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .serializer import FoodRecipesSerializer
from .models import FoodRecipes


class FoodRecipeList(APIView):
    def get(self, request):
        food_recipes = FoodRecipes.objects.all()

        serializer = FoodRecipesSerializer(food_recipes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FoodRecipesSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FoodRecipeDetail(APIView):
    def get_object(self, pk):
        try:
            return FoodRecipes.objects.get(pk=pk)
        except FoodRecipes.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        food_recipes = self.get_object(pk)
        serializer = FoodRecipesSerializer(food_recipes)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        food_recipes = self.get_object(pk)
        serializer = FoodRecipesSerializer(food_recipes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        food_recipes = self.get_object(pk)
        food_recipes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)