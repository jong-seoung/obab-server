from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializer import FoodRecipesSerializer
from .models import FoodRecipes
from .permissions import IsOwnerOrReadOnly
from accounts.functions import get_user_id

class FoodRecipesListCreateAPIView(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser,)
    queryset = FoodRecipes.objects.all()
    serializer_class = FoodRecipesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=get_user_id(self.request))

class FoodRecipesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodRecipes.objects.all()
    serializer_class = FoodRecipesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]