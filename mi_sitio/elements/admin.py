from calendar import c
from django.contrib import admin
from .models import Categoria, Tipo, Elemento
from django.utils.text import slugify
# Register your models here.

# class ElementoInline(admin.TabularInline):
#     model = Elemento
# class ElementoStackedInline(admin.StackedInline):
#     model = Elemento    

@admin.register(Categoria,Tipo)
class CategoriaTipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    # inlines = [
    #     #ElementoInline
    #     ElementoStackedInline
    # ]


#Personalizaciones
@admin.display(description='Título en mayúsculas')
def uppercase_titulo(obj):
    return f"{obj.id} - {obj.titulo}".upper()


@admin.register(Elemento)
class ElementoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'precio', 'categoria', 'tipo', 'creado', 'actualizado', uppercase_titulo, 'cheap')
    # search_fields = ('titulo', 'descripcion')
    # list_filter = ('categoria', 'tipo', 'creado')
    # prepopulated_fields = {'slug': ('titulo',)}     
    # date_hierarchy = 'creado'
    # ordering = ('-creado',) 
    # list_editable = ('precio',)
    # fields = ('titulo', 'slug', 'descripcion', 'precio', 'categoria', 'tipo') #opcion1
    # fields = (('titulo', 'slug'), 'descripcion', 'precio', ('categoria', 'tipo')) #opcion 2
    fieldsets = [
        (
            "Datos Generales", 
            {
                "fields": (('titulo', 'slug'), 'descripcion', ('categoria', 'tipo'))
            }
        ),
        (
            "Datos de Precio", 
            {
                "fields": ('precio',),
                "classes": ('collapse',)
            }
        )
    ]

    def save_model(self, request, obj, form, change):
        if not(change) and obj.slug == '':
            obj.slug=slugify(obj.titulo)
        if obj.slug == '':
            obj.slug=slugify(obj.titulo)

        super().save_model(request, obj, form, change)

    # #exclude = ()
    # save_as = True      
    # save_on_top = True
    # class Media:
    #     css={
    #          # 'all': ('mi_sitio/css/admin.css',)*
    #     }
    