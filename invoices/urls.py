from django.urls import path
from invoices.views import InvoiceListView


app_name = "invoices"
urlpatterns = [
    path('all/', InvoiceListView.as_view(), name='invoices-list'),
    
]