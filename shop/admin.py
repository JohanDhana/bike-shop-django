from django.contrib import admin
import admin_thumbnails

# Register your models here.
from .models import Bikes, Images, ShopCart

admin.site.site_header = 'Bike shop'


@admin_thumbnails.thumbnail('image')
class BikesImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1


@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image', 'title', 'image_thumbnail']


class BikesAdmin(admin.ModelAdmin):
    list_display = ['name', 'bike_categories']
    list_filter = ['size', 'bike_categories']
    inlines = [BikesImageInline]
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(Bikes, BikesAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(ShopCart)
