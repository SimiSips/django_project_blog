from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from pokeapi.api.serializers import PokemonDataSerializer, PokemonSerializer
from pokeapi.models import Pokemon, PokemonData

class Pokemons(APIView):

    def get(self, request):
        content = PokemonData.objects.all().last()
        serializer = PokemonDataSerializer(content)
        return Response(serializer.data)

class PokemonsListView(ListAPIView):
    serializer_class = PokemonSerializer

    def get_queryset(self):
        data = Pokemon.objects.all()
        name = self.request.query_params.get('name')
        data.filter(name__in = name)
        return data
