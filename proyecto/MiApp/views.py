from django.shortcuts import render
from django.http import HttpResponse
from models import club_deportivo, profesor, alumno
from forms import club_deportivoForm, profesorForm, alumnoForm


def mostrar_index(request):
   return render(request, 'index.html')


def buscar_profesor(request):

   consulta_profesor = profesor(deporte=['deporte'], nombre=['nombre'], DNI=['DNI'])
   
   return render(request, 'consulta_profesor.html' ,{'profesor':[consulta_profesor]})



def nuevo_deporte(request):
   if request.method == 'POST':
      
      formulario_ND = club_deportivoForm(request.POST)
      
      if formulario_ND.is_valid():
         
         formulario_ND_limpio = formulario_ND.cleaned_data
         
         nuevo_profesor = club_deportivo(deporte=formulario_ND_limpio['deporte'], nombre=formulario_ND_limpio['nombre'])
         
         nuevo_profesor.save()
         
         return render(request, 'index.html')

   else:
      formulario_ND = club_deportivoForm()
      
   return render(request, 'nuevo_deporte.html', {'formulario_ND': formulario_ND})

def nuevo_profesor(request):
   if request.method == 'POST':
      
      formulario_NP = profesorForm(request.POST)
      
      if formulario_NP.is_valid():
         
         formulario_NP_limpio = formulario_NP.cleaned_data
         
         nuevo_profesor = profesor(deporte=formulario_NP_limpio['deporte'], nombre=formulario_NP_limpio['nombre'], DNI=formulario_NP_limpio['DNI'])
         
         nuevo_profesor.save()
         
         return render(request, 'index.html')

   else:
      formulario_NP = profesorForm()
      
   return render(request, 'nuevo_profesor.html', {'formulario_NP': formulario_NP})


def nuevo_alumno(request):
   if request.method == 'POST':
      
      formulario_NA = alumnoForm(request.POST)
      
      if formulario_NA.is_valid():
         
         formulario_NA_limpio = formulario_NA.cleaned_data
         
         nuevo_alumno = alumno(deporte=formulario_NA_limpio['deporte'], nombre=formulario_NA_limpio['nombre'], DNI=formulario_NA_limpio['DNI'])
         
         nuevo_alumno.save()
         
         return render(request, 'index.html')

   else:
      formulario_NA = alumnoForm()
      
   return render(request, 'nuevo_alumno.html', {'formulario_NA': formulario_NA})



