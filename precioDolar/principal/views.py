from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import loader, Context
from django.http import HttpResponse
from principal.models import Dolar
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render_to_response
import time
import datetime
import precioDolar
import os
import json
import urllib

def lista_precios_dolar(request):
	precioDolar = Dolar.objects.all()
	return render_to_response('lista_precios_dolar.html',{'lista':precioDolar})
	
def sobre(request):
	html = "<html><body>Proyecto de ejemplo en MDW</body></html>"
	return HttpResponse(html)
		
def calcularPrecioDolar(request):
	print 'salsa'
	service = 'https://openexchangerates.org/api/historical/'
	app_id = '55453b33e897478a9b8546b16c5c1c27'
	hoy = datetime.datetime.now()
	numeroDia = 0; 
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
	
	datos= {'precios':valoresAnterioresdolar}
	return HttpResponse(json.dumps(datos))
	
	#jsonData = demjson.encode(valoresAnterioresdolar)
		#print hace_dias.strftime("%Y-%m-%d")
		
	

	# url = service + '2015-02-02.json?' + urllib.urlencode({'app_id':'55453b33e897478a9b8546b16c5c1c27'})
	# print 'Retrieving', url
	# uh = urllib.urlopen(url)
	# data = uh.read()
	# #print data
	# try: js = json.loads(data)
	# except: js = None
	
	# item = js['rates']['COP']
	# print 'Valor', item
	
	
	
	
	
	
	
	
		# if 'status' not in js or js['status'] != 'OK':
			# print '==== Failure To Retrieve ===='
			# print data
			# continue

	#print json.dumps(js, indent=4)

		# lat = js["results"][0]["geometry"]["location"]["lat"]
		# lng = js["results"][0]["geometry"]["location"]["lng"]
		# print 'lat',lat,'lng',lng
		# location = js['results'][0]['formatted_address']
		# print location

	# url = 'https://openexchangerates.org/api/historical/2010-12-17.json?app_id=55453b33e897478a9b8546b16c5c1c27'
	# resultado = request.GET(url)
	# uh = urllib.urlopen(url)
    # data = uh.read()
    # print 'Retrieved',len(data),'characters'
	# # url = 'http://obiee.banrep.gov.co/analytics/saw.dll?wsdl'
	# # client = Client(url)
	# # idSesion =  client.service.logon("publico", "publico")
	# # #logSql = 'SELECT TRM.Fecha saw_0 FROM "Tasa Representativa del Mercado"'
	# # logSql = 'SELECT Fecha.\"Fecha (dd/mm/yyyy)\" saw_0 FROM \"Subastas\"'
	# # executionOptions={'async':False,'maxRowsPerPage':50,'refresh':True,'presentationInfo':False,'type':'Q1'}
	# # print logSql
	# # #resultado = client.service['MetadataService'].getSubjectAreas(idSesion)
	# # #resultado = client.service['MetadataService'].describeSubjectArea('Tasa Representativa del Mercado','IncludeTables',idSesion)
	# # resultado = client.service['XmlViewService'].executeSQLQuery(logSql, 'JSON',executionOptions, idSesion)
	
	# # #resultado = client.service['MetadataService'].describeTable('Tasa Representativa del Mercado', 'TRM','IncludeColumns', idSesion)
	# # hoy = datetime.datetime.now()
	# # hace_10_dias = hoy - datetime.timedelta(days=10)
	
	# # for i in resultado:
		# # print i.Row
	# # print hoy.strftime("%Y/%m/%d")
	# # print hace_10_dias.strftime("%Y/%m/%d")
	# # client.service.logoff(idSesion)	
	#return render_to_response('principal/lista_precios_dolar.html', {'fecha': hoy.strftime("%Y/%m/%d"), 'hoy':jsonData})

def inicio(request):
	precioDolar = Dolar.objects.all
	miTemplate = loader.get_template("principal/inicio.html")
	params= Dolar.objects.all()
	print params
	return HttpResponse(miTemplate.render(params))
	#return render_to_response('inicio.html', {'lista':precioDolar})
