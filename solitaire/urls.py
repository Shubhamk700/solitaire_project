from django.urls import path
from . import views

urlpatterns = [
    path('', views.solitaire_game, name='solitaire_game'),
]