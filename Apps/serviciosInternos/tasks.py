from django.conf import settings
from Apps.cuentas.models import *
from Apps.administrador.models import Contract
from Apps.productor.models import *
from datetime import datetime
from celery import shared_task
from celery.utils.log import get_task_logger
 
logger = get_task_logger(__name__)
 
@shared_task()
def check_contract_date():
    contracts = Contract.objects.all()
    if contract :
        for contract in contracts:
            if contract.endDate <= datetime.now().date():
                contract.isActive = False
                contract.save()
                if contract.type == "PRODUCER":
                    producer = Producer.objects.get(businessName=contract.companyName)
                    producer.is_active = False
                    producer.save()
                if contract.type == "INTERNATIONAL TRADER":
                    international = InternationalTrader.objects.get(businessName=contract.companyName)
                    international.is_active = False
                    international.save()
                if contract.type == "LOCAL TRADER":
                    local = LocalTrader.objects.get(businessName=contract.companyName)
                    local.is_active = False
                    local.save()
                if contract.type == "CARRIER":
                    carrier = Carrier.objects.get(businessName=contract.companyName)
                    carrier.is_active = False
                    carrier.save()
                        
                logger.info(f"The contract with {contract.companyName} is no longer active, and it will be closed soon")

            else:
                pass
    return "Done"
@shared_task()
def send_email_contract_week_before():
    contract = Contract.objects.all()
    if contract:
        for contract in contract:
            if contract.endDate-7 == datetime.now().date():
                if contract.type == "PRODUCER":
                    producer = Producer.objects.get(businessName=contract.companyName)
                    send_email_before("contract",producer)
                if contract.type == "INTERNATIONAL TRADER":
                    international = InternationalTrader.objects.get(businessName=contract.companyName)
                    send_email_before("contract",international)
                if contract.type == "LOCAL TRADER":
                    local = LocalTrader.objects.get(businessName=contract.companyName)
                    send_email_before("contract",local)
                if contract.type == "CARRIER":
                    carrier = Carrier.objects.get(businessName=contract.companyName)
                    send_email_before("contract",carrier)
                        
                logger.info(f"The contract with {contract.companyName} will expire in 1 week from now")

            else:
                pass
    return "Done"

@shared_task()
def check_postulation_date():
    bids = Bid.objects.all()
    if bids:
        for bid in bids:
            if bid.endDate <= datetime.now().date():
                offers = bid.offer_set.all()
                postulations = bids.transportpostulation_set.all()
                if offers:
                    for offer in offers:
                        offer.closed = True
                        offer.status = "REJECTED"
                if postulations:
                    for postulation in postulations:
                        postulation.closed = True
                        postulation.processStatus = "CLOSED"
                logger.info(f"The bidding process {bid.name} is no longer active")
            else:
                pass
    return "Done"
@shared_task()
def send_email_postulation_week_before():
    bids = Bid.objects.all()
    if bids:
        for bid in bids:
            if bid.endDate-7 == datetime.now().date():
                offers = bid.offer_set.all()
                postulations = bid.postulacionlicitaciontransporte_set.all()
                if offers :

                    for offer in offers:
                        producer = Producer.objects.get(id= offer.producer)
                        send_email_before("offer", producer)
                
                if postulations:
                    for postulation in postulations:
                        carrier = Carrier.objects.get(id = postulation.transportista)
                        send_email_contract_week_before("postulation", carrier)
                logger.info(f"The bidding process {bid.name} will expire in one week from now")
            else:
                pass
    return "Done"
 
def send_email_before(self,reason, user):
    subject = f"Venta {user.name} creada"
    
    message = f"Dear Mr/Ms {user.firstName} {user.lastName}:\n\n your {reason} will expire in one week from now.\nIf you want to extend your contract period, please, contact one of our executives.\n\nSincerely Feria Virtual Maipo Grande"
    lista = []
    lista.append(user.email)
    send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=lista)