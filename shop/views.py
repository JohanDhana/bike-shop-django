from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Bikes
from .forms import ContactForm

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


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(form.data)
            return HttpResponseRedirect('/thank-you')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'shop/contact.html', {'form': form})


def thank(request):
    return render(request, 'shop/thank.html')
