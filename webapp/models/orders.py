from django.db import models

class Order(models.Model):
    products = models.ManyToManyField(to='Product', through='OrderProduct')
    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderProduct(models.Model):
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    order = models.ForeignKey(to='Order', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)