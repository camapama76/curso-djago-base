from django.contrib import admin
from .models import Comentario

# Register your models here.

@admin.register(Comentario)# opcion con decorador
class CommentAdmin(admin.ModelAdmin):
    # list_display = ('id', 'texto')
    # search_fields = ('id', 'texto')
    # date_hierarchy = 'fecha_posted'
    # ordering = ('fecha_posted',)
    # list_filter = ('id', 'fecha_posted')
    # list_editable = ('texto',)
    
    #fields = ('texto',)
    exclude = ('element',)
    
    save_as = True
    save_on_top = True

    def delete_queryset(self, request, queryset):
        print("Eliminando comentarios seleccionados...")
        super().delete_queryset(request, queryset)
    
    def save_model(self, request, obj, form, change):
        print("Guardando comentario...")
        super().save_model(request, obj, form, change)
        print("Comentario guardado.")

    # class Media:
    #     css = {
    #         "all": ['my_style.css']
    #     }
#opcional
#admin.site.register(Comentario,CommentAdmin)