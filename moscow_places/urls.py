from django.conf.urls.static import static
from django.urls import path

from moscow_places.views import show_map, show_place
from places import settings

urlpatterns = [
    path("", show_map),
    path("places/<int:place_id>/", show_place),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
