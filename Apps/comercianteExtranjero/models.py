from django.db import models
from Apps.cuentas.models import InternationalTrader
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.
class Bid(models.Model):
    class ProcessStatus(models.TextChoices):
        PUBLISHED = "PUBLISHED","Published"
        CLOSED = "CLOSED","Closed"
        ASSIGNED = "ASSIGNED","Assigned"
        CANCELED = "CANCELED","Canceled"
        REJECTED = "REJECTED","Rejected"
    

    name = models.CharField(max_length=255,blank=True)
    description = models.CharField(max_length=255,blank=True)
    country = models.CharField(max_length=255,blank=True)
    region = models.CharField(max_length=255,blank=True)
    city = models.CharField(max_length=255,blank=True)
    street = models.CharField(max_length=255,blank=True)
    postalCode = models.CharField(max_length=255,blank=True)
    productList = models.CharField(max_length=255,blank=True) 
    maxAmount = models.IntegerField()
    processStatus = models.CharField(max_length=255, choices= ProcessStatus.choices, default=ProcessStatus.PUBLISHED)
    initDate = models.DateField(auto_now_add= True) 
    closeDate = models.DateField()
    closed = models.BooleanField(default=False)
    editable = models.BooleanField(default=True)
    internationalTrader = models.ForeignKey(InternationalTrader, on_delete=models.DO_NOTHING)

@receiver(post_save, sender= Bid)
def afterCreateMail(instance=None, created= False, **kwargs):
    if created:
            subject = f"Bid {instance.name} created"
            international = InternationalTrader.objects.get(id = instance.internationalTrader.id)
            message = f"Dear Mr/Ms {international.firstName} {international.lastName}:\n\nYour Bid {instance.name} has been published successfully.\n\nSincerely. Feria Virtual Maipo Grande"
            lista = []
            lista.append(international.email)
            send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=lista)
            

