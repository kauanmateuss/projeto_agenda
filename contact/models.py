from django.db import models

from django.utils import timezone

# Create your models here.

# Criando o model categoria (ForeygnKey)
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    pincture = models.ImageField(blank=True, upload_to='pinctures/%Y/%m/')

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null =True)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"