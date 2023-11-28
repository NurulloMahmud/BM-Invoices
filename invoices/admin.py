from django.contrib import admin
from invoices.models import Status, Invoice


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'broker', 'status', 'days_since_invoiced')
    search_fields = ('invoice_number', 'broker', 'status', 'days_since_invoiced')
    list_filter = ('status', 'broker')


admin.site.register(Status)
admin.site.register(Invoice, InvoiceAdmin)