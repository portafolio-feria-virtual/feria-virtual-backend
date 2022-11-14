from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Oferta(models.Model):
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


