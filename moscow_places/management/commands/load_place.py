import os
from io import BytesIO

import requests
from django.core.management.base import BaseCommand

from moscow_places.models import Place


class Command(BaseCommand):
    help = "Load Moscow places data in DB"

    def add_arguments(self, parser):
        parser.add_argument(
            "json_url",
            type=str,
            help="URL of the JSON file",
        )

    def handle(self, *args, **options):
        response = requests.get(options["json_url"])
        response.raise_for_status()
        place_info = response.json()

        place = Place.objects.prefetch_related("photo").get_or_create(
            title=place_info["title"],
            short_description=place_info["description_short"],
            long_description=place_info["description_long"],
            lon=place_info["coordinates"]["lng"],
            lat=place_info["coordinates"]["lat"],
        )[0]

        if place_info["imgs"]:
            for num, img_url in enumerate(place_info["imgs"], start=1):
                response = requests.get(img_url)
                response.raise_for_status()
                image_content = BytesIO(response.content)
                image_name = os.path.basename(img_url)

                place_image = place.photo.get_or_create(
                    order=num, place=place.title
                )[0]

                place_image.image.save(image_name, image_content, save=True)
