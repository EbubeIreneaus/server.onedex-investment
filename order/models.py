from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
import logging
from . import signals
from django.forms import model_to_dict
from authentication.models import User

# Create your models here.

class Order(models.Model):
    channels = (
        ("BTC", "BTC"),
        ("USDT", "USDT"),
        ('MEMO', "MEMO")
    )
    types = (
        ("deposit", "DEPOSIT"),
        ("withdraw", "WITHDRAW"),
    )
    status = (
        ('approved', "APPROVE"),
        ('declined', "DECLINE"),
        ('pending', "PENDING")
    )
    orderId = models.CharField(max_length=9, unique=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    channel = models.CharField(max_length=20, choices=channels, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    wallet = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=10, choices=types)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=status, default="pending")


    def __str__(self):
        return f'{self.orderId} {self.type}'
    
@receiver(pre_save, sender=Order)
def presave_order_signal(sender, instance, update_fields, **kwargs):
    try:
        old_data = model_to_dict(sender.objects.get(id=instance.id))
        new_data= model_to_dict(instance)
        signals.handle_order_signal(old_data=old_data, new_data=new_data)
    except Exception as e:
        print(e)    
    
    

class Investment(models.Model):
    plans = (
        ("bronze", "BRONZE"),
        ("silver", "SILVER"),
        ("gold", "GOLD"),
        ("vip", "VIP")
    )
    status = (
        ('completed', "completed"),
        ('ongoing', "ongoing"),
    )
    orderId = models.CharField(max_length=9, unique=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    plan = models.CharField(max_length=20, choices=plans)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=status, default="ongoing")

    def __str__(self):
        return f'{self.orderId} {self.plan}'
    