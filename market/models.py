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
  item_img = models.ImageField(upload_to = "images/")
  description = models.CharField(max_length=200, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  
  def __str__(self):
    return self.name
  class Meta:
    verbose_name_plural = 'Items'
