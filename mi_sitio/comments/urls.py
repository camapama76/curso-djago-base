from django.urls import path
from . import views


app_name = 'comments'
urlpatterns = [
    path('/add',views.add, name='add'),    
    path('',views.listado, name='listado'),
    path('/actualizar/<int:id_comentario>', views.actualizar, name='actualizar'),
    path('/eliminar/<int:id_comentario>', views.eliminar, name='eliminar'),
]
