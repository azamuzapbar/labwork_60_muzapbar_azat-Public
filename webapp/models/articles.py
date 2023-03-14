from django.db import models

class Basket(models.Model):
    quantity = models.IntegerField(verbose_name='количество')