from django.db import models

from webapp.models import Product


class Basket(models.Model):
    quantity = models.IntegerField(verbose_name='количество')

class CartLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)