import folium
import django

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from pokemon_entities.models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    local_time = django.utils.timezone.localtime()
    pokemon_entity = PokemonEntity.objects.filter(
        appeared_at__lte=local_time,
        disappeared_at__gte=local_time,
     )

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemon_entity:
        add_pokemon(
                folium_map, pokemon.lat,
                pokemon.lon,
                request.build_absolute_uri(pokemon.pokemon.photo.url)
            )
    pokemons_on_page = []
    for num, pokemon in enumerate(pokemons):
        pokemons_on_page.append(
            {
                'pokemon_id': pokemon.id,
                'title_ru': pokemon.title,
            }
        )        
        if pokemon.photo:
            url = pokemon.photo.url
            pokemons_on_page[num]['img_url'] = request.build_absolute_uri(url)

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=int(pokemon_id))
    pokemon_entity = pokemon.entities.all()
    next_evolution = {}
    previous_evolution = {}
    if pokemon.children.all():
        pokemon_children = pokemon.children.all()[0]
        next_evolution = {
            'title_ru': pokemon_children.title,
            'pokemon_id': pokemon_children.id,
         }
        if pokemon_children.photo:
            url = pokemon_children.photo.url
            next_evolution['img_url'] = request.build_absolute_uri(url)        
    else:
        pokemon_children = None
    if pokemon.parent:
        previous_evolution = {
            'title_ru': pokemon.parent.title,
            'pokemon_id': pokemon.parent.id,
         }
        if pokemon.parent.photo:
            url = pokemon.parent.photo.url
            previous_evolution['img_url'] = request.build_absolute_uri(url)
    else:
        previous_evolution = None
    requested_pokemon = {
                'pokemon_id': pokemon.id,
                'title_ru': pokemon.title,
                'description': pokemon.description,
                'title_en': pokemon.title_en,
                'title_jp': pokemon.title_jp,
                'previous_evolution': previous_evolution,
                'next_evolution': next_evolution,
             }
    if pokemon.photo:
        url = pokemon.photo.url
        requested_pokemon['img_url'] = request.build_absolute_uri(url)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemon_entity:
        if pokemon.pokemon.photo:
            add_pokemon(
                folium_map, pokemon.lat,
                pokemon.lon,
                request.build_absolute_uri(pokemon.pokemon.photo.url)
            )
        else:
            add_pokemon(
                folium_map, pokemon.lat,
                pokemon.lon,
            )            

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': requested_pokemon
    })
