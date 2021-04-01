from django.urls import path, include
from django.contrib import admin
from .views import main, change, check, validate, leaderboard, result

urlpatterns = [
  path('', main),
  path('change/', change),
  path('check/<str:card>/', check),
  path('balance/<str:card>/', validate),
  path('result/', result),
  # path('player/', views.player_),
  # path('player/<str:id_card>/', views.player),
  path('leaderboard/<str:quest>/', leaderboard),
]
