# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import render
from rest_framework import viewsets
from games.models import Game, Author, GameCategory
from games.serializers import GameSerializer, AuthorSerializer, GameCategorySerializer

class GameViewSet(viewsets.ModelViewSet):
	queryset = Game.objects.all()
	serializer_class = GameSerializer
	filter_backends = [filters.SearchFilter,]
	# filter_backends = [DjangoFilterBackend,]
	search_fields = ['game_name',]
	# filterset_fields = ['quantity',]

class AuthorViewSet(viewsets.ModelViewSet):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer

class GameCategoryViewSet(viewsets.ModelViewSet):
	queryset = GameCategory.objects.all()
	serializer_class = GameCategorySerializer

