from django.db import models
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from Apps.comercianteExtranjero.models import Bid
from Apps.cuentas.models import Carrier
from Apps.productor.models import *
from Apps.comercianteExtranjero.models import *

# Create your models here.

class TransportPostulation(models.Model):
    class Status(models.TextChoices):

        ACCEPTED = "ACCEPTED" , "accepted"
        REFUSED = "REJECTED" , "rejected"
        STANDBY = "STANDBY", "standby"

    bid = models.ForeignKey(Bid, related_name="postulations",on_delete=models.DO_NOTHING, default= None)
    description = models.CharField(max_length=255, blank=True)
    carrier = models.ForeignKey(Carrier, on_delete=models.DO_NOTHING)
    capacity = models.CharField(max_length=255, blank=True)
    cooling = models.BooleanField(default=False)
    postDate = models.DateField(auto_now_add= True) 
    price = models.IntegerField(blank=True, null=True)
    assigned = models.BooleanField(default=False)
    accepted = models.CharField(max_length = 30 , choices = Status.choices , default = Status.STANDBY)
    closed = models.BooleanField(default=False)
    confirmed =  models.BooleanField(default=False)

class Shipping(models.Model):
    class Status(models.TextChoices):
        PREPARATION = "PREPARATION" , "preparation"
        AWAITING_CARRIER = "AWAITING_CARRIER" , "awaiting carrier"
        RECEIVED_BY_CARRIER = "RECEIVED_BY_CARRIER","received by carrier"
        ON_TRACK = "ON_TRACK", "on track"
        RECEPTIONED = "RECEPTIONED", "receptioned"

    status = models.CharField(max_length = 30 , choices = Status.choices , default = Status.PREPARATION)
    bid = models.ForeignKey(Bid, on_delete=models.DO_NOTHING, blank= True, null=True)
    producer= models.ForeignKey(Producer, on_delete=models.DO_NOTHING, blank= True, null=True)
    carrier = models.ForeignKey(Carrier, on_delete=models.DO_NOTHING, blank= True, null=True)

@receiver(post_save, sender= TransportPostulation)
def afterCreateMail(instance=None, created= False, **kwargs):
    if created:
            subject = f"Postulation {instance.name} published"
            carrier = Carrier.objects.get(id = instance.carrier.id)
            message = f"Dear Mr/Ms {carrier.firstName} {carrier.lastName}:\n\nYour postulation {instance.name} has been published successfuly.\nYou will be notified on any change.\n\nsincerely. Feria Virtual Maipo Grande"
            lista = []
            lista.append(carrier.email)
            send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=lista)