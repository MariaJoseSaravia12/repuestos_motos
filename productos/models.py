from django.db import models
from django.utils.html import format_html
import datetime

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return '%s' % self.nombre



class Producto(models.Model):
    Oferta = "Oferta"
    Publicado = "Publicado"
    Vendido = "Vendido"
    En_falta= "En Falta"
    
    
    APROBACION_PRODUCTO = (
      (Oferta, "Oferta"),
      (Publicado, "Publicado"),
      (Vendido ,"Vendido"),
      (En_falta,"En Falta")
    )
    estado = models.CharField(max_length=10, choices=APROBACION_PRODUCTO, default="Publicado")
    producto = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField('Fecha de publicación')
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", blank=True, null=True)    
    #categoria = models.ManyToManyField(Categoria)
    categoria = models.ForeignKey(Categoria, blank=False, null=True, on_delete=models.CASCADE
    )

    stock = models.IntegerField(default=0)
    descripcion = models.TextField(  default="")
    precio = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    descuento = models.IntegerField(default=0)


    def tipo_de_producto(self):
      if self.estado == "Vendido":
        return format_html('<span style="background-color: #258a60;color:#ffffff;padding: 7px;">{}</span>', self.estado, )
      elif self.estado == "Oferta":
        return format_html('<span style="background-color: #f80174;color:#ffffff; padding: 7px;">{}</span>', self.estado, )
      elif self.estado == "Publicado":
        return format_html('<span style="background-color: #3520F7;color:#ffffff;padding: 7px;">{}</span>', self.estado, )
      elif self.estado == "En Falta":
        return format_html('<span style="background-color: #FA150C;color:#ffffff;padding: 7px;">{}</span>', self.estado, )
     
    def __str__(self, ):
      return self.producto  + "------" + str(self.fecha_publicacion)


