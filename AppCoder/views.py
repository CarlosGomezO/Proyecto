import email
from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import * 
from AppCoder.forms import * # Imports forms djnago
from django.views.generic import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, User
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin #Login para clases
from django.contrib.auth.decorators import login_required #Login para vistas
#######


def inicioSesion(request):
    
    if request.method == "POST":
    
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password=contra)
            
            if user:
                
                login(request, user)
                
                return render(request, "AppCoder/inicio.html", {"mensaje":f"{user}"})
        
        else:
            return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos."})


    else:
        form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"formulario": form})








def registro(request):
    
    if request.method == "POST":
        
        form = UsuarioRegistro(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":"Usuario creado"})

    else:
        form = UsuarioRegistro()
    
    return render(request, "AppCoder/registro.html", {"formulario": form})








@login_required
def editarUsuario(request):
    
    usuario = request.user
    
    if request.method == "POST":
        
        form = FormularioEditar(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data
            
            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            
            usuario.save()
            
            return render(request, "AppCoder/inicio.html")
    
    else: 
        form = FormularioEditar(initial={
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name,
            
        })
    return render(request, "AppCoder/editarPerfil.html", {"formulario": form, "usuario": usuario})

                                                                             
                                         
                                         





# Create your views here.

# HTML

def inicio(request): #inicio.html  - muestra todo
    return render(request, "AppCoder/inicio.html")


def about(request): #aboutme.html  - muestra todo
    return render(request, "AppCoder/aboutme.html")









# FORMULARIO ------------------------------------------

#Formulario Forms y models 
@login_required
def formulario1(request):
    if request.method == "POST": # Si le doy al boton
        
        formulario = FormularioDatos(request.POST)
        
        if formulario.is_valid(): # comprobar que no haya errores    
            info = formulario.cleaned_data
            DataF = Data(nombre=info["nombre"], email=info["email"], phone=info["phone"], imagen=info["imagen"]) #Lee la info de las cajas de texto
            DataF.save()
            return render(request, "AppCoder/Inicio.html")
    else:
        formulario = FormularioDatos() #mostrar el formulario vacio    
    
    return render(request, "AppCoder/formu1.html", {"form1": formulario })  # Entro al ulr y me muestra una plantilla







# Busqueda Database ------------------------------------------

def busquedaDB(request):
    
    return render(request, "AppCoder/Inicio.html")

def resultados(request):
    
    if request.GET["email"]:
        
        Email = request.GET["email"]
        datos = Data.objects.filter(email__icontains=Email)
#       datos = Data.objects.filter(email__iexact=Email)
        return render(request, "AppCoder/Inicio.html", {"datos": datos,"email":Email,"datos": datos} )
    else:
        
        respuesta = "No enviaste datos."
    
    return HttpResponse(respuesta)














# -------------------------------------------------------




# CRUD con clases

def ListaData(request):
    data = Data.objects.all()

    return render (request, "AppCoder/data_list.html", {"data": data })
    
class DetalleData(LoginRequiredMixin, DetailView):
    model = Data
    

class CrearData(LoginRequiredMixin, CreateView):
    model = Data
    success_url = "/AppCoder/data/list"
    fields = ["nombre", "email", "phone", "imagen" ]



class ActualizarData(LoginRequiredMixin, UpdateView):
    model = Data
    success_url = "/AppCoder/data/list"
    fields = ["nombre", "email", "phone", "imagen" ]



class BorrarData(LoginRequiredMixin, DeleteView):
    model = Data
    success_url = "/AppCoder/data/list"
    fields = ["nombre", "email", "phone", "imagen" ]
    
    
    
    
    ########################################
    
    
@login_required
def agregarAvatar(request):
    
    if request.method=="POST":
        form = AvatarFormulario(request.POST, request.FILES)
        
        


@login_required
def agregarImagen(request):
    
    if request.method=="POST": #presionar el boton
        
        miFormulario = ImagenesFormulario(request.POST, request.FILES)
        
        if miFormulario.is_valid(): # comprobar que no haya errores    
            
            info = miFormulario.cleaned_data
            
           # avatar = Imagenes(user=request.user, imagen=info['imagen'])
            avatar = Imagenes(user=info['user'], imagen=info['imagen'])

            avatar.save()
            
            return render(request, "AppCoder/Inicio.html")
    else:
        miFormulario = ImagenesFormulario() #mostrar el formulario vacio    
    
    return render(request, "AppCoder/AgregarIMG.html", {"form": miFormulario })  # Entro al ulr y me muestra una plantilla


