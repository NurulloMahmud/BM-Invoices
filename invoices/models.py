from django.db import models
from brokers.models import Broker
from django.contrib.auth.models import User
from datetime import date



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
    invoiced_date = models.DateField(null=True, blank=True)
    paid_date = models.DateField(null=True, blank=True)
    days_since_invoiced = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.invoice_number)
    
    def save(self, *args, **kwargs):
        # Calculate days_since_invoiced
        if self.paid_date and self.invoiced_date:
            self.days_since_invoiced = (self.paid_date - self.invoiced_date).days
        elif self.invoiced_date:
            # Calculate days_since_invoiced based on today's date
            today = date.today()
            self.days_since_invoiced = (today - self.invoiced_date).days if self.invoiced_date else None

        # Call the original save method to perform the actual save
        super(Invoice, self).save(*args, **kwargs)


class InvoiceChange(models.Model):
    field = models.CharField(max_length=100)
    old = models.CharField(max_length=100)
    new = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)