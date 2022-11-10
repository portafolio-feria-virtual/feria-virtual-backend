from django.db import models

# Create your models here.
class Solicitud(models.Model):
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
    initDate = models.DateTimeField(auto_now_add= True) 
    closeDate = models.DateTimeField()
