from rest_framework.serializers import ModelSerializer

from pokeapi.models import Pokemon, PokemonData

class PokemonDataSerializer(ModelSerializer):
    class Meta:
        model = PokemonData
        fields = '__all__'

class PokemonSerializer(ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'