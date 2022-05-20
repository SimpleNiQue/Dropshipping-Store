from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Item
from django import forms

class ItemForm(ModelForm):
  class Meta:
    model = Item
    fields ='__all__'
  
    