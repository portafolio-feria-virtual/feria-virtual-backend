from django.db import models

# Create your models here.

class Oferta(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=255, blank=True)
    productorDescription = models.TextField(blank=255, blank=True)
    offer = models.BooleanField(default=False)
    unitPrice = models.IntegerField()
    adminArchives = models.CharField(max_length=255, blank=True)
    techArchives = models.CharField(max_length=255, blank=True)
    economicArchives = models.CharField(max_length=255, blank=True)
