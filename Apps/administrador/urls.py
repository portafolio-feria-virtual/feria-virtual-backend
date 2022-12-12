from .views import *
from django.urls import path,include

urlpatterns = [
    path('addContract/', CreateContractView.as_view()),
    path('viewAllContract/', SeeAllContractsView.as_view()),
    path('searchContract/', SearchContractView.as_view()),
    path('seeAllBids/', SeeAllBidsView.as_view()),
    path('seeAllOffers/', SeeAllOffersView.as_view()),
    path('seeAllLocalSales/', SeeAllLocalSalesView.as_view()),
    path('editContract/', EditContractView.as_view()),
]


