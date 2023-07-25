from django.db import models
from shopapp.models import Products


class Cart(models.Model):
    Cart_id = models.CharField(max_length=250, null=True)
    Date_Added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['Date_Added']

    def __str__(self):
        return '{}'. format(self.Cart_id)


class Cart_Item(models.Model):
    Product = models.ForeignKey(Products, on_delete=models.CASCADE)
    Cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Cart_Item'

    def Sub_Total(self):
        return self.Product.price * self.Quantity

    def __str__(self):
        return '{}' .format(self.Product)

