from django.contrib import admin
from gestionPedidos.models import clientes, Articulos, Pedidos

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","telefono")
    search_fields=("nombre","email")

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha","entregado")
    list_filter=("fecha",)
    date_hierarchy="fecha"  

admin.site.register(clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)

