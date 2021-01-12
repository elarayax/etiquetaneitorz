from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from gestionPedidos.imprimidor import imprimir,nota_venta,factura,guia,transferencia,bodega
from rest_framework_swagger.views import get_swagger_view


def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def resulta(rest):
    if rest == 1:
        resultado = "<br><div style = 'width: 250px;' class = 'alert alert-success'><strong> Impresión Lista!</strong></div>"
    elif rest == 2:
        resultado = "<br ><div style = 'width: 250px;' class = 'alert alert-danger' ><strong > Error en la impresion, no se encontró folio </strong></div>"
    elif rest == 3:
        resultado = "<br ><div style = 'width: 250px;' class = 'alert alert-danger' ><strong > Error en la impresion, no hay transporte </strong></div>"
    elif rest == 4:
        resultado = "<br ><div style = 'width: 250px;' class = 'alert alert-danger' ><strong > Error en la impresion, no se encontró nota de venta </strong></div>"
    elif rest == 5:
        resultado = "<br ><div style = 'width: 250px;' class = 'alert alert-danger' ><strong > Error en la impresion, no se encontró razón social </strong></div>"
    elif rest == 6:
        resultado = "<br ><div style = 'width: 250px;' class = 'alert alert-danger' ><strong > Error en la impresion, No se pudo conectar a la impresora</strong></div>"
    elif rest == 7:
        resultado = "<br ><div style = 'width: 250px;' class = 'alert alert-danger' ><strong > Error en la impresion, Query mal ejecutada </strong></div>"
    else:
        resultado = "<br ><div style = 'width: 250px;' class = 'alert alert-danger' ><strong > Error en la impresion </strong></div>"
    return resultado

def buscar(request):
    if request.GET["prd"]:
        #producto = request.GET["prd"]
        etiqueta = request.GET["prd"]
        seleccion = request.GET["select"]
        if seleccion == "nop":
            resultado = "<br ><div style = 'width: 250px;' class = 'alert alert-danger' ><strong > Seleccione Tipo de Documento </strong></div>"
            return render(request, "busqueda_productos.html", {"estado": resultado})
        elif seleccion == "1":
            lo = nota_venta(etiqueta)
            return render(request, "busqueda_productos.html", {"estado": resulta(lo)})
        elif seleccion == "2":
            lo = factura(etiqueta)
            return render(request, "busqueda_productos.html", {"estado": resulta(lo)})
        elif seleccion == "3":
            lo = guia(etiqueta)
            return render(request, "busqueda_productos.html", {"estado": resulta(lo)})
        elif seleccion == "4":
            lo = transferencia(etiqueta)
            return render(request, "busqueda_productos.html", {"estado": resulta(lo)})
        elif seleccion == "5":
            lo = bodega(etiqueta)
            return render(request, "busqueda_productos.html", {"estado": resulta(lo)})
    else:
        resultado = "<br ><div style = 'width: 250px;' class = 'alert alert-danger' ><strong > Ingrese Dato de Busqueda </strong></div>"
        return render(request, "busqueda_productos.html", {"estado": resultado})
    return render(request, "busqueda_productos.html")


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
