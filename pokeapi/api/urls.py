from django.urls import path

from pokeapi.api.views import Pokemons
from pokeapi.views import pokemon_list

urlpatterns = [
    path('info/', Pokemons.as_view()),
    path('', pokemon_list, name="Pokemons")
]