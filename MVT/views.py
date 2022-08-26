from http.client import HTTPResponse
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render, redirect

def inicio(request):
    return redirect('/AppMVT')

def appMVT(request):
    return render(request, 'inicio.html')