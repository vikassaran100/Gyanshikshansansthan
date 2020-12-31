from os import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=122)
    Child = models.CharField(max_length=70)
    Phone = models.CharField(max_length=12, default='DEFAULT VALUE')
    date = models.DateField()

    def __str__(self):
        return self.Name
    