from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()
    comision = forms.IntegerField()

class EstudianteFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)  
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()


class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)  #para mensajes de texto (cadenas de caracteres) pequeños
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=40)
    edad = forms.IntegerField()

class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    fecha = forms.DateField()
    entregado = forms.BooleanField()

class RegistroFormulario(UserCreationForm):

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Correo")
    password1 = forms.CharField(label="Ingrese una contraseña:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña:",widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]