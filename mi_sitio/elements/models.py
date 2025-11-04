from django.db import models
from django.contrib import admin
from django.core.exceptions import ValidationError

# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.titulo
    
class Tipo(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.titulo
    
class Elemento(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2,default=6.10)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now=True)

    #personalizacion 2
    #@admin.display(description='¿Barato?')
    @admin.display(boolean=True, description='¿Barato?')
    def cheap(self):
        return 0 <= self.precio < 9.9

    def __str__(self):
        return self.titulo
    
    #Validaciones personalizadas
    def clean(self):
        if self.precio < 0:
            raise ValidationError('El precio no puede ser negativo.')