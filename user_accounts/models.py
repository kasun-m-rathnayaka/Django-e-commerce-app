from django.db import models
from store.models import Product, User

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    purchase = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return f'{self.quantity} X {self.product.name}'