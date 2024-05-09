from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db.models import Q
from productos.models import Producto
from django.views.generic import View
import datetime



def index(request):
    params = {}    
    producto = Producto.objects.filter(
        Q(estado="Publicado"))
    oferta = Producto.objects.filter(
        Q(estado="Oferta"))   
    params["producto"] = producto
    params["oferta"] = oferta

    print(producto)
    return render(request, "vistaprevia/index.html", params)


def oferta(request):
    params = {}    
    producto = Producto.objects.filter(
        Q(estado="Oferta"),
    )
    params["producto"] = producto
    print(producto)
    return render(request, "vistaprevia/oferta.html", params)

class Templatetags1(View):
    template = "vistaprevia/templatetags1.html"
    def get(self, request):
        params = {}
        params["cross_site_scripting"]="""
            <script>
            $("*").css({
                "background-color": "yellow",
                "font-weight": "bolder",
            });
            </script>
        
        """
        producto = Producto.objects.filter(
            Q(estado="Publicado"),
        )
        params["los_productos"]=producto

        



        params["fecha_de_hoy"]=datetime.datetime.now
        params["mi_lista"]=[1,2,3,4,5,6]
        params["row3"]="row3"
        params["mi_lista2"]=[]

        return render(request, self.template, params)

    def post(self, request):
        params={}
        producto=request.POST.get("producto")
        el_pedido=request.session.get("el_pedido")
        if el_pedido:
            cantidad = el_pedido.get(producto)
            if cantidad:
                el_pedido[producto]=cantidad+1
            else:
                el_pedido[producto]=1
        else:
            el_pedido={}
            el_pedido[producto]=1

        request.session["el_pedido"]=el_pedido
        print(request.session["el_pedido"])

        return redirect("templatetags1")
    
    
