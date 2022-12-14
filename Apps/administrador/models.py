from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.core.mail import send_mail
from django.core.validators import FileExtensionValidator
from Apps.cuentas.models import *
# Create your models here.

class Contract(models.Model):
    class Types(models.TextChoices):
        LOCAL_TRADER = "LOCAL TRADER" , "local trader"
        INTERNATIONAL_TRADER = "INTERNATIONAL TRADER" , "international trader"
        CARRIER = "CARRIER","carrier"
        PRODUCER = "PRODUCER", "producer"
    type = models.CharField(max_length = 30 , choices = Types.choices , default = Types.LOCAL_TRADER)
    editable = models.BooleanField(default= True)
    companyName = models.CharField(max_length=255, blank=True)
    initDate = models.DateField(auto_now_add=True)
    modifyDate = models.DateField(auto_now=True)
    endDate = models.DateField(blank=True, null=True)
    isActive = models.BooleanField(default=True)
    file = models.FileField(blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    

@receiver(pre_save, sender=Contract)
def checkType(sender, instance=None, **kwargs):
    if instance.type == "PRODUCER":
        producer = Producer.objects.get(businessName=instance.companyName)
        producer.is_active = True
        producer.save()
    if instance.type == "INTERNATIONAL TRADER":
        international = InternationalTrader.objects.get(businessName=instance.companyName)
        international.is_active = True
        international.save()
    if instance.type == "LOCAL TRADER":
        local = LocalTrader.objects.get(businessName=instance.companyName)
        local.is_active = True
        local.save()
    if instance.type == "CARRIER":
        carrier = Carrier.objects.get(businessName=instance.companyName)
        carrier.is_active = True
        carrier.save()
            