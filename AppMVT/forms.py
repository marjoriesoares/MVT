from django import forms
from django.forms import TextInput, EmailInput

class ContactForm(forms.Form):
    Nombre=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre completo', 'style': 'width: 246px;'}))
    Email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Ingrese su correo electrónico', 'style': 'width: 246px;'}))
    Teléfono=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder' :'Ingrese su teléfono', 'style': 'width: 246px;'}))
    Mensaje=forms.CharField(max_length = 300,widget=forms.Textarea(attrs={'placeholder': 'Ingrese un mensaje de hasta 300 caracteres', 'style': 'width: 246px;'}))