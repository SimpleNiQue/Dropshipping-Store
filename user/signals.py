from django.db.models.signals import post_save
from django.contrib.auth.models import User

from django.contrib.auth.models import Group
from .models import Customer


def customer_profile(sender, instance, created, **kwargs):
  if created:
    group = Group.objects.get(name='Customer')
    instance.groups.add(group)
    
    Customer.objects.create(user=instance, name=instance.username)
    print('\nCustomer Created\n')
    
post_save.connect(customer_profile, sender=User)
    
"""def order(sender, instance, created, **kwargs):
  if created:
    Order.objects.create(status='Pending')
    print("\n Order Placed!!")

post_save.connect(order, sender=User)"""