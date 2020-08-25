from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bike/<name>', views.details, name='details'),
    path('contact', views.contact, name='contact'),
    path('thank-you', views.thank, name='thank'),
    path('search', views.search, name='search')
]
