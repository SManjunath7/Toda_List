from django.db import models

class Choclate(models.Model):
    name = models.CharField(max_length=100)
    price= models.FloatField()
    quantity=models.PositiveIntegerField()
    brand = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name