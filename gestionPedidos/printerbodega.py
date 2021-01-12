import pyodbc
import os
from os import system
from PIL import Image
import zpl
import socket


def imprimir2(razon, direccio, ciudad, telefono, nombre, folio, nota, bultos, peso):
    l = zpl.Label(80, 100)
    l.origin(2, 2)
    l.write_graphic(Image.open(os.path.join(
        os.path.dirname(zpl.__file__), 'logoimpac.png')), 20, 5)
    l.endorigin()

    l.origin(40, 3)
    l.write_text("WWW.IMPAC.CL", char_height=2,
                 char_width=2, line_width=80)
    l.endorigin()

    l.origin(2, 9)
    l.write_text("RAZON SOCIAL :", char_height=2,
                 char_width=2, line_width=80,)
    l.endorigin()
    l.origin(2, 11)
    l.write_text(razon, char_height=2,
                 char_width=2, line_width=80,)
    l.endorigin()
    l.origin(2, 13)
    l.write_text(60 * "-", char_height=1, char_width=1, line_width=80)
    l.endorigin()

    l.origin(2, 15)
    l.write_text("DIRECCION :", char_height=2,
                 char_width=2, line_width=80)
    l.endorigin()
    l.origin(2, 17)
    l.write_text(""+direccio, char_height=2,
                 char_width=2, line_width=80)
    l.endorigin()
    l.origin(2, 19)
    l.write_text(60 * "-", char_height=1, char_width=1, line_width=80)
    l.endorigin()

    l.origin(2, 21)
    l.write_text("CIUDAD :", char_height=2,
                 char_width=2, line_width=80)
    l.endorigin()
    l.origin(2, 23)
    l.write_text(ciudad, char_height=2, char_width=2, line_width=80)
    l.endorigin()
    l.origin(2, 25)
    l.write_text("------------------", char_height=1,
                 char_width=1, line_width=80)
    l.endorigin()
    l.origin(40, 21)
    l.write_text("TELEFONO :", char_height=2,
                 char_width=2, line_width=50)
    l.endorigin()
    l.origin(40, 23)
    l.write_text(telefono, char_height=2, char_width=2, line_width=80)
    l.endorigin()
    l.origin(40, 25)
    l.write_text("------------------", char_height=1,
                 char_width=1, line_width=80)
    l.endorigin()

    l.origin(2, 27)
    l.write_text("Receptor :", char_height=2,
                 char_width=2, line_width=80)
    l.endorigin()
    l.origin(2, 29)
    l.write_text(nombre, char_height=2, char_width=2, line_width=80)
    l.endorigin()
    l.origin(2, 31)
    l.write_text("------------------", char_height=1,
                 char_width=1, line_width=80)
    l.endorigin()

    l.origin(40, 27)
    l.write_text("RETIRO :", char_height=2,
                 char_width=2, line_width=80)
    l.endorigin()
    l.origin(40, 29)
    l.write_text("MESON BODEGA", char_height=2,
                 char_width=2, line_width=80)
    l.endorigin()
    l.origin(40, 31)
    l.write_text("------------------", char_height=1,
                 char_width=1, line_width=80)
    l.endorigin()


    l.origin(30, 33)
    l.write_text("NOTA DE VENTA", char_height=2,
                 char_width=2, line_width=80)
    l.endorigin()
    l.origin(30, 35)
    l.write_text(nota, char_height=2, char_width=2, line_width=80)
    l.endorigin()
    l.origin(30, 37)
    l.write_text("------------------", char_height=1,
                 char_width=1, line_width=80)
    l.endorigin()

    l.origin(20, 39)
    l.write_text("BULTOS", char_height=2,
                 char_width=2, line_width=80)
    l.endorigin()
    l.origin(20, 43)
    l.write_text("------------------", char_height=1,
                 char_width=1, line_width=80)
    l.endorigin()

    l.origin(40, 39)
    l.write_text("PESO", char_height=2,
                 char_width=2, line_width=80)
    l.endorigin()
    l.origin(40, 41)
    peso = round(peso, 2)
    l.write_text(str(peso)+" KG", char_height=2,
                 char_width=2, line_width=80)
    l.endorigin()
    l.origin(40, 43)
    l.write_text("------------------", char_height=1,
                 char_width=1, line_width=80)
    l.endorigin()

    l.origin(2, 47)
    l.write_text("Casa Matriz: Antonio Escobar Williams 176, Cerrillos, Chile",
                 char_height=2, char_width=2, line_width=80)
    l.endorigin()
    l.origin(2, 49)
    l.write_text("Fono:(56)225917500 - Correo: impac@impac.cl",
                 char_height=2, char_width=2, line_width=80)
    l.endorigin()
    if folio == None:
        folio = "S/N"
    l.origin(3, 32)
    l.write_text("^BQN,2,4^FDQA,Pedido con nota de venta "+str(nota)+" retirado en casa matriz", char_height=2,
                 char_width=2, line_width=50)
    l.endorigin()
    #l.preview()
    c = round(bultos)
    #print(c)
    c = round(bultos)
    j = 0
    for x in range(c):
        try:
            mysocket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            host = "192.168.0.241"
            port = 9100
            print("empieza")
            l.origin(20, 41)
            l.write_text(str(x+1)+" de "+str(bultos),
                         char_height=2, char_width=2, line_width=80)
            l.endorigin()
            n = str(l.dumpZPL()).encode()
            mysocket.connect((host, port))  # connecting to host
            print("conectado")
            mysocket.send(n)  # using bytes
            print("enviado")
            print(x)
            #print(l.dumpZPL())
            mysocket.close()
            j = 1
        except:
            print("Error with the connection")
            # closing connection
            os.system('CLS')
            j = 6
    return j
