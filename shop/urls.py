from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bike/<name>', views.details, name='details')
]
