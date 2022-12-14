from django.urls import path, include
from .views import *
urlpatterns = [
   # path("clase/", usersReportView.as_view()),
    #path("pdf/", usersReportPDF),
    path("usersReport/",usersReportPdfView.as_view()),
    path("contractsReport/",contractsReportPdfView.as_view()),
    path("localSalesReport/", localSalesReportPdfView.as_view()),
    
]
