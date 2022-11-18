from django.db import models

# Create your models here.

class CrearContrato(models.Model):
    companyName = models.CharField(max_length=255, blank=True)
    initDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField(blank=True, null=True)
    archiveName = models.CharField(max_length=255, blank=True)


class VerContrato(models.Model):
    idContract = models.CharField(max_length=255, blank=True)
    companyName = models.CharField(max_length=255, blank=True)
    initDate = models.CharField(max_length=255, blank=True)
    modifyDate = models.CharField(max_length=255, blank=True)
    endDate = models.CharField(max_length=255, blank=True)
    fileName = models.CharField(max_length=255, blank=True)

class VerProcesoVentas(models.Model):
    processName = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    endDate = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    regionState = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    street = models.CharField(max_length=255, blank=True)
    postalCode = models.CharField(max_length=255, blank=True)
    detail = models.CharField(max_length=255, blank=True)
    processStatus = models.CharField(max_length=255, blank=True)

