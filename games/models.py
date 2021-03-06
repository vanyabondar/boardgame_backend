from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Author(models.Model):
	author_name = models.CharField(max_length=100)
	author_description = models.TextField()


class GameCategory(models.Model):
	game_category_name = models.CharField(max_length=100)
	game_category_description = models.TextField()


class Game(models.Model):
	game_name = models.CharField(max_length=100)
	cost = models.DecimalField(max_digits=8, decimal_places=2)
	quantity = models.IntegerField()
	game_description = models.TextField()
	released_year = models.IntegerField()
	playing_time = models.IntegerField()
	min_age = models.IntegerField()
	authors = models.ManyToManyField(
		Author,
		blank=True,
		related_name='games')
	game_category = models.ManyToManyField(
		GameCategory,
		blank=True,
		related_name='games')


class OrderItem(models.Model):
	order = models.ForeignKey(
		'games.Order',
		on_delete=models.CASCADE,
		related_name='order_items')
	game = models.ForeignKey(
		'games.Game',
		on_delete=models.CASCADE)
	quantity = models.IntegerField()
	

class Order(models.Model):
	customer = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		related_name='orders',
		on_delete=models.DO_NOTHING)  # to save information for accounting
	games = models.ManyToManyField(
		Game,
		related_name='orders',
		through=OrderItem)
	time = models.DateTimeField(auto_now_add=True)
	comment = models.TextField(null=True)
