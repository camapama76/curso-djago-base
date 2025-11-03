from django.db import models
from elements.models import Elemento

# Create your models here.
class Comentario(models.Model):
    texto = models.TextField(max_length=250)
    fecha_posted = models.DateTimeField(auto_now_add=True)
    element = models.ForeignKey(Elemento, on_delete=models.CASCADE, null=True)    

    def __str__(self):
        return 'Commentario #{}'.format(self.id)