from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from .models import Libro, Escritor, Editorial

# Create your views here.
"""[E2] Funcionalidades básicas (2 puntos) Personalización de una plantilla (estructura de varios niveles) y sus 
estilos. Visualizar la portada de "Book Store", mostrando un libro de cada editorial (p.ej. el más reciente o el 
criterio que queráis). Visualizar la lista de libros, que además permita ir a otra vista para ver los detalles de un 
libro concreto, incluido el nombre de su editorial y la lista de sus autores. Visualizar la lista de editoriales, 
que además permita ir a otra vista para ver los detalles de una editorial, incluida la lista de libros de la misma. 
Visualizar la lista de autores, que además permita ir a otra vista para ver los detalles de un autor, incluida la 
lista de libros del mismo. """


# devuelve portada todo
def index(request):
    return ("TODO PORTADA")

#todo
def listaEscritor(request):
    # return HttpResponse("Hello, World , Biblioteca Edition")
    escritores = get_list_or_404(Escritor.objects.order_by("nombre"))
    output = ",".join([a.nombre for a in escritores])
    return HttpResponse(output)

#todo
def detalleEscritor(request, escritor_id):
    return


def listaEditorial(request):
    editoriales = get_list_or_404(Editorial.objects.order_by("nombre"))
    context = {"Editorial": editoriales}
    return render(request, "ListaEditoriales.html", editoriales)


#todo
def detalleEditorial(request, editorial_id):
    editorial = get_object_or_404(Editorial, pk=editorial_id)
    #libros = get_list_or_404() TODO encontrar una manera de pasar los libros que comparten la editorial
    #context =
    return request(request,"detalleEditorial.html",context)


# devuelve el listado de libros
def listaLibro(request):
    libros = get_list_or_404((Libro.objects.order_by("nombre")))
    output = output = ', '.join([e.nombre for e in libros])
    context = {"libro": libros}
    return render(request,"listaLibro.html",context)


# devuelve los detalles de un libro
def detalleLibro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    escritor = libro.escritor_set.all()
    editorial = libro.editorial
    context = {"escritor" : escritor, "editorial": editorial }
    return render(request, "detalleLibro", context)