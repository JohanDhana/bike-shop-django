from django.contrib import admin
import admin_thumbnails

# Register your models here.
from .models import Bikes, Images


@admin_thumbnails.thumbnail('image')
class BikesImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1


@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image', 'title', 'image_thumbnail']


class BikesAdmin(admin.ModelAdmin):
    # list_display = ['title', 'category', 'status', 'image_tag']
    list_filter = ['bike_categories']
    inlines = [BikesImageInline]
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(Bikes, BikesAdmin)
admin.site.register(Images, ImagesAdmin)
