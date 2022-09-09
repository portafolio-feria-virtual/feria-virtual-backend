
import uuid
from django.db import models
from django.utils.text import slugify
from apps.cuentas.models import usuarios
from dateutil.relativedelta import relativedelta
import datetime

class Contrato(models.Model):
    id_contrato = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    id_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    rut_persona = models.CharField(max_length=20)
    telefono_contacto = models.CharField(max_length=25)
    fec_emision_contrato = models.DateField(default=datetime.date.today(),blank= True)
    fec_fin_contrato= models.DateField(default=datetime.date.today()+ relativedelta(years = 1), blank = True) 
    estado = models.BooleanField(default = False)



