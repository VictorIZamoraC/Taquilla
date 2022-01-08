from django.utils import timezone
from django.db import models

class transferRequest(models.Model):

    """ Modelo Base de Datos para Solicitar una Transferencia en el Sistema """
    
    destinyAccount = models.CharField(max_length=16)
    originAccount = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expDate = models.CharField(max_length=5)
    ammount = models.DecimalField(default=0.0, decimal_places=2, max_digits=7)
    concept = models.CharField(max_length=255)

class transferStatus(models.Model):

    """ Modelo Base de Datos para Conocer el Estado de una Transferencia """

    transactionNum = models.CharField(max_length=16)
    status = models.CharField(max_length=10)
    date = models.DateTimeField(default=timezone.now)
    ammount = models.DecimalField(default=0.0, decimal_places=2, max_digits=7)
    origin = models.CharField(max_length=4)
    destiny = models.CharField(max_length=4)
