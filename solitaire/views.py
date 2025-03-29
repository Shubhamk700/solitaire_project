from django.shortcuts import render
from .utils import create_deck

def solitaire_game(request):
    deck = create_deck()
    context = {'deck': deck}
    return render(request, 'solitaire/game.html', context)