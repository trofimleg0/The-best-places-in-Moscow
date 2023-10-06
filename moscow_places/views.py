from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse

from moscow_places import services


def show_map(request):
    places = services.get_all_places()

    features = []
    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    place.lon,
                    place.lat,
                ],
            },
            "properties": {
                "title": place.title,
                "placeId": place.pk,
                "detailsUrl": reverse("place_info", args=[place.pk]),
            },
        }
        features.append(feature)

    geo_json = {"type": "FeatureCollection", "features": features}
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
