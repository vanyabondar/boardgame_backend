from rest_framework import serializers
from games.models import Game, Author, GameCategory, Order, OrderItem


# class GameGeneralSerializer(serializers.ModelSerializer):

# 	class Meta:
# 		model = Game
# 		fields = ('id', 'game_name')


# class GameCategoryGeneralSerializer(serializers.ModelSerializer):

# 	class Meta:
# 		model = GameCategory
# 		exclude = ('game_category_description',)	


# class AuthorGeneralSerializer(serializers.ModelSerializer):

# 	class Meta:
# 		model = Author
# 		exclude = ('author_description',)


class GameSerializer(serializers.ModelSerializer):

	# game_category = serializers.SlugRelatedField(slug_field="game_category_name", read_only=True, many=True)
	# authors = serializers.SlugRelatedField(slug_field="author_name", read_only=True, many=True)
	game_category = serializers.PrimaryKeyRelatedField(many=True, queryset=GameCategory.objects.all())
	authors = serializers.PrimaryKeyRelatedField(many=True,  queryset=Author.objects.all())
	# game_category = GameCategoryGeneralSerializer(many=True, read_only=True)
	# authors = AuthorGeneralSerializer(many=True, read_only=True)
	class Meta:
		model = Game
		fields = '__all__'
	

class AuthorSerializer(serializers.ModelSerializer):

	# games = serializers.SlugRelatedField(slug_field="game_name", read_only=True, many=True)
	# games = GameGeneralSerializer(many=True, read_only=True)
	games = serializers.PrimaryKeyRelatedField(many=True, queryset=Game.objects.all())
	class Meta:
		model = Author
		fields = "__all__"


class GameCategorySerializer(serializers.ModelSerializer):

	# games = serializers.SlugRelatedField(slug_field="game_name", read_only=True, many=True)
	# games = GameGeneralSerializer(many=True, read_only=True)
	games = serializers.PrimaryKeyRelatedField(many=True, queryset=Game.objects.all())

	class Meta:
		model = GameCategory
		fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderItem
		fields = ('game', 'quantity')

class OrderSerializer(serializers.ModelSerializer):
	order_items = OrderItemSerializer(many=True) 

	class Meta:
		model = Order
		exclude = ('games',)

	def create(self, validated_data):
		items = validated_data.pop('order_items')
		order = Order.objects.create(**validated_data)
		for item in items:
			d = dict(item)
			OrderItem.objects.create(order=order, game=d['game'], quantity=d['quantity'])
		return order

	def update(self, instance, validated_data):
		items = validated_data.pop('order_items')
		for item in validated_data:
			if Order._meta.get_field(item):
				setattr(instance, item, validated_data[item])
		OrderItem.objects.filter(order=instance).delete()
		for item in items:
			d = dict(item)
			OrderItem.objects.create(order=instance, game=d['game'], quantity=d['quantity'])
		instance.save()
		return instance