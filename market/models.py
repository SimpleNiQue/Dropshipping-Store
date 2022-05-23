from django.contrib.auth.models import User
from django.db import models
from user.models import Customer


class Category(models.Model):
  """Contains Every Category of Items Available"""
  name = models.CharField(max_length=200, null=True,)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'Categories'


class Item(models.Model):
  """Contains all The Available Items"""
  name = models.CharField(max_length=200, null=True)
  price = models.CharField(max_length=200, null=True)
  category  = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
  item_img = models.ImageField(upload_to = "images/")
  description = models.CharField(max_length=200, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  
  def __str__(self):
    return self.name
  class Meta:
    verbose_name_plural = 'Items'


class Size(models.Model):
  """Contains Every Size Available"""
  size_name = models.CharField(max_length=200, null=True,)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'Sizes'

class Cart(models.Model):
  #TODO: Complete it later
  """Contains all The User's selected Items"""
  name = models.CharField(max_length=200, null=True)
  price = models.CharField(max_length=200, null=True)
  size = models.ForeignKey(Size, null=True, on_delete=models.SET_NULL)
  item_img = models.ImageField(upload_to = "images/")
  date_added = models.DateTimeField(auto_now_add=True, null=True)
  
  def __str__(self):
    return self.name
  class Meta:
    verbose_name_plural = 'Carts'


class Order(models.Model):
  STATUS = ("Pending", "Delivered")
    
  customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
  item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  status = models.CharField(max_length=200, null=True)
  
  def __str__(self):
    return self.item.name

  class Meta:
    verbose_name_plural = 'Orders'
