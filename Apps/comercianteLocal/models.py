from django.db import models
from Apps.cuentas.models import *

# Create your models here.
class SolicitudCompra(models.Model):
    class ProcessStatus(models.TextChoices):
        publicar = "Publicada", "Publicada"
        onway = "En camino", "En camino"
        finalized = "Finalizado", "Finalizado"
        
    productor = models.ForeignKey(Productor, on_delete=models.DO_NOTHING)
    localClient = models.ForeignKey(ComercianteLocal, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=255, choices= ProcessStatus.choices, default=ProcessStatus.publicar)
    orderDate = models.DateField(auto_now_add= True) 
    transport = models.BooleanField(default=True)
    
    