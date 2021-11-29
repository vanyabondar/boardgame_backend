from django.db import models


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
		'games.Author',
		blank=True,
		related_name="games",
		)
	game_category = models.ManyToManyField(
		'games.GameCategory',
		blank=True,
		related_name="games",
		)
