from django.conf.urls import patterns, include, url
from principal.views import inicio, calcularPrecioDolar
urlpatterns = patterns('',
		url(r'^$', inicio),
		url(r'^precio_dolar/$', calcularPrecioDolar, name="precio_dolar"),
)