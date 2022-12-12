from django.db import models
from Apps.cuentas.models import *
from Apps.productor.models import *

# Create your models here.
class BuyingOffer(models.Model):
    class ProcessStatus(models.TextChoices):
        PUBLISHED = "PUBLISHED", "Published"
        ONTRACK = "ON TRACK", "On track"
        FINISHED = "FINISHED", "Finished"
        
    localSale = models.ForeignKey(LocalSale, on_delete=models.DO_NOTHING, related_name="buyingoffers")
    localTrader = models.ForeignKey(LocalTrader, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=255, choices= ProcessStatus.choices, default=ProcessStatus.PUBLISHED)
    orderDate = models.DateField(auto_now_add= True) 
    quantity = models.IntegerField()
    confirmed = models.BooleanField(default=False)
    transport = models.BooleanField(default=False)
    
    