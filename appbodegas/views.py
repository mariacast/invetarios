from django.shortcuts import render
from .models import *
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.hashers import make_password
from django.shortcuts import render , render_to_response, redirect
from django.template import RequestContext
from django.template.loader import render_to_string
from datetime import datetime, date, time, timedelta


def index(request):

    return render_to_response('index.html', context_instance = RequestContext(request))


def registro(request):
    if request.method == 'POST':
        usuario = Usuario()
        usuario.identificacion = request.POST['identificacion']
        usuario.nombres = request.POST['Nombre'].upper()
        usuario.apellidos = request.POST['Apellidos'].upper()
        usuario.save()
    return render_to_response('userRegistro.html', context_instance = RequestContext(request))

def showusers(request):
    users = Usuario.objects.all()

    return render_to_response('showusers.html',{'users':users},context_instance = RequestContext(request))
def showrecursos(request):
    recursos = Recurso.objects.all()

    return render_to_response ('showrecursos.html',{'recursos':recursos},context_instance = RequestContext(request))

def consultarrecursos(request):
    if request.method == 'POST':
        user = request.POST['id_user']
        U= Usuario.objects.get(id=user)
        list =[]
        Urecursos = RecursoUsuario.objects.filter(usuario_id=user)
        for r in Urecursos:
            recurso = Recurso.objects.get(id=r.recurso_id)
            list.append({'nombre':recurso.nombre,'categoria':recurso.categoria,'marca':recurso.marca})

        print(list)

        return render_to_response ('showconsultas.html',{'list':list,'U':U},context_instance = RequestContext(request))


def showasignacion(request):
    asignaciones = RecursoUsuario.objects.all()
    recursos = Recurso.objects.all()
    users = Usuario.objects.all()
    return render_to_response('showasignacion.html',{'recursos':recursos,'users':users},context_instance = RequestContext(request))


def showhistorial(request):
    historial = Historial.objects.all().order_by('fecha')
    list =[]
    for h in historial:

        recurso = Recurso.objects.get(id=h.recurso_id)
        usuario = Usuario.objects.get(id=h.usuario_id)
        list.append({'fecha':h.fecha,'nombre':recurso.nombre,'usuarion':usuario.nombres,'usuarioa':usuario.apellidos})


    return render_to_response('showhistorial.html',{'list':list},context_instance = RequestContext(request))
def asignar(request):
    hoy = date.today()
    ahora = datetime.now()  # Obtiene fecha
    print(ahora)

    recursos = Recurso.objects.all()
    users = Usuario.objects.all()
    if request.method == 'POST':
        asignar = RecursoUsuario()
        lol = request.POST['User']
        asignar.usuario_id = request.POST['User']
        asignar.recurso_id = request.POST['Recurso']
        asignar.save()


        historial = Historial()
        historial.fecha = ahora
        historial.recurso_id = request.POST['Recurso']
        historial.usuario_id = request.POST['User']
        historial.save()
        return HttpResponseRedirect('/showasignacion')
    return render_to_response('asignar.html',{'recursos':recursos,'users':users},context_instance = RequestContext(request))

def recursosNew(request):

    if request.method == 'POST':
       recurso = Recurso()
       recurso.nombre = request.POST['Nombre'].upper()
       recurso.categoria = request.POST['Categoria'].upper()
       recurso.codigo = request.POST['Codigo']
       recurso.marca = request.POST['Marca'].upper()
       recurso.serie = request.POST['Serie']
       recurso.save()

    return render_to_response('recursosregistro.html', context_instance = RequestContext(request))
