from django.contrib.auth.models import User
from django.db import models


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
  item_img = models.ImageField(upload_to = "images/upload/items/")
  description = models.CharField(max_length=200, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  
  def __str__(self):
    return self.name
  class Meta:
    verbose_name_plural = 'Items'


class Customer(models.Model):
  user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
  name = models.CharField(max_length=200, null=True)
  phone = models.CharField(max_length=200, null=True)
  email = models.CharField(max_length=200, null=True)
  profile_pic = models.ImageField(default="images/custom/person.svg", null=True, blank=True, upload_to = "images/upload/profiles/")
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
    return self.name
    
  class Meta:
    verbose_name_plural = 'Customers'
  
class Order(models.Model):
  STATUS = (
    ('Pending','Pending'),
    ('Delivered','Delivered'),
    )
    
  customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
  item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  status = models.CharField(max_length=200, null=True, choices=STATUS)
  
  def __str__(self):
    return self.item.name

  class Meta:
    verbose_name_plural = 'Orders'