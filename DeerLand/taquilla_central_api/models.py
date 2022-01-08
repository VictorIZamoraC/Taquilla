from django.db import models
from django.utils import timezone

# Create your models here.

class passesBoxOffice(models.Model):

    passName = models.CharField(max_length=120)
    passDescription = models.TextField()
    passPrice = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    passAvailability = models.PositiveIntegerField()

class passesSold(models.Model):
    
    idTransaction = models.CharField(max_length=16)
    account = models.CharField(max_length=4)
    date = models.DateField(default=timezone.now)
    customerName = models.CharField(max_length=255)
    passName = models.CharField(max_length=120)
    ammount = models.DecimalField(default=0.0, decimal_places=2, max_digits=7)