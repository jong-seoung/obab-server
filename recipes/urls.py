from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .viewsets import *

router = DefaultRouter()
router.register(r'food-recipes', FoodRecipesViewSet, basename='food-recipes') 
router.register(r'convenience-recipes', ConvenienceRecipesViewSet, basename='convenience-recipes') 
router.register(r'broadcast-recipes', BroadcastRecipesViewSet, basename='broadcast-recipes') 
router.register(r'seasoning_recipes', SeasoningRecipesViewSet, basename='seasoning_recipe') 

# 라우터 URL을 urlpatterns에 추가
urlpatterns = [
    path('', include(router.urls)),
]