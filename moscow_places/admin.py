from django.contrib import admin

from .models import Photo, Place

admin.site.register(Photo)


class PhotoInline(admin.TabularInline):
    model = Photo


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
