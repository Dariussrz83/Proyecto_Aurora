from django.db import models

class Frozen_cakes(models.Model):
    name = models.CharField(max_length= 100)
    price = models.FloatField()
    stock = models.BooleanField()