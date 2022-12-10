from django.conf import settings
from Apps.cuentas.models import *
from Apps.administrador.models import Contrato
from Apps.productor.models import *
from datetime import datetime
from celery import shared_task
from celery.utils.log import get_task_logger
 
logger = get_task_logger(__name__)
 
@shared_task()
def check_contract_date():
    contratos = Contrato.objects.all()
    if contratos :
        for contrato in contratos:
            if contrato.endDate <= datetime.now().date():
                contrato.isActive = False
                contrato.save()
                if contrato.type == "PRODUCTOR":
                    productor = Productor.objects.get(businessName=contrato.companyName)
                    productor.is_active = False
                    productor.save()
                if contrato.type == "COMERCIANTE EXTRANJERO":
                    extranjero = ComercianteExtranjero.objects.get(businessName=contrato.companyName)
                    extranjero.is_active = False
                    extranjero.save()
                if contrato.type == "COMERCIANTE LOCAL":
                    cLocal = ComercianteLocal.objects.get(businessName=contrato.companyName)
                    cLocal.is_active = False
                    cLocal.save()
                if contrato.type == "TRANSPORTISTA":
                    extranjero = Transportista.objects.get(businessName=contrato.companyName)
                    extranjero.is_active = False
                    extranjero.save()
                        
                logger.info(f"The contract with {contrato.companyName} is no longer active, and it will be closed soon")

            else:
                pass
    return "Done"
@shared_task()
def send_email_contract_week_before():
    contratos = Contrato.objects.all()
    if contratos:
        for contrato in contratos:
            if contrato.endDate-7 == datetime.now().date():
                if contrato.type == "PRODUCTOR":
                    productor = Productor.objects.get(businessName=contrato.companyName)
                    send_email_before("contract",productor)
                if contrato.type == "COMERCIANTE EXTRANJERO":
                    extranjero = ComercianteExtranjero.objects.get(businessName=contrato.companyName)
                    send_email_before("contract",extranjero)
                if contrato.type == "COMERCIANTE LOCAL":
                    cLocal = ComercianteLocal.objects.get(businessName=contrato.companyName)
                    send_email_before("contract",cLocal)
                if contrato.type == "TRANSPORTISTA":
                    transportista = Transportista.objects.get(businessName=contrato.companyName)
                    send_email_before("contract",transportista)
                        
                logger.info(f"The contract with {contrato.companyName} will expire in 1 week from now")

            else:
                pass
    return "Done"

@shared_task()
def check_postulation_date():
    licitaciones = Licitacion.objects.all()
    if licitaciones:
        for licitacion in licitaciones:
            if licitacion.endDate <= datetime.now().date():
                ofertas = licitacion.oferta_set.all()
                postulaciones = licitacion.postulacionlicitaciontransporte_set.all()
                if ofertas:
                    for oferta in ofertas:
                        oferta.closed = True
                if postulaciones:
                    for postulacion in postulaciones:
                        postulacion.closed = True
                licitacion.processStatus = "Cerrada"
                logger.info(f"The bidding process {licitacion.name} is no longer active")
            else:
                pass
    return "Done"
@shared_task()
def send_email_postulation_week_before():
    licitaciones = Licitacion.objects.all()
    if licitaciones:
        for licitacion in licitaciones:
            if licitacion.endDate-7 == datetime.now().date():
                ofertas = licitacion.oferta_set.all()
                postulaciones = licitacion.postulacionlicitaciontransporte_set.all()
                if ofertas :

                    for oferta in ofertas:
                        productor = Productor.objects.get(id= oferta.productor)
                        send_email_before("postulation", productor)
                
                if postulaciones:
                    for postulacion in postulaciones:
                        transportista = Transportista.objects.get(id = postulacion.transportista)
                        send_email_contract_week_before("postulation", transportista)
                logger.info(f"The bidding process {licitacion.name} will expire in one week from now")
            else:
                pass
    return "Done"
 
def send_email_before(self,reason, user):
    subject = f"Venta {user.name} creada"
    
    message = f"Dear Mr/Ms {user.firstName} {user.lastName}:\n\n your {reason} will expire in one week from now.\nIf you want to extend your contract period, please, contact one of our executives.\n\nSincerely Feria Virtual Maipo Grande"
    lista = []
    lista.append(user.email)
    send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=lista)