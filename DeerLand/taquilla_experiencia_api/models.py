from django.db import models
from django.utils import timezone

class registerCustomer(models.Model):

    clientCode = models.CharField(max_length=50)

class promotionsBoxOffice(models.Model):

    idPass = models.CharField(max_length=50)
    discount = models.CharField(max_length=3)
    expDate = models.DateField(default=timezone.now)