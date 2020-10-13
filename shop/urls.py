from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bike/<name>', views.details, name='details'),
    path('contact', views.contact, name='contact'),
    path('thank-you', views.thank, name='thank'),
    path('search', views.search, name='search'),
    path('category/<name>', views.category, name='category'),
    path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    path('shopcart/', views.shopcart, name='shopcart'),
    path('orderproduct/', views.orderproduct, name='orderproduct'),

]
