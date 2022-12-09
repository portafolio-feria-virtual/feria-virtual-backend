from django.conf import settings
from django.contrib.auth.models import User
from Apps.administrador.models import Contrato
from datetime import datetime
from celery import shared_task
from celery.utils.log import get_task_logger
 
logger = get_task_logger(__name__)
 
@shared_task()
def check_contract_date():
    contratos = Contrato.objects.all()
    for contrato in contratos:
        if contrato.endDate <= datetime.now().date():
            logger.info(f"el contrato con {contrato.companyName} no está vigente")
        else:
            logger.info(f"el contrato con {contrato.companyName} SIII está vigente")
    return "Done"
 
