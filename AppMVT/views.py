from django.shortcuts import render, redirect
from AppMVT.forms import ContactForm, LanguagesForm, CoursesForm
from AppMVT.models import Contact, Languages, Courses
from django.http import HttpResponse, HttpResponseRedirect


def inicioApp(request):
    return render(request, "AppMVT/inicioApp.html")

def courses(request):
    courses=Courses.objects.all()
    return render(
        request, "AppMVT/courses.html", {"courses": courses})
    

def addcourses(request):
    if request.method == 'POST':
        myform = CoursesForm(request.POST)
        if myform.is_valid():
            info = myform.cleaned_data
            course=Courses(name=info['name'],instituicion=info['instituicion'], start_date=info['start_date'])
            course.save()
            return render(request, 'AppMVT/courses.html')
        else:
            return render(request, 'AppMVT/addcourses.html')
    else:
        myform = CoursesForm()
    return render(request,'AppMVT/addcourses.html', {'myform':myform})

def languages(request, language=False):
    if language:
        try:
            lang = Languages.objects.get(language=language)
            return render(
                request,
                'AppMVT/languages.html',
                {'language': lang.language, 'text': lang.text}
                 )
        except:
            return render(request, 'AppMVT/languages.html', 
            {"mensaje": "Lenguaje no identificada. Asegúrese de poner las letras mayúsculas y minúsculas."} )
    else:
        return render(request,'AppMVT/languages.html')

def searchlanguages(request):
    if request.GET["language"]:
        language=request.GET["language"]
        return redirect(languages, language=language)
    else:
        return render(request, 'AppMVT/languages.html', {"mensaje": "No enviaste datos!"} )


def about(request):
    return render(request, 'AppMVT/about.html')

def contactform(request):
    if request.method == 'POST':
        myform = ContactForm(request.POST)
        if myform.is_valid():
            info = myform.cleaned_data
            contact=Contact(full_name=info['full_name'],email=info['email'], phone=info['phone'], message=info['message'])
            contact.save()
            return render(request, 'AppMVT/inicioApp.html')
        else:
            return render(request, 'AppMVT/contactform.html')
    else:
        myform = ContactForm()
        return render(request,'AppMVT/contactform.html', {'contactform':myform})