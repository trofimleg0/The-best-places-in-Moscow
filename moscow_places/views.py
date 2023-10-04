from django.http import JsonResponse
from django.shortcuts import render

from moscow_places import services


def show_map(request):
    moscow_places = services.get_moscow_legends_instance()
    roofs24 = services.get_roofs24_instance()
    geo_json = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        moscow_places.lon,
                        moscow_places.lat,
                    ],
                },
                "properties": {
                    "title": moscow_places.title,
                    "placeId": "moscow_legends",
                    "detailsUrl": "./static/places/moscow_legends.json",
                },
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        roofs24.lon,
                        roofs24.lat,
                    ],
                },
                "properties": {
                    "title": roofs24.title,
                    "placeId": "roofs24",
                    "detailsUrl": "./static/places/roofs24.json",
                },
            },
        ],
    }
    context = {"geo_json": geo_json}
    return render(request, "index.html", context=context)


def show_place(request, place_id):
    place = services.get_place(place_id)
    response_context = {
        "title": place.title,
        "imgs": [photo.image.url for photo in place.photo.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat,
        },
    }

    return JsonResponse(
        response_context,
        json_dumps_params={
            "ensure_ascii": False,
            "indent": 2,
        },
    )
