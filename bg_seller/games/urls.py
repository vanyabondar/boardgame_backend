from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from games import views

router = routers.DefaultRouter()

router.register(r'games', views.GameViewSet)
router.register(r'game_categoies', views.GameCategoryViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'orders', views.OrderViewSet, basename='order')
