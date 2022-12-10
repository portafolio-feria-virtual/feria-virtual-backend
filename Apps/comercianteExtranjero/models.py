from django.db import models
from Apps.cuentas.models import ComercianteExtranjero
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.
class Licitacion(models.Model):
    class ProcessStatus(models.TextChoices):
        publicar = "Publicada","Publicada"
        cerrar = "Cerrada","Cerrada"
        adjudicar = "Adjudicada","Adjudicada"
        cancelar = "Cancelada","Cancelada"
        rechazar = "Rechazada","Rechazada"
    

    name = models.CharField(max_length=255,blank=True)
    description = models.CharField(max_length=255,blank=True)
    country = models.CharField(max_length=255,blank=True)
    region = models.CharField(max_length=255,blank=True)
    city = models.CharField(max_length=255,blank=True)
    street = models.CharField(max_length=255,blank=True)
    postalCode = models.CharField(max_length=255,blank=True)
    productList = models.CharField(max_length=255,blank=True) 
    maxAmount = models.IntegerField()
    processStatus = models.CharField(max_length=255, choices= ProcessStatus.choices, default=ProcessStatus.publicar)
    initDate = models.DateField(auto_now_add= True) 
    closeDate = models.DateField()
    extranjero = models.ForeignKey(ComercianteExtranjero, on_delete=models.DO_NOTHING)

@receiver(post_save, sender= Licitacion)
def afterCreateMail(instance=None, created= False, **kwargs):
    if created:
            subject = f"Licitacion {instance.name} creada"
            extranjero = ComercianteExtranjero.objects.get(id = instance.extranjero.id)
            message = f"Estimado {extranjero.firstName} {extranjero.lastName}:\n\nSu licitacion de {instance.name} ha sido publicada satisfactoriamente.\n\nAtentamente. Feria Virtual Maipo Grande"
            lista = []
            lista.append(extranjero.email)
            send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=lista)

