from django.db import models
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from Apps.comercianteExtranjero.models import Licitacion
from Apps.cuentas.models import Transportista
from Apps.productor.models import *
from Apps.comercianteExtranjero.models import *

# Create your models here.

class PostulacionLicitacionTransporte(models.Model):
    class Status(models.TextChoices):

        ACCEPTED = "ACCEPTED" , "accepted"
        REFUSED = "REJECTED" , "rejected"
        STANDBY = "STANDBY", "standby"

    licitacion = models.ForeignKey(Licitacion, on_delete=models.DO_NOTHING, default= None)
    description = models.CharField(max_length=255, blank=True)
    transportista = models.ForeignKey(Transportista, on_delete=models.DO_NOTHING)
    capacity = models.CharField(max_length=255, blank=True)
    cooling = models.BooleanField(default=False)
    postDate = models.DateField(auto_now_add= True) 
    price = models.IntegerField(blank=True, null=True)
    assigned = models.BooleanField(default=False)
    accepted = models.CharField(max_length = 30 , choices = Status.choices , default = Status.STANDBY)
    closed = models.BooleanField(default=False)
    confirmed =  models.BooleanField(default=False)

class Envio(models.Model):
    class Status(models.TextChoices):
        PREPARATION = "PREPARATION" , "preparation"
        AWAITING_CARRIER = "AWAITING_CARRIER" , "awaiting carrier"
        RECEIVED_BY_CARRIER = "RECEIVED_BY_CARRIER","received by carrier"
        ON_TRACK = "ON_TRACK", "on track"
        RECEPTIONED = "RECEPTIONED", "receptioned"

    status = models.CharField(max_length = 30 , choices = Status.choices , default = Status.PREPARATION)
    licitacion = models.ForeignKey(Licitacion, on_delete=models.DO_NOTHING, blank= True, null=True)
    productor= models.ForeignKey(Productor, on_delete=models.DO_NOTHING, blank= True, null=True)
    transportista= models.ForeignKey(Transportista, on_delete=models.DO_NOTHING, blank= True, null=True)

@receiver(post_save, sender= PostulacionLicitacionTransporte)
def afterCreateMail(instance=None, created= False, **kwargs):
    if created:
            subject = f"Venta {instance.name} creada"
            transportista = Transportista.objects.get(id = instance.transportista.id)
            message = f"Estimado {transportista.firstName} {transportista.lastName}:\n\nSu venta de {instance.name} ha sido publicada satisfactoriamente.\nSe le notificará de las ofertas que reciba.\n\nAtentamente. Feria Virtual Maipo Grande"
            lista = []
            lista.append(transportista.email)
            send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=lista)