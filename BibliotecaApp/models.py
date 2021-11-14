from django.db import models


# Create your models here.


class Libro(models.Model):
    nombre = models.CharField(max_length=256)


class Escritor(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_nacimiento = models.DateField()


class Editorial(models.Model):
    nombre = models.CharField(max_length=256)

class RelacionBiblioteca(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
