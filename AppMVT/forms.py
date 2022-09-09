from django import forms
from django.forms import TextInput, EmailInput

class ContactForm(forms.Form):
    full_name=forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre completo', 'class': 'form-control', 'style': 'width: 246px;'}))
    email=forms.EmailField(label='Correo', widget=forms.EmailInput(attrs={'placeholder' :'Ingrese su correo electrónico', 'class': 'form-control','style': 'width: 246px;'}))
    phone=forms.IntegerField(label='Teléfono', widget=forms.NumberInput(attrs={'placeholder' :'Ingrese su teléfono', 'class': 'form-control','style': 'width: 246px;'}))
    message=forms.CharField(label='Mensaje', max_length = 300,widget=forms.Textarea(attrs={'placeholder': 'Ingrese un mensaje de hasta 300 caracteres', 'class': 'form-control','style': 'width: 246px;'}))

class LanguagesForm(forms.Form):
     language=forms.CharField(label='Lenguaje', widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre completo', 'class': 'form-control', 'style': 'width: 246px;'}))
     text=forms.CharField(label='Descripción', max_length = 600, widget=forms.Textarea(attrs={'placeholder': 'Ingrese una descripción del lenguaje', 'class': 'form-control', 'style': 'width: 246px;'}))

class AddLanguageForm(forms.Form):
     language=forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del lenguaje', 'class': 'form-control', 'style': 'width: 246px; text-align:center'}))
     text=forms.CharField(label='', max_length = 600, widget=forms.Textarea(attrs={'placeholder': 'Ingrese una descripción del lenguaje', 'class': 'form-control', 'style': 'width: 246px; text-align:center'}))

class CoursesForm(forms.Form):
     name=forms.CharField(label='',max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del curso', 'class': 'form-control', 'style': 'width: 246px; text-align:center'}))
     instituicion=forms.CharField(label='',max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Ingrese la instituición del curso', 'class': 'form-control', 'style': 'width: 246px; text-align:center'}))
     start_date=forms.DateField(label='', widget=forms.TextInput(attrs={'placeholder': 'Ingrese la fecha de início', 'class': 'form-control', 'style': 'width: 246px; text-align:center'}))

class SearchLanguageForm(forms.Form):
     language=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre del lenguaje', 'class': 'form-control text-center', 'style': 'width: 246px;'}))