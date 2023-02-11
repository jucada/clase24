from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):

    return render(request, "AppCoder/inicio.html")

def registro(request):

    if request.method == "POST":

        miFormulario = RegistroFormulario(request.POST) #obtener los datos que están en el formulario
    
        if miFormulario.is_valid():

            miFormulario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = RegistroFormulario()
    
    return render(request, "AppCoder/autenticacion/registro.html", {"formulario1":miFormulario})


def iniciar_sesion(request):

    if request.method == "POST":

        miFormulario = AuthenticationForm(request, data = request.POST) #obtener los datos que están en el formulario
    
        if miFormulario.is_valid():
            

            usuario = miFormulario.cleaned_data.get("username") #obteniendo el usuario y la contra ingresados
            contra = miFormulario.cleaned_data.get("password")

            miUsuario = authenticate(username=usuario, password=contra) #autentica que los datos de inicio sean correctos

            if miUsuario:

                login(request, miUsuario)
                mensaje = f"{miUsuario}"

                return render(request, "AppCoder/inicio.html", {"mensaje":mensaje})

        else:

            mensaje = f"Error. Ingresaste mal los datos."

            return render(request, "AppCoder/inicio.html", {"mensaje":mensaje})

    else:

        miFormulario = AuthenticationForm()
    
    return render(request, "AppCoder/autenticacion/login.html", {"formulario1":miFormulario})









def agregar_profe(request):

    profe1 = Profesor(nombre="Pepe", apellido="Perez", email = "pepe@perez.la", profesion="Desarrollador de Apps", edad=25)
    profe1.save()

    return HttpResponse(f"Hemos creado al profesor {profe1.nombre} a la base de datos.")

def agregar_familia(request):

    familiar1 = Familiar(parentesco="hermano",nombre="Pepe",edad=30, fecha="2023-01-26")
    familiar1.save()

    return HttpResponse(f"Hemos agregado a la base de datos el familiar {familiar1.nombre}.")

def ver_estudiantes(request):

    listaEstudiantes = Estudiante.objects.all()

    return render(request, "AppCoder/verEstudiantes.html", {"lista":listaEstudiantes})

def ver_profes(request):

    listaProfes = Profesor.objects.all()

    return render(request, "AppCoder/verProfesores.html", {"listaProfes":listaProfes})

def ver_entregables(request):

    return render(request, "AppCoder/verEntregables.html")

def ver_cursos(request):

    return render(request, "AppCoder/verCursos.html")


def crear_estudiantes_html(request): #crear usando forms de HTML

    if request.method == 'POST':
      
            estudiante1 =  Estudiante(nombre = request.POST['nombre'], 
                                apellido = request.POST['apellido'], 
                                email = request.POST['email'])
 
            estudiante1.save()
 
            return render(request, "AppCoder/inicio.html")

    return render(request, "AppCoder/crearEstudiantes.html")

def crear_cursos(request): #Crear usando forms de django

    if request.method == 'POST': #click al botón enviar: guardarse los datos y crearse el curso 

        miFormulario = CursoFormulario(request.POST) #obtener los datos que están en el formulario

        if miFormulario.is_valid(): #validar que los datos estén ok

            infoDict = miFormulario.cleaned_data #la info del formulario se pasa a tipo diccionario

            curso1 = Curso(nombre = infoDict["nombre"], camada = infoDict["camada"], comision=infoDict["comision"] )

            curso1.save()

            return render(request, "AppCoder/inicio.html")

    else: #si todavia no le doy click

        miFormulario = CursoFormulario()
    

    return render(request, "AppCoder/crearCursos.html", {"formulario1":miFormulario})


#Función para crear estudiantes
def crear_estudiantes(request): #Crear usando forms de django

    if request.method == 'POST': #click al botón enviar: guardarse los datos y crearse el curso 

        miFormulario = EstudianteFormulario(request.POST)

        if miFormulario.is_valid(): #validar que los datos estén ok

            infoDict = miFormulario.cleaned_data #la info del formulario se pasa a tipo diccionario

            estudiante1 = Estudiante(nombre = infoDict["nombre"], apellido = infoDict["apellido"], email = infoDict["email"] )

            estudiante1.save()

            return render(request, "AppCoder/inicio.html")

    else: #si todavia no le doy click

        miFormulario = EstudianteFormulario()
    

    return render(request, "AppCoder/nuevoEstudiante.html", {"formulario1":miFormulario})

#Función para crear estudiantes
def crear_entregables(request): #Crear usando forms de django

    if request.method == 'POST': #click al botón enviar: guardarse los datos y crearse el curso 

        miFormulario = EntregableFormulario(request.POST)

        if miFormulario.is_valid(): #validar que los datos estén ok

            infoDict = miFormulario.cleaned_data #la info del formulario se pasa a tipo diccionario
            entregable1 = Entregable(nombre = infoDict["nombre"], fecha = infoDict["fecha"], entregado = infoDict["entregado"] )

            entregable1.save()

            return render(request, "AppCoder/inicio.html")

    else: #si todavia no le doy click

        miFormulario = EntregableFormulario()
    

    return render(request, "AppCoder/nuevoEntregable.html", {"formulario1":miFormulario})

