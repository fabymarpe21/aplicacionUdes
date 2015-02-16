from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import loader, Context
from django.http import HttpResponse
from principal.models import Dolar
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render_to_response
import MySQLdb
from django.db import connection
import time
import datetime
import precioDolar
import os
import json
import urllib
	
def calcularPrecioDolar(request):
	service = 'https://openexchangerates.org/api/historical/'
	app_id = '55453b33e897478a9b8546b16c5c1c27'
	hoy = datetime.datetime.now()
	consulta = "SELECT * FROM principal_dolar where fecha='"
	consulta += hoy.strftime("%Y/%m/%d")
	consulta += "'"
	print consulta
	cursor = connection.cursor()
	print '2'
	cursor.execute(consulta)
	print '3'
	names = cursor.fetchall()
	numeroDia = 0
	valoresAnterioresdolar = []
	while numeroDia < 10:
		hace_dias = hoy - datetime.timedelta(days=numeroDia)
		print service
		url = service + hace_dias.strftime("%Y-%m-%d") +'.json?' + urllib.urlencode({'app_id': app_id})
		print 'URL', url
		uh = urllib.urlopen(url)
		data = uh.read()
		js = json.loads(data)
		item = js['rates']['COP']
		valoresAnterioresdolar.append({"fecha":hace_dias.strftime("%Y/%m/%d"), 'valorDolar':item})
		numeroDia += 1
	datos = {'precios':valoresAnterioresdolar}
	if(len(names)==0): 
		dolar = Dolar(precios=valoresAnterioresdolar)
		dolar.save()  
	return HttpResponse(json.dumps(datos))
	
def inicio(request):
	precioDolar = Dolar.objects.all()
	return render_to_response('principal/inicio.html',{'lista':precioDolar})
