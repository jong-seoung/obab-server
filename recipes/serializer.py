from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import FoodRecipes

class FoodRecipesSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()

    class Meta:
        model = FoodRecipes
        fields = ['id', 'author', 'user', 'profile', 'title', 'thumnail', 'content', 'categoryCD', 'tot_price', 'intro', 'time', 'video',
                 'people_num', 'difficulty', 'created_at', 'updated_at']

    def get_author(self, data):
        return data.user.nickname
    
    def get_profile(self, data):
        return data.user.profile_img.url
