from django.db import models
from brokers.models import Broker
from django.contrib.auth.models import User



class Status(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name


class Invoice(models.Model):
    invoice_number = models.BigIntegerField()
    reference = models.CharField(max_length=250)
    broker = models.ForeignKey(Broker, on_delete=models.SET_NULL, null=True, blank=True)
    pick_up = models.DateField()
    delivery = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.CharField(max_length=255)
    last_update = models.DateField()
    days_since_invoiced = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.invoice_number)


class InvoiceChange(models.Model):
    field = models.CharField(max_length=100)
    old = models.CharField(max_length=100)
    new = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)