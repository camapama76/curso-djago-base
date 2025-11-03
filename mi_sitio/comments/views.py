from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.http import Http404
from .models import Comentario
from .forms import ComentarioForm
# Create your views here.
""" def add(request):
    if(request.method == 'POST'):
        #save
        if request.POST.get('texto') != '' :            
            comentario=Comentario()
            comentario.texto=request.POST.get('texto')
            comentario.save()
        else:
            print("No hay texto")
    if(request.method=='GET'):
        pass
    return render(request, 'add.html') """
#insertar un comentario
def add(request):
    if(request.method == 'POST'):
        formulario=ComentarioForm(request.POST)
        comentario=formulario.save()
        print("Comentario guardado: ", comentario)
        return redirect('comments:listado')
    else:
        formulario=ComentarioForm()
    return render(request, 'comentarios/add.html', {'formulario': formulario})

#listar los comentarios
def listado(request):
    #listado=get_list_or_404(Comentario) #es para verificar si el listado esta vacio
    listado=Comentario.objects.all()
    #adicionamops la paginacion
    paginator=Paginator(listado, 3) #3 comentarios por pagina
    page_number=request.GET.get('page')
    comentarios_page=paginator.get_page(page_number)

    return render(request, 'comentarios/listado.html', {'listado': comentarios_page})

#actualizar un comentario
def actualizar(request, id_comentario):
    
    #metodo con get_object_or_404
    comentario=get_object_or_404(Comentario, id=id_comentario)
    #metodo con manejo de excepciones
    #try:
    #    comentario=get_object_or_404(Comentario, id=id_comentario)
    #except Http404:
    #    raise Http404("Comentario no encontrado")
    
    
    #metodo alternativo
    #try:
    #    comentario=Comentario.objects.get(id=id_comentario)
    #except Comentario.DoesNotExist:
    #    raise Http404("Comentario no encontrado")
    
    if(request.method == 'POST'):
        formulario=ComentarioForm(request.POST, instance=comentario)
        if formulario.is_valid():
            comentario=formulario.save()
            print("Comentario actualizado: ", comentario)
            return redirect('comments:listado')
    else:
        formulario=ComentarioForm(instance=comentario)
    return render(request, 'comentarios/add.html', {'formulario': formulario})

#eliminar un comentario
def eliminar(request, id_comentario):
    #comentario=Comentario.objects.get(id=id_comentario)
    comentario=get_object_or_404(Comentario, id=id_comentario)
    if request.method=='POST':
        comentario.delete()
        return redirect('comments:listado')
    #listado=Comentario.objects.all()    
    #return render(request, 'comentarios/listado.html', {'listado': listado})