from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Bikes
from .forms import ContactForm, HomeSearchForm, SearchForm
from django.urls import reverse

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = HomeSearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/search?q='+form.cleaned_data['search'])
    # if a GET (or any other method) we'll create a blank form
    else:
        form = HomeSearchForm()
        # __gte shfaq me te medha se 16
    kid_bikes = Bikes.objects.filter(size__lte=20)
    BMX_bikes = Bikes.objects.filter(bike_categories="BMX")
    context = {'kid_bikes': kid_bikes, 'BMX_bikes': BMX_bikes, 'form': form}

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


def search(request):
    search_query = request.GET.get('q', '')
    search_category = request.GET.get('category', '')
    search_size = request.GET.get('size', '')
    category = ''
    size = ''
    print(search_category)
    if request.method == 'POST':
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            print(form.cleaned_data)
            if form.cleaned_data['category']:
                category = form.cleaned_data['category'].split('-')[1]

            if form.cleaned_data['size']:
                size = form.cleaned_data['size']

            # redirect to a new URL:
            return HttpResponseRedirect('/search?q='+form.cleaned_data['query']+'&category='+category+'&size='+size)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()
        if search_category and search_size:
            bikes = Bikes.objects.filter(name__contains=search_query) & Bikes.objects.filter(
                bike_categories=search_category) & Bikes.objects.filter(
                size=search_size)
        elif search_size:
            bikes = Bikes.objects.filter(name__contains=search_query) & Bikes.objects.filter(
                size=search_size)
        elif search_category:
            bikes = Bikes.objects.filter(name__contains=search_query) & Bikes.objects.filter(
                bike_categories=search_category)
        else:
            bikes = Bikes.objects.filter(name__contains=search_query)

    context = {'bikes': bikes, 'form': form}
    return render(request, 'shop/search.html', context)
