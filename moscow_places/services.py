from django.shortcuts import get_object_or_404

from moscow_places.models import Place


def get_all_places():
    return Place.objects.prefetch_related("photo").all()


def get_place(place_id):
    return get_object_or_404(
        Place.objects.prefetch_related("photo"), pk=place_id
    )
