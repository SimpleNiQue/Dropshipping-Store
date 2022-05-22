from django.contrib import admin
from .models import Category,Item,Order

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Category)

