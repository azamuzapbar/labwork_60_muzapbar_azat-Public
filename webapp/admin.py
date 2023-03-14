from django.contrib import admin

from webapp.models import Product, Basket, Order, OrderProduct

admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(Order)
admin.site.register(OrderProduct)