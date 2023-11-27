from django.db import models



class Status(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
    

class Broker(models.Model):
    company = models.CharField(max_length=150, null=False, blank=False)
    postal = models.BigIntegerField(null=False, blank=False)
    state = models.CharField(max_length=50, null=False, blank=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=False, blank=False)
    mc_number = models.BigIntegerField(null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self) -> str:
        return self.company