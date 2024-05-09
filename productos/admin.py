from django.contrib import admin
from productos.models import Producto
from productos.models import Categoria
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render


class ProductoInline(admin.TabularInline):

    model = Producto
    extra = 0

class CategoriaAdmin(admin.ModelAdmin):
    inlines = [ProductoInline]




@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    #fields =['categoria', 'fecha_publicacion', 'producto', 'imagen']

    fieldsets = [
        ("Relación", {"fields": ["categoria"]}),
        (
            "Datos generales",
            {
                "fields": [
                    'fecha_publicacion', 'producto', 'estado' , 'imagen', 'descripcion',
                ]
            },
        ),
        (
            "Datos económicos",
            {
                "fields": [
                    'precio', 'stock', 'descuento',
                ]
            },
        ),

    ]
    #acciones
    list_display = ['producto', 'fecha_publicacion', 'tipo_de_producto', 'imagen','upper_case_name', 'descripcion', 'precio',]
    ordering = ['-fecha_publicacion']
    list_filter = ('producto', 'fecha_publicacion',)
    search_fields = ('producto', 'estado')
    list_display_links = ('producto', 'fecha_publicacion',)
    actions=["publicar", "exportar_a_json", "ver_productos", "pasar_a_oferta",]

    @admin.display(description='Name')
    def upper_case_name(self, obj ):
      return ("%s %s" %(obj.producto, obj.estado)).upper()
    #pasar a publicado
    def publicar(self, request, queryset):
        registro = queryset.update(estado="Publicado")
        if registro == 1:
            mensaje = "1 registro ha cambiado a Publicado"
        else:
            mensaje = "%s registros han cambiado a Publicado" % registro
        self.message_user(request, "%s exitosamente" % mensaje)


    publicar.short_description = "Pasar a publicado"
    #pasar a oferta
    def pasar_a_oferta(self, request, queryset):
        registro = queryset.update(estado="Oferta")
        if registro == 1:
            mensaje = "1 registro ha pasado a Ofrta"
        else:
            mensaje = "%s registros han pasado a Oferta" % registro
        self.message_user(request, "%s exitosamente" % mensaje)


    pasar_a_oferta.short_description = "Pasar a oferta"
    #Ver el producto en json

    def exportar_a_json(self, request, queryset):
        response=HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response)
        return response

    def ver_productos(self, request, queryset=None, ver_todos=False):
        params={}
        productos_seleccionados = queryset        
        params["productos"]=productos_seleccionados
        return render(request, "admin/productos/productos.html", params )
    ver_productos.short_description  = "Ver productos seleccionados"

#admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
#admin.site.register(Categoria)
#admin.site.register(Producto)




