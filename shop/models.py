from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.forms import ModelForm

# Create your models here.


class Bikes(models.Model):
    name = models.CharField(max_length=35, default="Shimano")
    size = models.CharField(max_length=2, default=26)
    color = models.CharField(max_length=10, default="Blu")
    description = models.TextField(default="bicklete")
    full_description = RichTextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=100)
    image = models.ImageField(default="defalut.png")
    age_category = models.CharField(default=16, max_length=15)
    bike_categories = models.CharField(default="BMX", max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Bikes'


class Images(models.Model):
    bike = models.ForeignKey(Bikes, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Images'


class ShopCart(models.Model):
    user = models.CharField(max_length=20, default=0)
    bike = models.ForeignKey(Bikes, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    # def __str__(self):
    #     return self.bike.name

    # @property
    # def price(self):
    #     return (self.bike.price)

    # @property
    # def amount(self):
    #     return (self.quantity * self.bike.price)

    # @property
    # def varamount(self):
    #     return (self.quantity * self.variant.price)


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    first_name = models.CharField(max_length=10, editable=True)
    last_name = models.CharField(max_length=10, editable=True)
    email = models.CharField(max_length=30, editable=True, default="")
    code = models.CharField(max_length=5, editable=False)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    total = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    adminnote = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name',
                  'address', 'email', 'city', 'country', "city"]


class UserProfile(models.Model):
    user = models.CharField(blank=True, max_length=20)
    email = models.EmailField("", default="")
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + '] '


class OrderProduct(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.CharField(default="", max_length=50)
    bike = models.ForeignKey(Bikes, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bike.title
