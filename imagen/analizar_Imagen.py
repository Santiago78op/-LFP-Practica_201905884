import matplotlib.pyplot as plt
from PIL import Image
import os
import requests
import json

class Analizarimagen:
    
    Tp = ''
    producto = ''
    ingresos = ''
    nombre = ''
    grafica = ''
    titulo = ''
    titulox = ''
    tituloy = ''
    lista_invtario = ''
    lista_contenido = ''
                
    def analizadorData(self, infoData:dict, encabezado):
        global Tp 
        global producto
        global ingresos
        global lista_invtario
        Tp = encabezado
        articulo = []
        producto = articulo
        monto = []
        ingresos = monto
        lista_invet = []
        lista_invtario = lista_invet
        for inventario in infoData[encabezado]:
            if len(inventario) == 3:
                nombre_pt = inventario[0]
                articulo.append(nombre_pt)
                precio = inventario[1]
                precio = float(precio)
                cantidad = inventario[2]
                cantidad = float(cantidad)
                total = precio * cantidad
                monto.append(total)
                lista_invet.append([nombre_pt,precio,cantidad,total])
            else:
                print("Error faltan datos para procesar Grafica")
        
        
    def analizadorInts(self, infoInst:dict):
        global nombre
        global grafica
        global titulo
        global titulox
        global tituloy
        
        identificador = []
        nombre_G = infoInst["NOMBRE"]
        identificador.append(nombre_G)
        nombre = identificador
        
        tipo = []
        grafica_g = infoInst["GRAFICA"]
        tipo.append(grafica_g)
        s = tipo
        for i in range(len(s)):
            s[i] = s[i].upper()
        grafica = tipo

        indice = []
        titulo_g = infoInst["TITULO"]
        indice.append(titulo_g)
        titulo = indice
        
        indicex = []
        titulox_g = infoInst["TITULOX"]
        indicex.append(titulox_g)
        titulox = indicex
        
        indicey = []
        tituloy_g = infoInst["TITULOY"]
        indicey.append(tituloy_g)
        tituloy = indicey
   
        
    def crearGrafica(self):
        nombre_1 = nombre[-1]
        nombre_2 = nombre_1.replace('"','')
        while 1:
            if grafica[-1] == '"BARRAS"':
                ## Creamos Gráfica
                plt.bar(producto, ingresos)
                ## Legenda en el eje y
                plt.ylabel(tituloy[-1])
                ## Legenda en el eje x
                plt.xlabel(titulox[-1])
                ## Título de Gráfica
                plt.title('Reporte de Ventas'+' '+Tp)
                ##Guardar Grafica
                plt.savefig(f"{nombre_2}.png")
                ## Limpiar la unidad de memoria grafica
                plt.clf()
                img=Image.open(f"{nombre_2}.png")
                img.show()
                return True
            elif grafica[-1] == '"LINEAS"':
                fig, ax = plt.subplots()
                ax.plot(producto, ingresos)
                plt.ylabel(tituloy[-1])
                plt.xlabel(titulox[-1])
                plt.title('Reporte de Ventas'+' '+Tp)
                plt.savefig(f"{nombre_2}.png")
                plt.clf()
                img=Image.open(f"{nombre_2}.png")
                img.show()
                return True
            elif grafica[-1] == '"PIE"':
                plt.pie(ingresos, labels=producto, autopct="%0.1f %%")
                plt.title('Reporte de Ventas'+' '+Tp)
                plt.axis("equal")
                plt.savefig(f"{nombre_2}.png")
                plt.clf()
                img=Image.open(f"{nombre_2}.png")
                img.show()
                return True
            else:
                print("Fallo el generar Grafica")
                return False
        

    def getListaReporte(self):
        global lista_contenido
        lista_1 = sorted(lista_invtario, key=lambda dato: dato[3],reverse=True)
        product = dict()
        product["Producto"]=lista_1
        contenido = product["Producto"]
        contenido[0][0].replace('\"','')
        #print(json.dumps(product,indent=4))
        lista_contenido = product
        

    def sendImage(self):
        r = requests.post('http://127.0.0.1:5000/postLista',json=lista_contenido)
        print('> Server devolvio: ',r.status_code)
        