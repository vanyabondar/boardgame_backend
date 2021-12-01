# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as filters_rest
from django_filters import rest_framework as filters_dj
from django.shortcuts import render
from rest_framework import viewsets
from games.models import Game, Author, GameCategory, Order
from games.serializers import GameSerializer, AuthorSerializer, GameCategorySerializer, OrderSerializer
from rest_framework import permissions
from bg_seller.permissions import IsAdminOrReadOnly


class GameViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAdminOrReadOnly]
	queryset = Game.objects.all()
	serializer_class = GameSerializer
	filter_backends = [filters_rest.SearchFilter, filters_dj.DjangoFilterBackend, filters_rest.OrderingFilter]
	filter_fields = ['game_category', 'authors',]
	search_fields = ['game_name',]
	ordering_fields = ["cost", "playing_time", "relised_year"]
	

class AuthorViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAdminOrReadOnly]
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer


class GameCategoryViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAdminOrReadOnly]
	queryset = GameCategory.objects.all()
	serializer_class = GameCategorySerializer
	pagination_class = None

class OrderViewSet(viewsets.ModelViewSet):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = OrderSerializer
	# To filter orders by user
	def get_queryset(self):
		return Order.objects.filter(customer=self.request.user)

