from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.core.files.storage import default_storage
from django.conf import settings
# Create your models here.
from django.db import models
from Apps.cuentas.models import Productor, ComercianteExtranjero
from Apps.comercianteExtranjero.models import Licitacion

# Create your models here.

class Oferta(models.Model):
    class Status(models.TextChoices):

        ACCEPTED = "ACCEPTED" , "accepted"
        REFUSED = "REJECTED" , "rejected"
        STANDBY = "STANDBY", "standby"

    productor = models.ForeignKey(Productor, on_delete=models.DO_NOTHING, null=True,blank=True)
    licitacion = models.ForeignKey(Licitacion, on_delete=models.DO_NOTHING, null=True,blank=True)
    name = models.CharField(max_length=255, blank=True)
    offerDescription = models.CharField(max_length=255, blank=True)
    offerValue = models.IntegerField()
    offerFileName = models.FileField(null=False, blank=False, default=None)
    assigned = models.BooleanField(default=False)
    accepted = models.CharField(max_length = 30 , choices = Status.choices , default = Status.STANDBY)
    closed = models.BooleanField(default=False)
    confirmed =  models.BooleanField(default=False)

    def __str__(self):
        return self.name

class VentaLocal(models.Model):

    class Status(models.TextChoices):
        PUBLISHED = "PUBLISHED" , "published"
        HAS_OFFER = "HAS_OFFER" , "hasOffer"
        CLOSED = "CLOSED","closed"

    status = models.CharField(max_length = 30 , choices = Status.choices , default = Status.PUBLISHED)
    sold =models.BooleanField(default=False)
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=False)
    price = models.IntegerField()
    stock = models.IntegerField()
    location = models.CharField(max_length=255,blank=True)
    
    def __str__(self):
        return self.name
    


class ImagenVentaLocal(models.Model):
    ventaLocal = models.ForeignKey(VentaLocal, related_name="imagenventalocal", on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False)


@receiver(post_save)
def afterCreateMail(sender, instance=None, created= False, **kwargs):
    if sender.__name__ == "VentaLocal":
        if created:
            subject = f"Venta {instance.name} creada"
            productor = Productor.objects.get(id = instance.productor.id)
            message = f"Estimado {productor.firstName} {productor.lastName}:\n\nSu venta de {instance.name} ha sido publicada satisfactoriamente.\nSe le notificará de las ofertas que reciba.\n\nAtentamente. Feria Virtual Maipo Grande"
            lista = []
            lista.append(productor.email)
            send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=lista)


    if sender.__name__ == "Oferta":
        if created:
            licitacion = Licitacion.objects.get(id=instance.licitacion.id)
            subject = f"Oferta {instance.name} ingresada en la licitación {licitacion} "
            productor = Productor.objects.get(id = instance.productor.id)
            message = f"Estimado {productor.firstName} {productor.lastName}:\n\nSu oferta de {instance.name} ha sido publicada satisfactoriamente.\nSe le notificará de cualquier cambio de estado.\n\nAtentamente. Feria Virtual Maipo Grande"
            lista = []
            lista.append(productor.email)
            send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=lista)

# @receiver(post_save, sender=ImagenVentaLocal)
# def deleteImage(sender, instance=None, created=False, **kwargs):
#     if created:
#         print(instance.image)
#         default_storage.delete("Diagrama signup.png")
#         default_storage.delete("Diagrama_signup.png")


