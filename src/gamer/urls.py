from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_view, name='game'),  # Указываем путь к нашей views-функции
]
