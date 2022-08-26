from django import forms

class ContactForm(forms.Form):
    full_name=forms.CharField(max_length=50)
    email=forms.EmailField()
    phone=forms.IntegerField()
    message=forms.CharField(widget=forms.Textarea)