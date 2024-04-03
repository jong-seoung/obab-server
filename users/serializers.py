from rest_framework import serializers 

from accounts.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_login', 'created_at', 'updated_at', 'email', 'name', 'nickname', 'profile_img', 'self_info']