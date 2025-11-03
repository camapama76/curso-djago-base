from django.db import models

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
    slug = models.SlugField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo