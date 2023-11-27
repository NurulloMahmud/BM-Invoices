from django.contrib import admin
from brokers.models import Status, Broker


class StatusAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)

class BrokerAdmin(admin.ModelAdmin):
    search_fields = ('company', 'postal', 'state', 'mc_number')
    list_display = ('company', 'mc_number')
    list_filter = ('state', 'status')


admin.site.register(Status, StatusAdmin)
admin.site.register(Broker, BrokerAdmin)