from django.shortcuts import get_object_or_404

from moscow_places.models import Place


def get_moscow_legends_instance():
    return Place.objects.get(title="Экскурсионная компания «Легенды Москвы»")


def get_roofs24_instance():
    return Place.objects.get(title="Экскурсионный проект «Крыши24.рф»")


def get_place(place_id):
    return get_object_or_404(
        Place.objects.prefetch_related("photo"), pk=place_id
    )
