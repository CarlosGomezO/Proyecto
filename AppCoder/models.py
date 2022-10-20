import email
from email.mime import image
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.




    
class Data(models.Model):
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Email: {self.email} - Phone: {self.phone} - Imagen: {self.imagen}"
    
    
    nombre = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.IntegerField()
    imagen = models.ImageField(upload_to="imagen", null=True, blank=True)
    
    
class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    
    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"
        
        

class Imagenes(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True)
    
    
    