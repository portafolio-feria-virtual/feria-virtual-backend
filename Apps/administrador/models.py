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
        


        
          
    type = models.CharField(max_length = 30 , choices = Types.choices , 
                            # Default is user is teacher
                            default = Types.COMERCIANTE_LOCAL)
    
    companyName = models.CharField(max_length=255, blank=True)
    initDate = models.DateField(auto_now_add=True)
    modifyDate = models.DateField(auto_now=True)
    endDate = models.DateField(blank=True, null=True)
    isActive = models.BooleanField(default=True)
    fileName = models.CharField(max_length=255, blank=True)

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
        extranjero = Transportista.objects.get(businessName=instance.companyName)
        extranjero.is_active = True
        extranjero.save()
            # print(instance.email)

            # subject = f"Bienvenido {instance.firstName} {instance.lastName} a Maipo Grande"
            # message = f"Estimado {instance.firstName} {instance.lastName}:\nEn Maipo Grande estamos muy contentos de contar con tu apoyo.\nEn las proximas horas uno de nuestros ejecutivos se contactará contigo "
            # lista = []
            # lista.append(instance.email)
            # send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=lista)