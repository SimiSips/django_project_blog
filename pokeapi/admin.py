from django.contrib import admin

from .models import Pokemon, PokemonData

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(PokemonData)

