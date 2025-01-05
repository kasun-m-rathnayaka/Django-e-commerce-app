from django.contrib import admin
from .models import Catrgory, Product, Customer, Order, OrderProduct

admin.site.register(Catrgory)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderProduct)
