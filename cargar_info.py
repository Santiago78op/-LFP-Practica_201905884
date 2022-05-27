#Librerias Tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
#Lebrerias
from analisis import lexicodata,lexicoints
import os
import requests
import json

from io import open

class cargarInfo:
    
    
    def cargar_data(self):
        fileChooser = Tk()
        fileChooser.withdraw()
        self.datainfo = askopenfilename(filetypes = (("data files","*.data"),("all files","*.*")))
        fileChooser.destroy()         
        
        
    def cargar_inst(self):
        fileChooser = Tk()
        fileChooser.withdraw()
        self.instinfo = askopenfilename(filetypes = (("data files","*.lfp"),("all files","*.*")))
        fileChooser.destroy()


    def readfile_data(self,*args):
        entrada = ''
        try:
            file = open(self.datainfo, encoding='utf-8')
            for line in file:
                entrada += line
            file.close()
            self.lexicodata = lexicodata.LexicoData()
            self.lexicodata.escanear(entrada)  
        except FileNotFoundError:
            print('> No se encontró ningun archivo') 
            
    
    def readfile_inst(self,*args):
        entrada = ''
        try:
            file = open(self.instinfo, encoding='utf-8')
            for line in file:
                entrada += line
            file.close()
            self.lexicoinst = lexicoints.LexicoInst()
            self.lexicoinst.escanear(entrada) 
        except FileNotFoundError:
            print('> No se encontró ningun archivo')

