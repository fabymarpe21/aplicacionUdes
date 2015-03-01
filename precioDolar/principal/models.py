from django.db import models
from djorm_pgarray.fields import ArrayField

class Dolar(models.Model):
	fecha = models.DateField()
	precios =  models.TextField()
	def __unicode__(self):
		return self.fecha.strftime('%Y-%m-%d')