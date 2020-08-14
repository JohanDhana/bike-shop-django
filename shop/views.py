from django.shortcuts import render
from django.http import HttpResponse
from .models import Bikes
# Create your views here.


def index(request):
    # __gte shfaq me te medha se 16
    kid_bikes = Bikes.objects.filter(size__lte=20)
    BMX_bikes = Bikes.objects.filter(bike_categories="BMX")
    context = {'kid_bikes': kid_bikes, 'BMX_bikes': BMX_bikes}
    return render(request, 'shop/index.html', context)


def details(request, name):
    selected_bike = Bikes.objects.get(name=name)
    show_bike = {'bike': selected_bike}
    return render(request, 'shop/details.html', show_bike)

