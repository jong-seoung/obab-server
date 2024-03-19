from django.urls import path
from .views import *

urlpatterns = [
    path('recipes/', FoodRecipesListCreateAPIView.as_view(), name='foodrecipes-list'),
    path('recipes/<int:pk>/', FoodRecipesRetrieveUpdateDestroyAPIView.as_view(), name='foodrecipes-detail'),
]