from django.shortcuts import render, ,get_object_or_404,get_list_or_404
from django.http import HttpResponse, Http404
from .models import Libro, Escritor, Editorial, RelacionBiblioteca
# Create your views here.

#devuelve el listado de empresas
def index(request):
    #return HttpResponse("Hello, World , Biblioteca Edition")
    escritores = get_list_or_404(Escritor.objects.order_by("nombre"))
    output = ', '.join([d.nombre for d in escritores])
    return HttpResponse(output)
