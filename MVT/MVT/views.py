from http.client import HTTPResponse
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render

def inicio(request):
    return HttpResponse('Ingrese AppMVT en la URL para mirar las opciones')

def teste_template(request):
    miHtml=open('C:/Users/marjo/OneDrive/Área de Trabalho/MVT/MVT/MVT/templates/template1.html')
    plantilla=loader.get_template('template1.html')
    documento=plantilla.render()
    return HttpResponse(documento)