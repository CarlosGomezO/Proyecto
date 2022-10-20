from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

from AppCoder.models import Avatar, Data

class FormularioDatos(forms.ModelForm):  #relacionada a models tabla Data

    class Meta:
        model = Data
        fields = ['nombre', 'email', 'phone', 'imagen']


class UsuarioRegistro(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        
        model = User
        fields =["username", "email", "first_name","last_name", "password1", "password2"]
        
       
       
class FormularioEditar(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget=forms.PasswordInput) 
    
    class Meta:
        
        model = User
        fields =[ "email", "first_name","last_name", "password1", "password2"]
        
        
        
class ImagenesFormulario(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = [ 'user', 'imagen']
        
class AvatarFormulario(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = [ 'user', 'imagen']