from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import FoodRecipes
from comments.models import Comments
from comments.serializers import CommentSerializer

class FoodRecipesSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()
    categoryCD = serializers.ReadOnlyField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = FoodRecipes
        fields = ['id', 'author', 'user', 'profile', 'title', 'thumnail', 'categoryCD', 'intro', 'time', 'video',
                 'people_num', 'difficulty', 'created_at', 'updated_at', 'comments']

    def get_author(self, data):
        return data.user.nickname
    
    def get_profile(self, data):
        return data.user.profile_img.url
    
    def get_comments(self, data):
        comment = Comments.objects.filter(recipe=data.id)
        serializer = CommentSerializer(comment, many=True)
        return serializer.data

class ConvenienceRecipesSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()
    categoryCD = serializers.ReadOnlyField()

    class Meta:
        model = FoodRecipes
        fields = ['id', 'author', 'user', 'profile', 'title', 'thumnail', 'categoryCD', 'tot_price', 'intro', 'time', 'video',
                'difficulty', 'created_at', 'updated_at']

    def get_author(self, data):
        return data.user.nickname
    
    def get_profile(self, data):
        return data.user.profile_img.url
    
    def get_comments(self, data):
        comment = Comments.objects.filter(recipe=data.id)
        serializer = CommentSerializer(comment, many=True)
        return serializer.data

