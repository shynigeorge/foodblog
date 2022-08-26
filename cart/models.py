from django.db import models

# Create your models here.
from shop.models import Product


class CartList(models.Model):
    cart_id=models.CharField(max_length=250,unique=True)
    date_add=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cart_id
class Items(models.Model):
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(CartList,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.products
    def total(self):
        return self.products.price*self.quantity


