from django.core.files.storage import default_storage

from rest_framework.parsers import MultiPartParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from recipes.permissions import IsOwnerOrReadOnly, UserPostAccessPermission
from accounts.functions import get_user_id
from recipes.models import FoodRecipes

class BaseRecipesViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=get_user_id(self.request))

class BaseAbuotRecipesViewset(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    parser_classes = (MultiPartParser,)
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserPostAccessPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_user_id(self.request)
        instance = serializer.validated_data['foodrecipe']
        post_id = instance.id
        post_user = FoodRecipes.objects.get(id=post_id).user

        if user != post_user:
            return Response({'error': '자격 인증 데이터가 잘못되었습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        return self.create_response(serializer, instance)

    def create_response(self, serializer, instance):
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class RecipeImageViewset(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    parser_classes = (MultiPartParser,)
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    def perform_create(self, serializer):
        serializer.save(state='임시저장')
    
    def perform_update(self, serializer):
        instance = self.get_object()
        default_storage.delete(instance.image.path)
        serializer.save(state='반영')

    def perform_destroy(self, instance):
        instance = self.get_object()
        default_storage.delete(instance.image.path)
        instance.delete()
        