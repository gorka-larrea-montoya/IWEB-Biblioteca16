from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listaLibro/', views.listaLibro, name="listaLibro"),
    path('detalleLibro/<int:libro_id>/', views.detalleLibro, name="detalleLibro"),
    path('listaEscritor/', views.listaEscritor, name="listaEscritor"),
    path('detalleEscritor/<int:escritor_id>/', views.detalleEscritor, name="detalleEscritor"),
    path('listaEditorial/', views.listaEditorial, name="listaEditorial"),
    path('detalleEditorial/<int:editorial_id>/', views.detalleEditorial, name="detalleEditorial"),
]
