from rest_framework import serializers
from games.models import Game, Author, GameCategory

class GameSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Game
		fields = '__all__'

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Author
		fields = "__all__"

class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = GameCategory
		fields = "__all__"