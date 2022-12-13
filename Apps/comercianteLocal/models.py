from django.db import models
from Apps.cuentas.models import *
from Apps.productor.models import *

# Create your models here.
class BuyingOffer(models.Model):
    class ProcessStatus(models.TextChoices):
        PUBLISHED = "PUBLISHED", "Published"
        ONTRACK = "ON TRACK", "On track"
        REJECTED = "REJECTED", "Rejected"
        ACCEPTED = "ACCEPTED", "Accepted"
        FINISHED = "FINISHED", "Finished"
        
    localSale = models.ForeignKey(LocalSale, on_delete=models.DO_NOTHING, related_name="buyingoffers")
    localTrader = models.ForeignKey(LocalTrader, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=255, choices= ProcessStatus.choices, default=ProcessStatus.PUBLISHED)
    orderDate = models.DateField(auto_now_add= True) 
    editable = models.BooleanField(default=True)
    quantity = models.IntegerField()
    confirmed = models.BooleanField(default=False)
    
@receiver(post_save, sender= BuyingOffer)
def afterCreateMail(instance=None, created= False, **kwargs):
    if created:
            try:
                lSale = LocalSale.objects.get(id = instance.localSale)
                subject = f"Sale offer to {lSale.name} published"
                lTrader = LocalTrader.objects.get(id = instance.localTrader.id)
                message = f"Dear Mr/Ms {lTrader.firstName} {lTrader.lastName}:\n\nYour offer to {lSale.name} has been published.\nYou will be notified on any change.\n\nsincerely. Feria Virtual Maipo Grande"
                lista = []
                lista.append(lTrader.email)
                send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=lista)
            except:
                pass

