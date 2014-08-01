from django.db import models

from apps.consultants.models import Consultant

# Create your models here.


class Terminal(models.Model):

    name        = models.CharField(max_length=50)
    model       = models.CharField(max_length=50)


class Reservation(models.Model):
    
    consultant  = models.ForeignKey(Consultant, null=True)
    terminal    = models.ForeignKey(Terminal)
    dateFrom    = models.DateTimeField()
    dateTo      = models.DateTimeField()
