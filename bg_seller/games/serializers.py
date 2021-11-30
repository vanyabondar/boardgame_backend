from rest_framework import serializers
from games.models import Game, Author, GameCategory

class GameSerializer(serializers.ModelSerializer):

	game_category = serializers.SlugRelatedField(slug_field="game_category_name", read_only=True, many=True)
	authors = serializers.SlugRelatedField(slug_field="author_name", read_only=True, many=True)

	class Meta:
		model = Game
		fields = '__all__'


class GameNameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Game
		fields = ("game_name",)


class AuthorSerializer(serializers.ModelSerializer):

	# games = GameNameSerializer(many=True)
	games = serializers.SlugRelatedField(slug_field="game_name", read_only=True, many=True)

	class Meta:
		model = Author
		fields = "__all__"

class GameCategorySerializer(serializers.ModelSerializer):

	# games = GameNameSerializer(many=True)
	games = serializers.SlugRelatedField(slug_field="game_name", read_only=True, many=True)

	class Meta:
		model = GameCategory
		fields = "__all__"

