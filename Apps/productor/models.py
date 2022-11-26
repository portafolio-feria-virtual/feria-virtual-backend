from django.db import models

# Create your models here.
from django.db import models
from Apps.cuentas.models import Productor

# Create your models here.

class Oferta(models.Model):
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    productorDescription = models.CharField(max_length=255, blank=True)
    # "Mi oferta" (Si/No)
    offer = models.BooleanField(default=False)
    unitPrice = models.IntegerField()
    adminArchives = models.CharField(max_length=255, blank=True)
    techArchives = models.CharField(max_length=255, blank=True)
    economicArchives = models.CharField(max_length=255, blank=True)

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
    image = models.ImageField(blank=True, null=True)


class ImagenVentaLocal(models.Model):
    ventaLocal = models.ForeignKey(VentaLocal, related_name="imagenventalocal", on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False)