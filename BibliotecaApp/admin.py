from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Libro, Escritor, Editorial, RelacionBiblioteca
admin.site.register(Libro)
admin.site.register(Escritor)
admin.site.register(Editorial)
admin.site.register(RelacionBiblioteca)