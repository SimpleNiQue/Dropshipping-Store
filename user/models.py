from django.db import models
from market.models import Item
from django.contrib.auth.models import User

class Customer(models.Model):
  user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
  name = models.CharField(max_length=200, null=True)
  phone = models.CharField(max_length=200, null=True)
  email = models.CharField(max_length=200, null=True)
  profile_pic = models.ImageField(default="images/custom/person.svg", null=True, blank=True, upload_to = "images/upload/profiles/")
  date_created = models.DateTimeField(auto_now_add=True, null=True)


  def __str__(self):
    return self.name
    
  class Meta:
    verbose_name_plural = 'Customers'
  


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