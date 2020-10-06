from django.contrib import admin
# Register your models here.
from .models import Bikes

admin.site.site_header = 'Bike shop'


class BikesAdmin(admin.ModelAdmin):
    list_display = ('name', 'bike_categories')
    list_filter = ('size', 'bike_categories')


admin.site.register(Bikes, BikesAdmin)

