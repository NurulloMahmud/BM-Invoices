
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def landing_page(request):
    return render(request, 'base.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='home'),
    path('users/', include('users.urls')),
    path('brokers/', include('brokers.urls')),
    path('invoices/', include('invoices.urls')),
]
