from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.core.validators import FileExtensionValidator
from django.core.files.storage import default_storage
from django.conf import settings
from django.db import models
from Apps.cuentas.models import Producer, InternationalTrader
from Apps.comercianteExtranjero.models import Bid

# Create your models here.

class Offer(models.Model):
    class Status(models.TextChoices):

        ACCEPTED = "ACCEPTED" , "accepted"
        REFUSED = "REJECTED" , "rejected"
        STANDBY = "STANDBY", "standby"

    producer = models.ForeignKey(Producer, on_delete=models.DO_NOTHING, null=True,blank=True)
    bid = models.ForeignKey(Bid,related_name="offers", on_delete=models.DO_NOTHING, null=True,blank=True)
    name = models.CharField(max_length=255, blank=True)
    offerDescription = models.CharField(max_length=255, blank=True)
    offerValue = models.IntegerField()
    offerFile = models.FileField(null=False, blank=False, default=None, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    assigned = models.BooleanField(default=False)
    editable = models.BooleanField(default=True)
    status = models.CharField(max_length = 30 , choices = Status.choices , default = Status.STANDBY)
    closed = models.BooleanField(default=False)
    confirmed =  models.BooleanField(default=False)

    def __str__(self):
        return self.name

class LocalSale(models.Model):

    class Status(models.TextChoices):
        PUBLISHED = "PUBLISHED" , "published"
        HAS_OFFER = "HAS_OFFER" , "hasOffer"
        CLOSED = "CLOSED","closed"

    status = models.CharField(max_length = 30 , choices = Status.choices , default = Status.PUBLISHED)
    sold =models.BooleanField(default=False)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=False)
    price = models.IntegerField()
    stock = models.IntegerField()
    location = models.CharField(max_length=255,blank=True)
    published = models.DateField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    editable = models.BooleanField(default=True)
    confirmed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    


class LocalSaleImage(models.Model):
    localSale = models.ForeignKey(LocalSale, related_name="localsaleimage", on_delete=models.CASCADE)
    image = models.FileField(null=False, blank=False,validators=[ FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'svg']),])



@receiver(post_save)
def afterCreateMail(sender, instance=None, created= False, **kwargs):
    if sender.__name__ == "LocalSale":
        if created:
            subject = f"Local Sale {instance.name} published"
            producer = Producer.objects.get(id = instance.producer.id)
            message = f"Dear {producer.firstName} {producer.lastName}:\n\nYour sale {instance.name} has been published successfuly.\nYou will be notified on any offer it receives.\n\nSincerely. Feria Virtual Maipo Grande"
            lista = []
            lista.append(producer.email)
            send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=lista)


    if sender.__name__ == "Offer":
        if created:
            bid= Bid.objects.get(id=instance.bid.id)
            subject = f"Offer {instance.name} published at biddin proccess {bid.name} "
            producer = Producer.objects.get(id = instance.producer.id)
            message = f"Dear Mr/Ms {producer.firstName} {producer.lastName}:\n\nYour offer{instance.name} has been published successfully.\nYou will be notified of any change on it.\n\nSincerely. Feria Virtual Maipo Grande"
            lista = []
            lista.append(producer.email)
            send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=lista)