#Función para crear profesores
def crear_profesores(request): #Crear usando forms de django

    if request.method == 'POST': #click al botón enviar: guardarse los datos y crearse el curso 

        miFormulario = ProfesorFormulario(request.POST)

        if miFormulario.is_valid(): #validar que los datos estén ok

            infoDict = miFormulario.cleaned_data #la info del formulario se pasa a tipo diccionario
            profe1 = Profesor(nombre = infoDict["nombre"], apellido = infoDict["apellido"], 
                              email = infoDict["email"], profesion = infoDict["profesion"], 
                              edad = infoDict["edad"] )

            profe1.save()

            return render(request, "AppCoder/inicio.html")

    else: #si todavia no le doy click

        miFormulario = ProfesorFormulario()
    

    return render(request, "AppCoder/nuevoProfesor.html", {"formulario1":miFormulario})


def buscar_profe(request):

    return render(request, "AppCoder/busquedaProfe.html")

def resultadosBusqueda(request):

    if request.method == "GET":

        profesionBusqueda = request.GET["profesion"]
        profesResultados = Profesor.objects.filter(profesion__icontains=profesionBusqueda)

        return render(request, "AppCoder/resultadosBusqueda.html", {"profesion":profesionBusqueda, "resultado":profesResultados})

    return render(request, "AppCoder/resultadosBusqueda.html")


def borrar_profesor(request, profesor_nombre):

    profesor_elegido = Profesor.objects.get(nombre=profesor_nombre)
    profesor_elegido.delete()

    return render(request, "AppCoder/inicio.html")


def editar_profesor(request, profesor_nombre):

    profesor_elegido = Profesor.objects.get(nombre=profesor_nombre)

    #print(profesor_elegido)

    if request.method == 'POST': #click al botón editar:editar los datos del profesor 

        miFormulario = ProfesorFormulario(request.POST) #tener los datos del profe

        if miFormulario.is_valid(): #validar que los datos estén ok

            infoDict = miFormulario.cleaned_data #la info del formulario se pasa a tipo diccionario

            #print(infoDict)

            profesor_elegido.nombre = infoDict["nombre"]
            profesor_elegido.apellido = infoDict["apellido"]
            profesor_elegido.email = infoDict["email"]
            profesor_elegido.profesion = infoDict["profesion"]
            profesor_elegido.edad = infoDict["edad"]
            
            profesor_elegido.save()

            return render(request, "AppCoder/inicio.html")

    else: #si todavia no le doy click

        miFormulario = ProfesorFormulario(initial={"nombre":profesor_elegido.nombre,
                                                    "apellido":profesor_elegido.apellido,
                                                    "email":profesor_elegido.email,
                                                    "profesion":profesor_elegido.profesion,
                                                    "edad":profesor_elegido.edad})
    

    return render(request, "AppCoder/editarProfesor.html", {"formulario1":miFormulario})

#CRUD de Cursos con vistas basadas en clases
class CursoLista(ListView): #por defecto el template name se llama curso_list.html
    model = Curso
    template_name = "AppCoder/cursos/curso_list.html"
    
class CursoCrear(LoginRequiredMixin, CreateView): #por defecto el template name se llama curso_form.html
    model = Curso
    fields = ["nombre", "camada", "comision"]
    success_url = "/AppCoder/cursos/lista"
    template_name = "AppCoder/cursos/curso_form.html"

class CursoBorrar(LoginRequiredMixin, DeleteView): #por defecto el template name se llama curso_confirm_delete.html
    model = Curso
    success_url = "/AppCoder/cursos/lista"
    template_name = "AppCoder/cursos/curso_borrar.html"

class CursoEditar(LoginRequiredMixin, UpdateView): #usa el mismo html que el CreateView (curso_form.html)
    model = Curso
    fields = ["nombre", "camada", "comision"]
    success_url = "/AppCoder/cursos/lista"
    template_name = "AppCoder/cursos/curso_form.html"

#CRUD de Cursos con vistas basadas en clases

class EntregableLista(ListView): #por defecto se llama entregable_list.html
    model = Entregable
    template_name = "AppCoder/entregas/entregable_list.html"

class EntregableCrear(CreateView): #por defecto el template name se llama entregable_form.html
    model = Entregable
    fields = ["nombre", "fecha", "entregado"]
    success_url = "/AppCoder/entregables/lista"
    template_name = "AppCoder/entregas/entregable_form.html"

class EntregableBorrar(DeleteView): #por defecto el template name se llama entregable_confirm_delete.html
    model = Entregable
    success_url = "/AppCoder/entregables/lista"
    template_name = "AppCoder/entregas/entregable_confirm_delete.html"

class EntregableEditar(UpdateView): #usa el mismo html que el CreateView (entregable_form.html)
    model = Entregable
    fields = ["nombre", "fecha", "entregado"]
    success_url = "/AppCoder/entregables/lista"
    template_name = "AppCoder/entregas/entregable_form.html"
