from django.db import models
from djorm_pgarray.fields import ArrayField

class Dolar(models.Model):
	fecha = models.DateTimeField(auto_now=True)
	precios =  models.CharField(max_length=500)
	