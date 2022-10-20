from django.contrib import admin
from django.urls import path
from AppCoder import views
from AppCoder.views import *
from django.contrib.auth.views import LogoutView
###########





urlpatterns = [
    
    path("",inicio, name="beginning"),
    
    
    path("formu1/", formulario1, name = "FormularioDatos"),
    path("busquedaDB/", busquedaDB, name= "email"),
    path("resultados/", resultados, name= "ResultadosBusqueda"),
    path("aboutme/", about, name= "AboutMe"),
    #Crud de Data usando Clases
    
    path("data/list/", views.ListaData, name="DataLeer"),
    path("data/<int:pk>", DetalleData.as_view(), name="DataDetalle"),
    path("data/crear/", CrearData.as_view(), name="DataCrear"),
    path("data/editar/<int:pk>/", ActualizarData.as_view(), name="DataEditar"),
    path("data/borrar/<int:pk>/", BorrarData.as_view(), name="DataBorrar"),
    
    #Login
    path("accounts/login/", inicioSesion, name="Login"),
    
    #Registro
    path("accounts/singup/", registro, name="SignUp"),

    #Logout
    path("logout/", LogoutView.as_view(template_name= "AppCoder/logout.html"), name="Logout"),



    #EditarUser
    path("accounts/profile/", editarUsuario, name="EditarUsuario"),

    #Subir Imagenes
    path("agregarImagen/", views.agregarImagen, name="AgregarImagen"),





]




