from rest_framework.parsers import MultiPartParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

from recipes.permissions import IsOwnerOrReadOnly
from accounts.functions import get_user_id

class BaseRecipesViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=get_user_id(self.request))