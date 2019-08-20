from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import Libro

# Create your views here.

def cargar_inicio(request):
    return render(request, "miapp/index.html")
     
class LibroList(ListView):
    model = Libro
    template_name = 'miapp/lista_libros.html'

class LibroCreate():
    model = Libro
    template_name ='miapp/nuevo_libro.html'
