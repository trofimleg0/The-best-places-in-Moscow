from django.contrib import admin

from .models import Photo, Place

# @admin.register(Place)
admin.site.register(Place)
# @admin.register(Photo)
admin.site.register(Photo)
