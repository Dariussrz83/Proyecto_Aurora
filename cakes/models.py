from django.db import models

class Frozen_cakes(models.Model):
    name = models.CharField(max_length= 100)
    price = models.FloatField(blank=False)
    stock = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Frozen Cake'
        verbose_name_plural = 'Frozen Cakes'
    
    
class Birthday_cakes(models.Model):
    name = models.CharField(max_length= 50)
    price = models.FloatField()
    stock = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Birthday Cake'
        verbose_name_plural ='Birthday Cakes'
    
    
    
    
class Alfajores(models.Model):
    name = models.CharField (max_length=50)
    price = models.FloatField()
    stock = models.BooleanField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Alfajor'
        verbose_name_plural = 'Alfajores'