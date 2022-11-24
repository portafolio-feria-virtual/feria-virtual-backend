from django.db import models

# Create your models here.

class Contrato(models.Model):
    companyName = models.CharField(max_length=255, blank=True)
    initDate = models.DateField(auto_now_add=True)
    modifyDate = models.DateField(auto_now=True)
    endDate = models.DateField(blank=True, null=True)
    fileName = models.CharField(max_length=255, blank=True)

