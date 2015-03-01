import datetime
from suds.client import Client
from principal.models import Dolar
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

def lista_precios_dolar(request):
	precioDolar = Dolar.objects.all()
	return render_to_response('lista_precios_dolar.html',{'lista':precioDolar})
	
def sobre(request):
	html = "<html><body>Proyecto de ejemplo en MDW</body></html>"
	return HttpResponse(html)
		
def calcularPrecioDolar(request):
	url = 'http://obiee.banrep.gov.co/analytics/saw.dll?wsdl'
	client = Client(url)
	#print client
	idSesion =  client.service.logon("publico", "publico")
	logSql='SELECT TRM.Fecha saw_0 FROM "Tasa Representativa del Mercado"'
	executionOptions={'async':False,'maxRowsPerPage':50,'refresh':True,'presentationInfo':False,'type':'Q1'}

	#resultado = client.service['MetadataService'].getSubjectAreas(idSesion)
	#resultado = client.service['MetadataService'].describeSubjectArea('Tasa Representativa del Mercado','IncludeTables',idSesion)
	resultado = client.service['XmlViewService'].executeSQLQuery(logSql, 'JSon',executionOptions, idSesion)
	
	#resultado = client.service['MetadataService'].describeTable('Tasa Representativa del Mercado', 'TRM','IncludeColumns', idSesion)
	hoy = datetime.datetime.now().strftime("%Y/%m/%d")
	print hoy
	client.service.logoff(idSesion)
	return render_to_response('lista_precios_dolar.html', {'hoy':resultado})
	
def inicio(request):
	print('entro')
	precioDolar = Dolar.objects.all()
	return render_to_response('inicio.html', {'lista':precioDolar})
