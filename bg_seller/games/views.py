from django.shortcuts import render

from rest_framework import viewsets
from games.models import Game, Author, GameCategory
from games.serializers import GameSerializer, AuthorSerializer, GameCategorySerializer

class GameViewSet(viewsets.ModelViewSet):
	queryset = Game.objects.all()
	serializer_class = GameSerializer

class AuthorViewSet(viewsets.ModelViewSet):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer

class GameCategoryViewSet(viewsets.ModelViewSet):
	queryset = GameCategory.objects.all()
	serializer_class = GameCategorySerializer

