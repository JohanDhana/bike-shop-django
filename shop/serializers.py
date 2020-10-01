from .models import Bikes
from rest_framework import serializers


class BikesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bikes
        fields = [
            'name',
            'size',
            'color',
            'description',
            'full_description',
            'price',
            'image',
            'age_category',
            'bike_categories',
        ]
