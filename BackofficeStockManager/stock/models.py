from django.db import models

# Create your models here.


class Stock(models.Model):
    name = models.CharField(max_length=120)
    ref = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    desc = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=10)
    stock = models.DecimalField(decimal_places=0,max_digits=10)

    def __unicode__(self):
    	return self.ref
