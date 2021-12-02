from rest_framework import filters as filters_rest
from rest_framework import permissions, viewsets
from django_filters import rest_framework as filters_dj
from django.shortcuts import render

from bg_seller.permissions import IsAdminOrReadOnly
from games.models import Game, Author, GameCategory, Order
from games.serializers import \
    GameSerializer, \
    AuthorSerializer, \
    GameCategorySerializer, \
    OrderSerializer


class GameViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = GameSerializer
    queryset = Game.objects.order_by('pk').all()
    
    filter_backends = [
        filters_rest.SearchFilter, 
        filters_dj.DjangoFilterBackend, 
        filters_rest.OrderingFilter]

    filter_fields = ['game_category', 'authors',]
    search_fields = ['game_name',]
    ordering_fields = ["cost", "playing_time", "released_year"]
    

class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class GameCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = GameCategorySerializer
    queryset = GameCategory.objects.all()
    
    pagination_class = None  # we don't have that mush game categories


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        # To filter orders by user
        return Order.objects.filter(customer=self.request.user)

