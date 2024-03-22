from rest_framework.parsers import MultiPartParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed
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

class BaseAbuotRecipesViewset(CreateModelMixin, UpdateModelMixin, GenericViewSet):
    parser_classes = (MultiPartParser,)
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserPostAccessPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_user_id(self.request)
        post_id = serializer.validated_data['foodrecipe'].id
        post_user = FoodRecipes.objects.get(id=post_id).user

        if user != post_user:
            return Response({'error': 'Custom validation failed.'}, status=status.HTTP_400_BAD_REQUEST)
            
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
