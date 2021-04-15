from django.db import models
from products.models import Product


class ShopList(models.Model):
    pass

class ShopItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    list_name = models.ForeignKey('ShopList', related_name='items', on_delete=models.PROTECT)

