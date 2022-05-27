from analisis.error import Error
from analisis.token import *
from analisis.lexema import *
from imagen.analizar_Imagen import Analizarimagen

class LexicoInst:
    
    def __init__(self) -> None:
        self.estado = 0
        self.conteo = 0
        self.fila = 1
        self.col = 1
        self.prefijo = ''
        self.entrada = list()
        self.flujo = list()
        self.tokens = list()
        self.errores = list()
        self.imgs = list()
        self.img = dict()
        self.contenedor = list()
        self.subcont = list()
        self.seccion = ''
        self.verificada = []
        self.reserved = [   
                            'NOMBRE', 'GRAFICA','TITULO',
                            'TITULOX', 'TITULOY'
                        ]
        

    def escanear(self,entrada):
        self.str_to_list(entrada)
        while len(self.entrada) > 0:
            if self.getSeparador():
                continue
            elif self.getSimbolo():
                continue
            elif self.getId():
                token = Token(self.prefijo,self.getLexema(),'Identificador')
                self.addToken(token)
            elif self.getCadena():
                token = Token('Cadena',self.getLexema(),'Cadena de Caracteres')
                self.addToken(token)
            elif self.getNumero():
                token = Token('Numero',self.getLexema(),'Digito')
                self.addToken(token)
            else: #Hay un error léxico
                self.error()
        if len(self.errores) == 0:
            self.imgs.append(self.img)

    def str_to_list(self,entrada):
        chars = list()
        for c in entrada:
            chars.append(c)
        self.entrada = chars
        self.flujo = chars
    
    def sigChar(self) -> str:
        return self.entrada[0]
    
    def getLexema(self) -> Lexema:
        lexema = Lexema(self.prefijo,self.fila,self.col)
        self.prefijo = ''
        self.conteo = 0
        return lexema
        
    def getId(self) -> bool: # regex: [A-Z]+
        self.regresar() # Obtener los caracteres previamente analizados por otro automata
        while 1:
            if self.estado == 0:
                if self.sigChar().isalpha():
                    self.transicion(1)
                else:
                    return False
            elif self.estado == 1:
                reservada = self.prefijo.upper()
                if self.sigChar().isalpha():
                    self.transicion(1)
                elif self.getSeparador():
                    if reservada in self.reserved:
                        self.verificada.append(reservada)   
                        self.seccion = reservada
                        return True
                    else:
                        return False
                else:
                    if reservada in self.reserved:
                        self.verificada.append(reservada)      
                        self.seccion = reservada
                        return True
                    else:
                        return False
                
    def getCadena(self) -> bool:
        self.regresar()
        while 1:
            if self.estado == 0:
                if self.sigChar() == '"':
                    self.transicion(1)
                else:
                    return False
            elif self.estado == 1:
                c = self.sigChar()
                if c != '"' and c != '\n':
                    self.transicion(1)
                elif c == '"':
                    self.transicion(2)
                else:
                    return False
            elif self.estado == 2:
                self.subcont.append(self.prefijo)
                return True

    def getNumero(self) -> bool:
        self.regresar()
        while 1:
            if self.estado == 0:
                if self.sigChar().isdigit():
                    self.transicion(1)
                else:
                    return False
            elif self.estado == 1:
                if self.sigChar().isdigit():
                    self.transicion(1)
                elif self.getSeparador():
                    self.subcont.append(self.prefijo)
                    return True
                else:
                    self.subcont.append(self.prefijo)
                    return True
                

    def getSimbolo(self) -> bool:
        self.regresar()
        tipo = ''
        while 1:
            if self.estado == 0:
                if self.sigChar() == '<':
                    tipo = 'Menor'
                    description = 'Caracter Menor que'
                    self.transicion(1)
                elif self.sigChar() == '¿':
                    tipo = 'Interrogación Apertura'
                    description = 'Caracter Interrogación Apertura'
                    self.transicion(1)
                elif self.sigChar() == ':':
                    tipo = 'Dos Puntos'
                    description = 'Caracter Dos Puntos'
                    self.transicion(1)
                elif self.sigChar() == ",":
                    tipo = 'Coma'
                    description = 'Caracter Coma'
                    self.transicion(1)
                    self.img[self.seccion] = self.asignarValor()
                elif self.sigChar() == "?":
                    tipo = 'Interrogación Cierre'
                    description = 'Caracter Interrogación Cierre'
                    self.transicion(1)
                elif self.sigChar() == '>':
                    tipo = 'Mayor'
                    description = 'Caracter Mayor que'
                    self.transicion(1)
                    self.verificacion()
                else:
                    return False
            elif self.estado == 1:
                token = Token(tipo,self.getLexema(), description)
                self.addToken(token)
                return True

    def getSeparador(self) -> bool:
        c = self.sigChar()
        if c == ' ' or c == '\t':
            self.consumir()
            return True
        elif self.sigChar() == '\n':
            self.consumir()
            self.updateCount()
            return True
        else:
            return False
        
    def transicion(self,estado:int):
        self.prefijo += self.consumir()
        self.estado = estado
    
    def consumir(self) -> str:
        self.col += 1
        self.conteo += 1
        return self.flujo.pop(0)

    def updateCount(self):
        self.fila += 1
        self.col = 1
        self.conteo = 0

    def addToken(self,t:Token):
        self.tokens.append(t)
        self.entrada = self.flujo
        self.estado = 0

    def regresar(self):
        self.flujo = self.entrada
        self.estado = 0

    def error(self):
        caracter = self.consumir()
        self.entrada = self.flujo
        err = Error(self.fila,self.col,caracter)
        self.errores.append(err)
        self.estado = 0

    def asignarValor(self):
        if len(self.contenedor) == 0:
            self.contenedor.append(self.subcont)
        if len(self.contenedor) == 1 and len(self.subcont) == 1:
            valor = self.subcont.pop()
            self.subcont = list()
            self.contenedor = list()
            return valor
        else:
            valor = self.contenedor
            self.subcont = list()
            self.contenedor = list()
            return valor
    
    def verificacion(self):
        if "NOMBRE" in self.verificada and "GRAFICA" in self.verificada:
            self.inst = Analizarimagen()
            self.inst.analizadorInts(self.img)
        else:
            print("Error en el Archvio,\n"
                  "No cuenta con palabras reservadas:\n"
                  "Nombre o Grafica")
        