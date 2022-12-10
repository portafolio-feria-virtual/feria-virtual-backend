from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.core.mail import send_mail
from Apps.cuentas.models import *
# Create your models here.

class Contrato(models.Model):
    class Types(models.TextChoices):
        COMERCIANTE_LOCAL = "COMERCIANTE LOCAL" , "comerciante local"
        COMERCIANTE_EXTRANJERO = "COMERCIANTE EXTRANJERO" , "comerciante extranjero"
        CONSULTOR = "CONSULTOR","consultor"
        PRODUCTOR = "PRODUCTOR", "productor"
    type = models.CharField(max_length = 30 , choices = Types.choices , default = Types.COMERCIANTE_LOCAL)
    companyName = models.CharField(max_length=255, blank=True)
    initDate = models.DateField(auto_now_add=True)
    modifyDate = models.DateField(auto_now=True)
    endDate = models.DateField(blank=True, null=True)
    isActive = models.BooleanField(default=True)
    fileName = models.FileField(blank=True, null=True)
    

@receiver(pre_save, sender=Contrato)
def checkType(sender, instance=None, **kwargs):
    if instance.type == "PRODUCTOR":
        productor = Productor.objects.get(businessName=instance.companyName)
        productor.is_active = True
        productor.save()
    if instance.type == "COMERCIANTE EXTRANJERO":
        extranjero = ComercianteExtranjero.objects.get(businessName=instance.companyName)
        extranjero.is_active = True
        extranjero.save()
    if instance.type == "COMERCIANTE LOCAL":
        cLocal = ComercianteLocal.objects.get(businessName=instance.companyName)
        cLocal.is_active = True
        cLocal.save()
    if instance.type == "TRANSPORTISTA":
        transportista = Transportista.objects.get(businessName=instance.companyName)
        transportista.is_active = True
        transportista.save()
            