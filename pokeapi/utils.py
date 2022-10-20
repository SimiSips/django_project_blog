import requests
from django.utils import timezone

from pokeapi.models import PokemonData, Pokemon

def pokemon_list():
    offset = 100
    empty_list = []
    response = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=100',).json()
    res_data = response['results']
    for res in res_data:
        # digits = [d for d in res['url'] if d.isdigit()]
        # digit = ''.join(digits)
        empty_list.append({
            'name': res['name'],
            # 'url': res['url'],
            # 'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{}.png'.format(digit),
        })

    return empty_list

def save_cell_list():
    poke_data = pokemon_list()
    PokemonData.objects.create(
        #date=timezone.now(),
        json_data=poke_data
    )
    poke_list = []
    for data in poke_data:
        poke_list.append(
            Pokemon(
                name=data['name'],
                # url=data['url'],
                # image=data['image']
            )
        )
    Pokemon.objects.bulk_create(poke_list)
    return 'API Call Saved'
