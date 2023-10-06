from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin
from django.utils.html import format_html

from .models import Photo, Place

admin.site.register(Photo)


class PhotoInline(SortableStackedInline):
    model = Photo
    readonly_fields = ["show_image"]
    extra = 0

    def show_image(self, obj):
        return format_html(
            '<img src="{}" width="{}" max-height={} />',
            obj.image.url,
            200,
            200,
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [PhotoInline]
