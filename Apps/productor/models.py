from django.db import models

# Create your models here.
from django.db import models
from Apps.cuentas.models import Productor
from Apps.comercianteExtranjero.models import Licitacion

# Create your models here.

class Oferta(models.Model):
    productor = models.ForeignKey(Productor, on_delete=models.DO_NOTHING, null=True,blank=True)
    licitacion = models.ForeignKey(Licitacion, on_delete=models.DO_NOTHING, null=True,blank=True)
    name = models.CharField(max_length=255, blank=True)
    offerDescription = models.CharField(max_length=255, blank=True)
    offerValue = models.IntegerField()
    offerFileName = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class VentaLocal(models.Model):
    productor = models.ForeignKey(Productor, on_delete=models.DO_NOTHING, null=True, blank=True)
    name = models.CharField(max_length=255, blank=False)
    price = models.IntegerField()
    stock = models.IntegerField()
    location = models.CharField(max_length=255,blank=True)
    image = models.ImageField(null=True, blank=True)
