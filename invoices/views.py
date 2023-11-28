from django.shortcuts import render, redirect
from django.views.generic import ListView
from invoices.models import Invoice
from django.views import View
from brokers.models import Broker
from invoices.models import Status



class InvoiceListView(ListView):
    queryset = Invoice.objects.all().order_by('status__pk')
    context_object_name = 'invoices'
    template_name = 'invoices/invoice_list.html'

class InvoiceCreateView(View):
    def get(self, request):
        statuses = Status.objects.all()
        brokers = Broker.objects.all()

        context = {
            "brokers": brokers,
            "statuses": statuses,
        }

        return render(request, 'invoices/create_invoice.html', context)
    
    def post(self, request):
        invoice_number = request.POST.get('invoice_number')
        reference = request.POST.get('reference')
        broker = request.POST.get('broker')
        pick_up = request.POST.get('pick_up')
        delivery = request.POST.get('delivery')
        amount = request.POST.get('amount')
        status = request.POST.get('selected_status')
        comment = request.POST.get('comment')
        # last_update = request.POST.get('last_update')
        # days_since_invoiced = request.POST.get('days_since_invoiced')

        Invoice.objects.create(
            invoice_number=invoice_number,
            reference=reference,
            broker=broker,
            pick_up=pick_up,
            delivery=delivery,
            amount=amount,
            status=status,
            comment=comment,
            # last_update=last_update,
            # days_since_invoiced=days_since_invoiced,
        )

        return redirect('invoices:invoices-list')