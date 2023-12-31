from django.shortcuts import render, redirect
from django.views.generic import ListView
from invoices.models import Invoice, InvoiceChangeHistory
from django.views import View
from brokers.models import Broker
from invoices.models import Status
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.http import JsonResponse



class InvoiceListView(ListView):
    queryset = Invoice.objects.all().order_by('status__pk')
    context_object_name = 'invoices'
    template_name = 'invoices/invoice_list.html'

class InvoiceCreateView(View):
    def get(self, request):
        statuses = Status.objects.all()
        brokers = Broker.objects.all()
        broker_names = [broker.company for broker in brokers]

        context = {
            "brokers": brokers,
            "statuses": statuses,
            'broker_names': broker_names
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


class InvoiceStatusChangeView(View):
    def get(self, request, pk, status):
        invoice_instance = get_object_or_404(Invoice, pk=pk)
        status_instance = Status.objects.get(name=status)
        old_status = invoice_instance.status
        invoice_instance.status=status_instance

        # record invoiced date if the status invoice is changed to invoiced
        invoice_instance.invoiced_date = timezone.now().date() if status_instance.name == 'Invoiced' else invoice_instance.invoiced_date

        # record paid date if the status is changed to paid
        if status_instance.name == 'Paid':
            invoice_instance.paid_date = timezone.now().date()

            try:
                invoice_instance.days_since_invoiced = timezone.now().date() - invoice_instance.invoiced_date
            except:
                invoice_instance.days_since_invoiced = 0

        # save all changes
        invoice_instance.save()

        # record the change in history
        InvoiceChangeHistory.objects.create(
            field='Status',
            old=old_status,
            new=invoice_instance.status,
            user=request.user,
            invoice=invoice_instance,
        )

        previous_url = request.META.get('HTTP_REFERER')
        try:
            return redirect(previous_url)
        except:
            return redirect('invoices:invoices-list')       


class InvoiceCommentView(View):
    def get(self, request, pk):
        invoice_instance = get_object_or_404(Invoice, pk=pk)
        return render(request, 'invoices/add_comment.html', {"comment": invoice_instance.comment})
    
    def post(self, request, pk):
        invoice_instance = get_object_or_404(Invoice, pk=pk)
        comment = request.POST.get('comment')
        old_comment = invoice_instance.comment
        invoice_instance.comment=comment
        invoice_instance.save()

        # record comment change in history model
        InvoiceChangeHistory.objects.create(
            field='Comment',
            old=old_comment,
            new=invoice_instance.comment,
            user=request.user,
            invoice=invoice_instance,
        )

        return redirect('invoices:invoices-list')
    

class InvoiceDetailView(View):
    def get(self, request, pk):
        invoice_instance = get_object_or_404(Invoice, pk=pk)

        history = InvoiceChangeHistory.objects.filter(invoice=invoice_instance).all()

        context = {
            "invoice": invoice_instance,
            "history": history,
        }

        return render(request, 'invoices/invoice_detail.html', context)


class GetBrokerForInvoice(View):
    def get(self, request):
        query = request.GET.get('broker', '')
        options = Broker.objects.filter(company__icontains=query)
        result = [option.company for option in options]
        return JsonResponse(result, safe=False)


class InvoiceCreateView(View):
    def get(self, request):
        return render(request, 'invoices/create_invoice.html')
    
    def post(self, request):
        invoice_number = request.POST.get('invoice_number')
        reference = request.POST.get('reference')
        broker = request.POST.get('broker')
        pick_up = request.POST.get('pick_up')
        delivery = request.POST.get('delivery')
        amount = request.POST.get('amount')
        comment = request.POST.get('comment')

        broker = Broker.objects.get(company=broker)
        status = Status.objects.get(name='Missing paperwork')

        Invoice.objects.create(
            invoice_number=invoice_number,
            reference=reference,
            broker=broker,
            pick_up=pick_up,
            delivery=delivery,
            amount=amount,
            comment=comment,
            status=status,
            last_update=timezone.now().date(),
        )

        return redirect('invoices:invoices-list')