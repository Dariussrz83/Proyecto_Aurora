from django.db import models

class Frozen_cakes(models.Model):
    name = models.CharField(max_length= 100)
    price = models.FloatField()
    stock = models.BooleanField()
    
    
class Birthday_cakes(models.Model):
    name = models.CharField(max_length= 50)
    price = models.FloatField()
    stock = models.BooleanField()
    
    
class Alfajores(models.Model):
    name = models.CharField (max_length=50)
    price = models.FloatField()
    stock = models.BooleanField()