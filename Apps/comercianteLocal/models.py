from django.db import models
from Apps.cuentas.models import *

# Create your models here.
class BuyingOffer(models.Model):
    class ProcessStatus(models.TextChoices):
        PUBLISHED = "PUBLISHED", "Published"
        ONTRACK = "ON TRACK", "On track"
        FINISHED = "FINISHED", "Finished"
        
    producer = models.ForeignKey(Producer, on_delete=models.DO_NOTHING)
    localTrader = models.ForeignKey(LocalTrader, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=255, choices= ProcessStatus.choices, default=ProcessStatus.PUBLISHED)
    orderDate = models.DateField(auto_now_add= True) 
    transport = models.BooleanField(default=True)
    
    