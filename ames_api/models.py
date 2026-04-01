from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Corsa(models.Model):
    date = models.DateField(null=True)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    derivatiopn_path = models.CharField(max_length=500, blank=True, null=True)

class Sample(models.Model):
    sampleId = models.IntegerField(primary_key=True)
    sampleName =  models.CharField(max_length=255)
    corsa = models.ForeignKey(
        Corsa, 
        on_delete=models.CASCADE, 
        related_name='samples'
    )
    
