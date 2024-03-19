from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import FoodRecipes

class FoodRecipesSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()

    class Meta:
        model = FoodRecipes
        fields = ['id', 'nickname', 'author', 'profile', 'title', 'thumnail', 'content', 'categoryCD', 'tot_price', 'intro', 'time', 'video',
                 'people_num', 'difficulty', 'created_at', 'updated_at']

    def get_nickname(self, data):
        return data.author.nickname
    
    def get_profile(self, data):
        print(data.author.profile_img.url)
        return data.author.profile_img.url
