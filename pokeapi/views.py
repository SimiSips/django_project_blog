from django.shortcuts import render
from django.views.generic import ListView

from .models import Pokemon

# Create your views here.

class PokemonListView(ListView):
    pass

def pokemon_list(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'poke.html', {"pokemon": pokemon})