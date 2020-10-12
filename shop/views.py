from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Bikes, Images, ShopCart, ShopCartForm
from .forms import ContactForm, HomeSearchForm, SearchForm
from rest_framework import viewsets
from rest_framework import permissions
from shop.serializers import BikesSerializer
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class BikesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Bikes to be viewed or edited.
    """
    queryset = Bikes.objects.all().order_by('id')
    serializer_class = BikesSerializer
    permission_classes = [permissions.IsAuthenticated]

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
    images = Images.objects.filter(bike_id=selected_bike.id)
    show_bike = {'bike': selected_bike, 'images': images}
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
    query = ''

    if request.method == 'POST':
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            query = ''.join(
                e for e in form.cleaned_data['query'] if e.isalnum())

            if form.cleaned_data['category']:
                category = form.cleaned_data['category']

            if form.cleaned_data['size']:
                size = form.cleaned_data['size']

        # redirect to a new URL:
        return HttpResponseRedirect('/search?q='+query+'&category='+category+'&size='+size)
    # if a GET (or any other method) we'll create a blank form
    else:
        search_query = ''.join(e for e in search_query if e.isalnum())

        form = SearchForm(initial={
            'query': search_query, 'category': search_category, 'size': search_size})

        if search_category and search_size:
            bikes = Bikes.objects.filter(name__icontains=search_query) & Bikes.objects.filter(
                bike_categories=search_category) & Bikes.objects.filter(
                size=search_size)
        elif search_size:
            bikes = Bikes.objects.filter(name__icontains=search_query) & Bikes.objects.filter(
                size=search_size)
        elif search_category:
            bikes = Bikes.objects.filter(name__icontains=search_query) & Bikes.objects.filter(
                bike_categories=search_category)
        else:
            bikes = Bikes.objects.filter(name__icontains=search_query)

    context = {'bikes': bikes, 'form': form, }
    return render(request, 'shop/search.html', context)


def category(request, name):
    selected_category = Bikes.objects.filter(bike_categories__iexact=name)
    context = {'bikes': selected_category, 'category_name': name}
    return render(request, 'shop/category.html', context)


@login_required(login_url='/admin')  # Check login
def addtoshopcart(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information

    if request.method == 'POST':  # if there is a post
        form = ShopCartForm(request.POST)
        if form.is_valid():
            data = ShopCart()
            data.user_id = current_user.id
            data.bike_id = id
            data.quantity = form.cleaned_data['quantity']
            data.save()
            messages.success(request, "Product added to Shopcart ")
            return HttpResponseRedirect(url)

    else:  # if there is no post
        data = ShopCart()
        data.user_id = current_user.id
        data.product_id = id
        data.quantity = 1
        data.variant_id = None
        data.save()  #
        messages.success(request, "Product added to Shopcart")
        return HttpResponseRedirect(url)


def shopcart(request):
    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        total += float(rs.bike.price) * rs.quantity

    context = {'shopcart': shopcart,
               'total': total,
               }
    print(shopcart)

    return render(request, 'shop/shopcart_products.html', context)


@login_required(login_url='/admin')  # Check login
def deletefromcart(request, id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Your item deleted form Shopcart.")
    return HttpResponseRedirect("/shopcart")


# def orderproduct(request):
#     category = Category.objects.all()
#     current_user = request.user
#     shopcart = ShopCart.objects.filter(user_id=current_user.id)
#     total = 0
#     for rs in shopcart:
#         if rs.product.variant == 'None':
#             total += rs.product.price * rs.quantity
#         else:
#             total += rs.variant.price * rs.quantity

#     if request.method == 'POST':  # if there is a post
#         form = OrderForm(request.POST)
#         # return HttpResponse(request.POST.items())
#         if form.is_valid():
#             # Send Credit card to bank,  If the bank responds ok, continue, if not, show the error
#             # ..............

#             data = Order()
#             # get product quantity from form
#             data.first_name = form.cleaned_data['first_name']
#             data.last_name = form.cleaned_data['last_name']
#             data.address = form.cleaned_data['address']
#             data.city = form.cleaned_data['city']
#             data.phone = form.cleaned_data['phone']
#             data.user_id = current_user.id
#             data.total = total
#             data.ip = request.META.get('REMOTE_ADDR')
#             ordercode = get_random_string(5).upper()  # random cod
#             data.code = ordercode
#             data.save()

#             for rs in shopcart:
#                 detail = OrderProduct()
#                 detail.order_id = data.id  # Order Id
#                 detail.product_id = rs.product_id
#                 detail.user_id = current_user.id
#                 detail.quantity = rs.quantity
#                 if rs.product.variant == 'None':
#                     detail.price = rs.product.price
#                 else:
#                     detail.price = rs.variant.price
#                 detail.variant_id = rs.variant_id
#                 detail.amount = rs.amount
#                 detail.save()
#                 # ***Reduce quantity of sold product from Amount of Product
#                 if rs.product.variant == 'None':
#                     product = Product.objects.get(id=rs.product_id)
#                     product.amount -= rs.quantity
#                     product.save()
#                 else:
#                     variant = Variants.objects.get(id=rs.product_id)
#                     variant.quantity -= rs.quantity
#                     variant.save()
#                 # ************ <> *****************

#             # Clear & Delete shopcart
#             ShopCart.objects.filter(user_id=current_user.id).delete()
#             request.session['cart_items'] = 0
#             messages.success(
#                 request, "Your Order has been completed. Thank you ")
#             return render(request, 'Order_Completed.html', {'ordercode': ordercode, 'category': category})
#         else:
#             messages.warning(request, form.errors)
#             return HttpResponseRedirect("/order/orderproduct")

#     form = OrderForm()
#     profile = UserProfile.objects.get(user_id=current_user.id)
#     context = {'shopcart': shopcart,
#                'category': category,
#                'total': total,
#                'form': form,
#                'profile': profile,
#                }
#     return render(request, 'Order_Form.html', context)
