from django.contrib import admin
from .models import Category, Customer, Item, Order

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Category)

