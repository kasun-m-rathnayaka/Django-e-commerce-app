import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.db import models


class Catrgory(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Catrgory, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/images')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name


class Customer(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.f_name} {self.l_name}'


class Order(models.Model):
    product = models.ManyToManyField(Product, through='OrderProduct')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, blank=True, default='')
    phone = models.CharField(max_length=10, blank=True, default='')
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.product


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField(blank=False, default=0)
    sold_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return "{}_{}".format(self.product.__str__(), self.order.__str__())


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=10, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username
