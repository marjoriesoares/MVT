from django.shortcuts import render
from AppMVT.forms import ContactForm

def inicioApp(request):
    return render(request, 'inicioApp.html')

def contactform(request):

    if request.method == 'GET':
        miFormulario = ContactForm()
        
    elif request.method == 'POST':
        miFormulario = ContactForm(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            #fromForm = {full_name:informacion[full_name], email: informacion[email]}
            #contacto = Contact(fromForm)
            #contacto.save()

            #return render()

    return render(request, 'contactform.html', {"form": miFormulario})

def portfolio(request):
    return render(request, 'portfolio.html')

def about(request):
    return render(request, 'about.html')


