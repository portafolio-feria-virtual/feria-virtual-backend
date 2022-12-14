from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Apps.cuentas.models import *
from rest_framework.views import APIView
from .utils import render_to_pdf
from django.template import loader
from django.template.loader import render_to_string
import time
import datetime
from django.template.loader import get_template
from rest_framework import permissions
from xhtml2pdf import pisa
import pdfkit
import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from Apps.cuentas.models import * 
from Apps.administrador.models import * 
from Apps.productor.models import * 
# Create your views here.
# class usersReportView(APIView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, *args, **kwargs):
#         data = self.request.data
#         print(" zzzzzzzzzzzzzzzzzzzzzzzzzzz " + data["endDate"])
#         startDate = datetime.datetime.strptime(data["startDate"],"%d/%m/%Y")
#         endDate = datetime.datetime.strptime(data["endDate"],"%d/%m/%Y")
#         accounts = UserAccount.objects.all().filter(date_joined__range=(str(startDate),str(endDate)))
#         total = UserAccount.objects.count()
#         data = {
#             "accounts": accounts,
#             "total": total,
#             "startDate":data["startDate"],
#             "endDate":data["endDate"],
#         }
#         # template_path = 'reporteUsuarios.html'
#         # response = HttpResponse(content_type='application/pdf')
#         # response['Content-Disposition'] = 'attachment; filename="Reporte.pdf"'

#         # html = render_to_string(template_path, data)

#         # pisaStatus = pisa.CreatePDF(html, dest=response)

#         # return response 
#         print("AQUI SE ESTÁ IMPRIMIENDO LA FECHA DE INICIO" + str(startDate))
#         print(endDate)
        
        
#         pdf = render_to_pdf("reporteUsuarios.html", data)
#         return HttpResponse(pdf, content_type='application/pdf')
def link_callback(uri, rel):
            """
            Convert HTML URIs to absolute system paths so xhtml2pdf can access those
            resources
            """
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise Exception(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path



class usersReportPdfView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        data = self.request.data
        user = self.request.user
        startDate = datetime.datetime.strptime(data["startDate"],"%d/%m/%Y")
        endDate = datetime.datetime.strptime(data["endDate"],"%d/%m/%Y")
        accounts = UserAccount.objects.all().filter(date_joined__range=(str(startDate),str(endDate)))
        
        # businessNames = []
        # for acc in accounts:
        #     if acc.type == "PRODUCER":
        #         businessNames.append( Producer.objects.get(id = acc.id).businessName)
        #     if acc.type == "LOCAL TRADER":
        #         businessNames.append( LocalTrader.objects.get(id = acc.id).businessName)
        #     if acc.type == "INTERNATIONAL TRADER":
        #         businessNames.append(InternationalTrader.objects.get(id = acc.id).businessName)
        #     if acc.type == "CARRIER":
        #         businessNames.append(Carrier.objects.get(id = acc.id).businessName)
            
        total = UserAccount.objects.count()

        context = {
            "accounts": accounts,
            "total": total,
            "startDate":data["startDate"],
            "endDate":data["endDate"],
            "user":user,
            
         #   "business": businessNames,
        }
        #print(businessNames[0])
        
        template_path = 'reporteUsuarios.html'  
        
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
        # if error then show some funny view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
class contractsReportPdfView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        data = self.request.data
        user = self.request.user
        startDate = datetime.datetime.strptime(data["startDate"],"%d/%m/%Y").date()
        endDate = datetime.datetime.strptime(data["endDate"],"%d/%m/%Y").date()
        contracts = Contract.objects.all().filter(initDate__range=(str(startDate),str(endDate)))
        actives = contracts.filter(isActive=True).count()
        notActives = contracts.filter(isActive=False).count()
        
        # businessNames = []
        # for acc in accounts:
        #     if acc.type == "PRODUCER":
        #         businessNames.append( Producer.objects.get(id = acc.id).businessName)
        #     if acc.type == "LOCAL TRADER":
        #         businessNames.append( LocalTrader.objects.get(id = acc.id).businessName)
        #     if acc.type == "INTERNATIONAL TRADER":
        #         businessNames.append(InternationalTrader.objects.get(id = acc.id).businessName)
        #     if acc.type == "CARRIER":
        #         businessNames.append(Carrier.objects.get(id = acc.id).businessName)
            
        total = Contract.objects.count()

        context = {
            "contracts": contracts,
            "total": total,
            "startDate":data["startDate"],
            "endDate":data["endDate"],
            "user":user,
            "actives":actives,
            "notActives": notActives,
         #   "business": businessNames,
        }
        #print(businessNames[0])
        
        template_path = 'reporteContratos.html'  
        
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
        # if error then show some funny view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
class localSalesReportPdfView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        data = self.request.data
        user = self.request.user
        startDate = datetime.datetime.strptime(data["startDate"],"%d/%m/%Y").date()
        endDate = datetime.datetime.strptime(data["endDate"],"%d/%m/%Y").date()
        lSales = LocalSale.objects.all().filter(published__range=(str(startDate),str(endDate)))
        actives = lSales.filter(closed=False).count()
        notActives = lSales.filter(closed=True).count()
        total = LocalSale.objects.count()
        
        # businessNames = []
        # for acc in accounts:
        #     if acc.type == "PRODUCER":
        #         businessNames.append( Producer.objects.get(id = acc.id).businessName)
        #     if acc.type == "LOCAL TRADER":
        #         businessNames.append( LocalTrader.objects.get(id = acc.id).businessName)
        #     if acc.type == "INTERNATIONAL TRADER":
        #         businessNames.append(InternationalTrader.objects.get(id = acc.id).businessName)
        #     if acc.type == "CARRIER":
        #         businessNames.append(Carrier.objects.get(id = acc.id).businessName)
            
        

        context = {
            "lSales": lSales,
            "total": total,
            "startDate":data["startDate"],
            "endDate":data["endDate"],
            "user":user,
            "actives":actives,
            "notActives": notActives,
         #   "business": businessNames,
        }
        #print(businessNames[0])
        
        template_path = 'reporteVentas.html'  
        
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
        # if error then show some funny view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response