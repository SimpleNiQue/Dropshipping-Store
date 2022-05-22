from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Item,Order
from django import forms

class ItemForm(ModelForm):
  class Meta:
    model = Item
    fields ='__all__'


  
class OrderForm(ModelForm):
  
  class Meta:
    model = Order
    fields = '__all__'
    exclude = ['status']
    
  
    