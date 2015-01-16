from django.db import models

class Dolar(models.Model):
	fecha = models.DateField()
	precios =  models.CharField(max_length=3000)
	