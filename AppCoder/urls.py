from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("inicio/", inicio, name="Start"),

    #autenticacion de usuario
    path("registro/", registro, name="Sign Up"),
    path("login/", iniciar_sesion, name="Sign In"),
    path("logout/", LogoutView.as_view(template_name="AppCoder/autenticacion/logout.html"), name="Logout"),

    #urls primeras clases

    path("agregar_profe/", agregar_profe),
    path("ver_estudiantes/", ver_estudiantes, name="Ver Estudiantes"),
    path("ver_profes/", ver_profes, name="Ver Profesores"),
    path("ver_entregables/", ver_entregables, name="Ver Entregables"),
    #path("ver_cursos/", ver_cursos, name="Ver Cursos"),
    path("agregar_familiar/", agregar_familia),

    #crear con formulario de html
    path("crear_estudiante_html/", crear_estudiantes_html, name="Crear Estudiantes HTML"),


    #crear con form de django
    path("crear_curso/", crear_cursos, name="Crear Cursos"),
    path("crear_estudiante/", crear_estudiantes, name="Crear Estudiantes"),
    path("crear_entregable/", crear_entregables, name="Crear Entregables"),
    path("crear_profesor/", crear_profesores, name="Crear Profesores"),


    #buscar info
    path("buscar_profe/", buscar_profe, name="Buscar Profes"),
    path("resultados_busqueda/", resultadosBusqueda),

    #borrar modelos
    path("borrar_profe/<profesor_nombre>", borrar_profesor, name="Borrar Profesor"),

    #editar modelos
    path("editar_profesor/<profesor_nombre>", editar_profesor, name="Editar Profesor"),

    #CRUD basado en clases

    #CRUD de Cursos
    path("cursos/lista", CursoLista.as_view(), name = "Ver Cursos"),
    path("cursos/nuevo", CursoCrear.as_view(), name = "Crear Cursos"),
    path("cursos/borrar/<int:pk>", CursoBorrar.as_view(), name="Borrar Cursos"),
    path("cursos/editar/<int:pk>", CursoEditar.as_view(), name="Editar Cursos"),

    #CRUD de Entregables
    path("entregables/lista", EntregableLista.as_view(), name = "Ver Entregables"),
    path("entregables/nuevo", EntregableCrear.as_view(), name = "Crear Entregables"),
    path("entregables/borrar/<int:pk>", EntregableBorrar.as_view(), name="Borrar Entregables"),
    path("entregables/editar/<int:pk>", EntregableEditar.as_view(), name="Editar Entregables"),


]
