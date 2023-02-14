import folium

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.timezone import localtime
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
    local_time = localtime()
    pokemons_entities = PokemonEntity.objects.filter(
        appeared_at__lt=local_time,
        disappeared_at__gt=local_time
    )

    media_url = request.build_absolute_uri('/media/')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.latitude,
            pokemon_entity.longitude,
            f"{media_url}{pokemon_entity.pokemon.image}"
        )

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': f"{media_url}{pokemon.image}",
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    media_url = request.build_absolute_uri('/media/')

    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
    except Pokemon.DoesNotExist:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    local_time = localtime()
    pokemons_entities = PokemonEntity.objects.filter(
        pokemon=pokemon,
        appeared_at__lt=local_time,
        disappeared_at__gt=local_time
    )

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.latitude,
            pokemon_entity.longitude,
            f"{media_url}{pokemon_entity.pokemon.image}"
        )

    next_evolution = pokemon.next_evolutions.all().first()
    pokemon_next_evolution = {}
    if next_evolution:
        pokemon_next_evolution = {
            "title_ru": next_evolution.title,
            "pokemon_id": next_evolution.id,
            "img_url": f"{media_url}{next_evolution.image}",
        }

    pokemon_previous_evolution = {}
    if pokemon.previous_evolution:
        pokemon_previous_evolution = {
            "title_ru": pokemon.previous_evolution.title,
            "pokemon_id": pokemon.previous_evolution.id,
            "img_url": f"{media_url}{pokemon.previous_evolution.image}",
        }

    pokemon_info = {
        "pokemon_id": pokemon_id,
        "title_ru": pokemon.title,
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
        "description": pokemon.description,
        "img_url": f"{media_url}{pokemon.image}",
        "previous_evolution": pokemon_previous_evolution,
        "next_evolution": pokemon_next_evolution,
        "entities": [],
    }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_info
    })
