from django.db import models

# Create your models here.

class Book(models.Model):
    STATUSES = {
        (0, 'Unknown'),
        (1, 'processed'),
        (2, 'paid')


    }
    title = models.CharField(null=True, blank=False, choices=STATUSES) 
