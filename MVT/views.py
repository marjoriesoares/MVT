from django.http import HttpResponse
from django.shortcuts import render, redirect

def inicio(request):
    return redirect('/AppMVT')