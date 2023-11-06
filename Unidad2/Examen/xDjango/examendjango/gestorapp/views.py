from django.shortcuts import render,redirect,get_object_or_404
from gestorapp.models import Estudiante
from gestorapp.forms import EstudianteForm
from gestorapp.models import Gerentes
from gestorapp.forms import GerenteForm
# Create your views here.
def nuevoEstudiante(request):
    if request.method == 'POST':
          formaEstudiante = EstudianteForm(request.POST)
          if formaEstudiante.is_valid():
                formaEstudiante.save()
                return redirect('indexEstudiante')
    else:
            formaEstudiante= EstudianteForm()
    return render(request,'nuevoEstudiante.html',{'formaEstudiante': formaEstudiante})

def editarEstudiante(req,id):
      estudiante = get_object_or_404(Estudiante,pk=id)
      if req.method == 'POST':
        formaEstudiante = EstudianteForm(req.POST,instance=estudiante)
        if formaEstudiante.is_valid():
             formaEstudiante.save()
             return redirect('indexEstudiante')
      else:
        formaEstudiante = EstudianteForm(instance=estudiante)
      return render(req,'editarEstudiante.html',{'formaEstudiante': formaEstudiante})
def eliminarEstudiante(req,id):
     estudiante = get_object_or_404(Estudiante,pk=id)
     if estudiante:
          estudiante.delete()
     return redirect('indexEstudiante')

def detalleEstudiante(req,id):
     estudiante = get_object_or_404(Estudiante,pk=id)
     return render(req,'detalleGerente.html',{'estudiante':estudiante})

def nuevoGerente(request):
    if request.method == 'POST':
          formaGerente = GerenteForm(request.POST)
          if formaGerente.is_valid():
                formaGerente.save()
                return redirect('indexGerente')
    else:
            formaGerente= GerenteForm()
    return render(request,'nuevoGerente.html',{'formaGerente': formaGerente})

def editarGerente(req,id):
      gerente = get_object_or_404(Gerentes,pk=id)
      if req.method == 'POST':
        formaGerente = GerenteForm(req.POST,instance=gerente)
        if formaGerente.is_valid():
             formaGerente.save()
             return redirect('indexGerente')
      else:
        formaGerente = EstudianteForm(instance=gerente)
      return render(req,'editarGerente.html',{'formaGerente': formaGerente})
def eliminarGerente(req,id):
     gerente = get_object_or_404(Gerentes,pk=id)
     if gerente:
          gerente.delete()
     return redirect('indexGerente')

def detalleGerente(req,id):
     gerente = get_object_or_404(Gerentes,pk=id)
     return render(req,'detalleGerente.html',{'gerente':gerente})