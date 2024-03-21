from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from comments.models import Comments
from comments.serializers import CommentSerializer

class BaseRecipeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    profile = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_profile(self, data):
        return data.user.profile_img.url
    
    def get_comments(self, data):
        comment = Comments.objects.filter(recipe=data.id)
        serializer = CommentSerializer(comment, many=True)
        return serializer.data