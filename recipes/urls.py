from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FoodRecipeList, FoodRecipeDetail

urlpatterns = [
    path('foodrecipe/',FoodRecipeList.as_view()),
    path('foodrecipe/<int:pk>/',FoodRecipeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)