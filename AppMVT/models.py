from django.db import models

class Contact(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.CharField(max_length=400)
