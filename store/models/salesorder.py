from django.db import  models
from store.models.retailstore import RetailStore
from store.models.product import Product


class SalesOrder(models.Model):
    retail = models.ForeignKey(RetailStore, on_delete=models.CASCADE, related_name='orders')
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    order_items = models.ManyToManyField(Product, through='OrderItem')

class OrderItem(models.Model):
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.qty} of {self.product.name}"
