from django.shortcuts import render
from .models import Item
from.forms import ItemForm

def index(request):
    all_items = Item.objects.all()
  
    context ={'items':all_items,}
    return render(request, 'market/index.html', context)


def product(request: str, prod_id: str):
    context = {
        "prod_id":prod_id,
    }
    return render(request, 'market/product.html', context)


def products(request):
    all_items = Item.objects.all()
  
    context ={
        'items':all_items,
    }
    return render(request, 'market/products.html', **context)

def cart(request):
    context = {}
    return render(request, 'market/cart.html', context)