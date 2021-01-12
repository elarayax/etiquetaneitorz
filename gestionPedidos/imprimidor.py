import pyodbc
import os
from os import system
from PIL import Image
import zpl
import socket
from gestionPedidos.printerbodega import imprimir2


def imprimir(razon, direccio, ciudad, telefono, nombre, transporte, folio, nota, bultos, peso):
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
    l.write_text("RAZON SOCIAL / AT :", char_height=2,
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
    l.write_text("TRANSPORTE", char_height=2,
                 char_width=2, line_width=80)
    l.endorigin()
    l.origin(40, 29)
    l.write_text(transporte, char_height=2,
                 char_width=2, line_width=80)
    l.endorigin()
    l.origin(40, 31)
    l.write_text("------------------", char_height=1,
                 char_width=1, line_width=80)
    l.endorigin()

    l.origin(20, 33)
    l.write_text("FACTURA", char_height=2,
                 char_width=2, line_width=80)
    l.endorigin()
    l.origin(20, 35)
    l.write_text(folio, char_height=2, char_width=2, line_width=80)
    l.endorigin()
    l.origin(20, 37)
    l.write_text("------------------", char_height=1,
                 char_width=1, line_width=80)
    l.endorigin()

    l.origin(40, 33)
    l.write_text("NOTA DE VENTA", char_height=2,
                 char_width=2, line_width=80)
    l.endorigin()
    l.origin(40, 35)
    l.write_text(nota, char_height=2, char_width=2, line_width=80)
    l.endorigin()
    l.origin(40, 37)
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
    l.write_text("^BQN,2,4^FDQA,Envío "+str(folio)+" usando "+transporte+", desde impac a su destino", char_height=2,
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
            l.write_text(str(x+1)+" de "+str(bultos), char_height=2, char_width=2, line_width=80)
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

def nota_venta(nota):
    op = nota
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=IMPAC-SAP;DATABASE=DB_IMPAC_NUEVA;UID=sa;PWD=')
    cursor = conn.cursor()
    telefono = "S/N"
    try:
        qt = "SELECT distinct T0.[DocNum], T2.[FolioNum], T2.[U_transporte], T2.[U_PesoNeto], T3.[CityS], T3.[StreetS], T2.[CardName], FLOOR(T2.[U_CantBultos]), T2.[PayToCode], T4.[Name], T4.[Tel1], T4.[Cellolar] FROM ORDR T0 INNER JOIN RDR1 T1 ON T0.DocEntry = T1.DocEntry INNER JOIN ODLN T2 ON T2.DocEntry = T1.TrgetEntry full JOIN DLN12 T3 ON T2.DocEntry = T3.DocEntry full JOIN OCPR T4 ON T2.CntctCode = T4.CntctCode where T0.DocNum ="+str(op)
        nota = None
        folio = None
        cursor.execute(qt)
    except:
        return 0
    
    for row in cursor.fetchall():
        razon = row[6]
        direccio = row[5]
        transporte = row[2]
        folio = row[1]
        tel = row[10]
        cel = row[11]
        peso = row[3]
        bultos = row[7]
        nota = row[0]
        ciudad = row[4]
        nombre = row[9]
    if nota == None:
        cur = conn.cursor()
        q = "SELECT distinct T2.DocNum, T0.FolioNum, T2.U_Transporte, T2.U_PesoNeto, T3.[CityS], T3.[StreetS], T2.[CardName],FLOOR(T2.[U_CantBultos]), T2.[PayToCode], T4.[Name], T4.[Tel1], T4.[Cellolar], T2.DocEntry FROM OINV T0 JOIN INV1 T1 ON T0.DocEntry = T1.DocEntry JOIN ORDR T2 ON T1.BaseEntry = T2.DocEntry full JOIN RDR12 T3 ON T2.DocEntry = T3.DocEntry full JOIN OCPR T4 ON T0.CntctCode = T4.CntctCode WHERE  T2.DocNum ="+str(op)
        cur.execute(q)
        for row in cur.fetchall():
            razon = row[6]
            direccio = row[5]
            transporte = row[2]
            folio = row[1]
            tel = row[10]
            cel = row[11]
            peso = row[3]
            bultos = row[7]
            nota = row[0]
            ciudad = row[4]
            nombre = row[9]

    if folio == None:
        cur = conn.cursor()
        print(nota)
        try:
            q = "select T1.FolioNum, T1.U_Transporte  from DLN1 T0 FULL JOIN OINV T1 on T0.TrgetEntry = T1.DocEntry WHERE T0.BaseDocNum =" + str(nota)
            cur.execute(q)
        except : 
            return 0
        for rows in cur.fetchall():
            folio = rows[0]
            transporte = rows[1]
        if tel != None:
            telefono = tel
        elif cel != None:
            telefono = cel
        else:
            telefono = "S/N"
    if folio == None:
        return 2
    elif transporte == None:
        return 3
    elif nota == None:
        return 4
    elif razon == None:
        return 5
    return imprimir(razon, direccio, ciudad, telefono, nombre, transporte, folio, nota, bultos, peso)

def factura(nota):
    op = nota
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=IMPAC-SAP;DATABASE=DB_IMPAC_NUEVA;UID=sa;PWD=')
    cursor = conn.cursor()
    tel = "S/N"
    razon = "sd"
    direccio = "nn"
    ciudad = "nn"
    nombre = "asd"
    transporte = "sa"
    folio = "npp"
    try:
        q = "select T0.FolioNum,T0.U_Transporte,T1.BaseDocNum from OINV T0 FULL JOIN DLN1 T1 ON T1.TrgetEntry = T0.DocEntry WHERE T0.FolioNum ="+str(op)
        cursor.execute(q)
        for row in cursor.fetchall():
            print(row)
            if row[0] != None:
                folio = row[0]
                transporte = row[1]
                nota = row[2]
            else:
                return 0
    except:
        return 7
    cursors = conn.cursor()
    try:
        qt = "SELECT distinct T0.[DocNum], T2.[FolioNum], T2.[U_transporte], T2.[U_PesoNeto], T3.[CityS], T3.[StreetS], T2.[CardName], FLOOR(T2.[U_CantBultos]), T2.[PayToCode], T4.[Name], T4.[Tel1], T4.[Cellolar] FROM ORDR T0 INNER JOIN RDR1 T1 ON T0.DocEntry = T1.DocEntry INNER JOIN ODLN T2 ON T2.DocEntry = T1.TrgetEntry full JOIN DLN12 T3 ON T2.DocEntry = T3.DocEntry full JOIN OCPR T4 ON T2.CntctCode = T4.CntctCode where T0.DocNum ="+str(nota)
        cursors.execute(qt)
        for row in cursors.fetchall():
            print(row)
            razon = row[6]
            direccio = row[5]
            #transporte = row[2]
            tel = row[10]
            cel = row[11]
            peso = row[3]
            bultos = row[7]
            ciudad = row[4]
            nombre = row[9]
    except :
        return 7
    if tel != None:
        telefono = tel
    elif cel != None:
        telefono = cel
    else:
        telefono = "S/N"
    if folio == None:
        return 2
    elif transporte == None:
        return 3
    elif nota == None:
        return 4
    elif razon == None:
        return 5
    return imprimir(razon, direccio, ciudad, telefono, nombre,transporte, folio, nota, bultos, peso)

def guia(nota):
    op = nota
    tel = None
    cel = None
    razon = None
    direccio = None
    peso = None
    bultos = None
    ciudad = None
    nombre = None
    folio = None
    nota = None
    conn = pyodbc.connect( 'DRIVER={SQL Server};SERVER=IMPAC-SAP;DATABASE=DB_IMPAC_NUEVA;UID=sa;PWD=')
    try:
        cursors = conn.cursor()
        qt = "SELECT distinct T0.[DocNum], T2.[FolioNum], T2.[U_transporte], T2.[U_PesoNeto], T3.[CityS], T3.[StreetS], T2.[CardName],FLOOR(T2.[U_CantBultos]), T2.[PayToCode], T4.[Name], T4.[Tel1], T4.[Cellolar] FROM ORDR T0 INNER JOIN RDR1 T1 ON T0.DocEntry = T1.DocEntry INNER JOIN ODLN T2 ON T2.DocEntry = T1.TrgetEntry full JOIN DLN12 T3 ON T2.DocEntry = T3.DocEntry full JOIN OCPR T4 ON T2.CntctCode = T4.CntctCode where T2.FolioNum ="+str(op)
        cursors.execute(qt)
    except:
        return 0
    for row in cursors.fetchall():
        print(row)
        razon = row[6]
        direccio = row[5]
        transporte = row[2]
        tel = row[10]
        cel = row[11]
        peso = row[3]
        bultos = row[7]
        ciudad = row[4]
        nombre = row[9]
        folio = row[1]
        nota = row[0]

    if tel != None:
        telefono = tel
    elif cel != None:
        telefono = cel
    else:
        telefono = "S/N"
    if folio == None:
        return 2
    elif transporte == None:
        return 3
    elif nota == None:
        return 4
    elif razon == None:
        return 5
    return imprimir(razon, direccio, ciudad, telefono, nombre,transporte, folio, nota, bultos, peso)

def transferencia(nota):
    op = nota
    razon = None
    direccio = None
    transporte = "S/N"
    tel = None
    cel = None
    peso = None
    bultos = None
    ciudad = None
    nombre = None
    folio = None
    nota = None
    try :
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=IMPAC-SAP;DATABASE=DB_IMPAC_NUEVA;UID=sa;PWD=')
        cursors = conn.cursor()
        qt = "SELECT distinct T0.[DocNum], T0.[FolioNum], T2.[U_transporte], T2.[U_PesoNeto], T3.[CityS], T3.[StreetS], T2.[CardName],FLOOR(T2.[U_CantBultos]), T2.[PayToCode], T4.[Name], T4.[Tel1], T4.[Cellolar] FROM OWTR T0 INNER JOIN RDR1 T1 ON T0.DocEntry = T1.DocEntry INNER JOIN ODLN T2 ON T2.DocEntry = T1.TrgetEntry full JOIN DLN12 T3 ON T2.DocEntry = T3.DocEntry full JOIN OCPR T4 ON T2.CntctCode = T4.CntctCode where T0.FolioNum ="+str(op)
        cursors.execute(qt)
    except:
        return 0
    for row in cursors.fetchall():
        print(row)
        razon = row[6]
        direccio = row[5]
        transporte = row[2]
        tel = row[10]
        cel = row[11]
        peso = row[3]
        bultos = row[7]
        ciudad = row[4]
        nombre = row[9]
        folio = row[1]
        nota = row[0]

    if tel != None:
        telefono = tel
    elif cel != None:
        telefono = cel
    else:
        telefono = "S/N"
    
    if folio == None:
        return 2
    elif transporte == None:
        return 3
    elif nota == None:
        return 4
    elif razon == None:
        return 5
    return imprimir(razon, direccio, ciudad, telefono, nombre,transporte, folio, nota, bultos, peso)
def bodega(nota):
    op = nota
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=IMPAC-SAP;DATABASE=DB_IMPAC_NUEVA;UID=sa;PWD=')
    cursor = conn.cursor()
    telefono = "S/N"
    try:
        qt = "SELECT distinct T0.[DocNum], T2.[FolioNum], T2.[U_transporte], T2.[U_PesoNeto], T3.[CityS], T3.[StreetS], T2.[CardName], FLOOR(T2.[U_CantBultos]), T2.[PayToCode], T4.[Name], T4.[Tel1], T4.[Cellolar] FROM ORDR T0 INNER JOIN RDR1 T1 ON T0.DocEntry = T1.DocEntry INNER JOIN ODLN T2 ON T2.DocEntry = T1.TrgetEntry full JOIN DLN12 T3 ON T2.DocEntry = T3.DocEntry full JOIN OCPR T4 ON T2.CntctCode = T4.CntctCode where T0.DocNum ="+str(op)
        nota = None
        folio = None
        cursor.execute(qt)
    except:
        return 0
    for row in cursor.fetchall():
        razon = row[6]
        direccio = row[5]
        folio = row[1]
        tel = row[10]
        cel = row[11]
        peso = row[3]
        bultos = row[7]
        nota = row[0]
        ciudad = row[4]
        nombre = row[9]
    if nota == None:
        cur = conn.cursor()
        q = "SELECT distinct T2.DocNum, T0.FolioNum, T2.U_Transporte, T2.U_PesoNeto, T3.[CityS], T3.[StreetS], T2.[CardName],FLOOR(T2.[U_CantBultos]), T2.[PayToCode], T4.[Name], T4.[Tel1], T4.[Cellolar], T2.DocEntry FROM OINV T0 JOIN INV1 T1 ON T0.DocEntry = T1.DocEntry JOIN ORDR T2 ON T1.BaseEntry = T2.DocEntry full JOIN RDR12 T3 ON T2.DocEntry = T3.DocEntry full JOIN OCPR T4 ON T0.CntctCode = T4.CntctCode WHERE  T2.DocNum ="+str(op)
        cur.execute(q)
        for row in cur.fetchall():
            razon = row[6]
            direccio = row[5]
            folio = row[1]
            tel = row[10]
            cel = row[11]
            peso = row[3]
            bultos = row[7]
            nota = row[0]
            ciudad = row[4]
            nombre = row[9]
    """
    if folio == None:
        cur = conn.cursor()
        print(nota)
        try:
            q = "select T1.FolioNum, T1.U_Transporte  from DLN1 T0 FULL JOIN OINV T1 on T0.TrgetEntry = T1.DocEntry WHERE T0.BaseDocNum =" + str(nota)
            cur.execute(q)
        except : 
            return 0
        for rows in cur.fetchall():
            folio = rows[0]
            transporte = rows[1]
        if tel != None:
            telefono = tel
        elif cel != None:
            telefono = cel
        else:
            telefono = "S/N"
    """
    return imprimir2(razon, direccio, ciudad, telefono, nombre, folio, nota, bultos, peso)
