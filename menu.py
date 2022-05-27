
#Librerias 
import webbrowser
import os
from cargar_info import cargarInfo
from analisis import lexicodata,lexicoints
from imagen import analizar_Imagen



class Menu:

    def __init__(self) -> None:
        self.Cargar_Data = 1
        self.Cargar_Instrucciones = 2
        self.Analizar = 3
        self.Reportes  = 4
        self.salir = 5
        self.routeData = ''
        self.routeInst = ''
    
    def mostrar_menu(self) -> None:
        """
        Función que limpia la pantalla y muestra nuevamente el menu
        """
        os.system('cls') # NOTA para windows tienes que cambiar clear por cls
        print(f'''\t<--Menu Principal-->\n
Selecciona una opción:\n
    \t{self.Cargar_Data}) - Cargar Data
    \t{self.Cargar_Instrucciones}) - Cargar Instrucciones
    \t{self.Analizar}) - Analizar
    \t{self.Reportes}) - Reportes
    \t{self.salir}) - Salir\n''')
        
    def menu(self) -> bool:
        infodata = cargarInfo()
        cargar_imagen = analizar_Imagen.Analizarimagen()
        
        while True:
            
            self.mostrar_menu()
            
            opcionMenu = input("Inserta el numero de la opcion: >> ")
            
            try:
                opcionMenu = int(opcionMenu)
            except ValueError as error:
                opcionMenu = -1
                print(f'Error: {error}')
                print('El programa no permite carateres tipo cadena')
                input('Presione la tecla para continuar@')
            
            os.system('cls')
            
            if opcionMenu == self.Cargar_Data:
                infodata.cargar_data()
                infodata.readfile_data()
            elif opcionMenu == self.Cargar_Instrucciones:
                infodata.cargar_inst()
                infodata.readfile_inst()
            elif opcionMenu == self.Analizar:
                cargar_imagen.crearGrafica()
            elif opcionMenu == self.Reportes:
                cargar_imagen.getListaReporte()
                cargar_imagen.sendImage()
                webbrowser.open("http://127.0.0.1:5500/reportes/html/Reporte_html/reporte.html")
            elif opcionMenu == self.salir:
                print("Esto no es un adios sino un asta pronto\n")
                False
                break
            else:
                print('Opcion no válida...')
            input('Presiona enter para Ingresar al Menú...')
    
