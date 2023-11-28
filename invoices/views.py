from django.shortcuts import render
from django.views.generic import ListView
from invoices.models import Invoice


class InvoiceListView(ListView):
    queryset = Invoice.objects.all().order_by('status__pk')
    context_object_name = 'invoices'
    template_name = 'invoices/invoice_list.html'