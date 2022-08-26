from http.client import HTTPResponse
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def appMVT(request):
    return render(request, 'inicio.html')