from rest_framework import serializers
from games.models import Game, Author, GameCategory


class GameGeneralSerializer(serializers.ModelSerializer):

	class Meta:
		model = Game
		fields = ('id', 'game_name')


class GameCategoryGeneralSerializer(serializers.ModelSerializer):

	class Meta:
		model = GameCategory
		exclude = ('game_category_description',)	


class AuthorGeneralSerializer(serializers.ModelSerializer):

	class Meta:
		model = Author
		exclude = ('author_description',)

class GameSerializer(serializers.ModelSerializer):

	# game_category = serializers.SlugRelatedField(slug_field="game_category_name", read_only=True, many=True)
	# authors = serializers.SlugRelatedField(slug_field="author_name", read_only=True, many=True)
	game_category = GameCategoryGeneralSerializer(many=True, read_only=True)
	authors = AuthorGeneralSerializer(many=True, read_only=True)
	
	class Meta:
		model = Game
		fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):

	# games = serializers.SlugRelatedField(slug_field="game_name", read_only=True, many=True)
	games = GameGeneralSerializer(many=True, read_only=True)

	class Meta:
		model = Author
		fields = "__all__"


class GameCategorySerializer(serializers.ModelSerializer):

	# games = serializers.SlugRelatedField(slug_field="game_name", read_only=True, many=True)
	games = GameGeneralSerializer(many=True, read_only=True)

	class Meta:
		model = GameCategory
		fields = '__all__'




