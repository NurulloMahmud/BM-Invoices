from django.urls import path
from invoices.views import InvoiceListView, InvoiceCreateView


app_name = "invoices"
urlpatterns = [
    path('all/', InvoiceListView.as_view(), name='invoices-list'),
    path('create/', InvoiceCreateView.as_view(), name='create-invoice')    
]