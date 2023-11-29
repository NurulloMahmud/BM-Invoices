from django.shortcuts import render, redirect
from django.views import View
from brokers.models import Status, Broker
from django.views.generic import ListView, CreateView


class BrokerCreateView(View):
    def get(self, request):
        statuses = Status.objects.all()

        return render(request, 'brokers/add_broker.html', {"statuses": statuses})
    
    def post(self, request):
        company = request.POST.get('company_name')
        postal = request.POST.get('postal')
        state = request.POST.get('state')
        mc_number = request.POST.get('mc_number')
        city = request.POST.get('city')
        phone_number = request.POST.get('phone_number')
        status = request.POST.get('selected_status')

        selected_status = Status.objects.get(name=status)
        try:
            Broker.objects.create(
                company=company,
                postal=postal,
                state=state,
                mc_number=mc_number,
                city=city,
                phone_number=phone_number,
                status=selected_status,
            )

            return redirect('brokers:brokers-list')
        except:
            return redirect('brokers:create-broker')


class BrokerListView(ListView):
    model = Broker
    template_name = 'brokers/brokers.html'
    context_object_name = 'brokers'