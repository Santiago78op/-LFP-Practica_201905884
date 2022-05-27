from analisis.lexema import *

class Token:

    def __init__(self,id:str,valor:Lexema, description:str) -> None:
        self.id = id
        self.valor = valor
        self.description = description
        
    def info(self):
        lex = self.valor
        print("Token")
        print("Nombre-Token: ", self.id)
        print("Valor-Atributo: ", lex.valor)
        print("Descripcion: ", self.description)
        print("Fila: ", lex.fila)
        print("Columna: ", lex.col)
        

        
    def toString(self) -> str:
        lex = self.valor
        return f'{self.id} | " {lex.valor} " en: ({str(lex.fila)}, {str(lex.col)})' 
    