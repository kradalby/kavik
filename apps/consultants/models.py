from django.db import models

# Create your models here.

class Consultant(models.Model):

    longUniqueTWNumber  = models.CharField(max_length=20, unique=True, primary_key=True)
    ship                = models.CharField(max_length=4)
    team                = models.CharField(max_length=2)
    number              = models.CharField(max_length=4)
    position            = models.CharField(max_length=2)
    y                   = models.CharField(max_length=1)
    firstName           = models.CharField(max_length=100)
    lastName            = models.CharField(max_length=100)
    address             = models.CharField(max_length=200)
    zipCode             = models.CharField(max_length=4)
    town                = models.CharField(max_length=50)
    country             = models.CharField(max_length=30)
    phone1              = models.CharField(max_length=8)
    phone2              = models.CharField(max_length=8)
    email               = models.EmailField()
    password            = models.CharField(max_length=100)
    y2                  = models.CharField(max_length=1)
    active              = models.BooleanField(default=False)


    def __str__(self):
        return self.number + " " + self.firstName + " " + self.lastName
