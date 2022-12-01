from django.db import models
from Apps.comercianteExtranjero.models import Licitacion
from Apps.cuentas.models import Transportista
# Create your models here.

class PostulacionLicitacionTransporte(models.Model):
    licitacion = models.ForeignKey(Licitacion, on_delete=models.DO_NOTHING)
    transportista = models.ForeignKey(Transportista, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=255)
    capacity = models.CharField(max_length=255, blank=True)
    size=models.IntegerField(null=True)
    cooling = models.BooleanField(default=False)
    postDate = models.DateField(auto_now_add= True) 
    

class MetodoTransporte(models.Model):
    transportista = models.ForeignKey(Transportista, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

