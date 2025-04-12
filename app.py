import tkinter as tk
from tkinter import *
from tkinter import ttk
from utils.config import Config
from analizadores.sintactico import Yax
from analizadores.lexico import Lexer

class App():
    def __init__(self,root):
        self.root = root
        self.root.title("Conversor de Divisas")

        self.divisas = Config.divisas
        self.lexer = Lexer()
        self.yax = Yax()
    
        self.cantidad = tk.StringVar(root,"0.0")
        self.cantidad.trace('wu',self.updateCadena)
        self.origen = tk.StringVar(root,"")
        self.origen.trace('wu',self.updateCadena)
        self.destino = tk.StringVar(root,"")
        self.destino.trace('wu',self.updateCadena)

        self.resultado = tk.StringVar(root,"0.0")

        self.operadores =   {
                            "cantidad":0,
                            "origen": "",
                            "destino": ""
                            }
        
        self.cadena = tk.StringVar(root,"$")

        self.makeWidgets(root)

    def makeWidgets(self,root):
        self.resultFrame = tk.Frame(root)
        self.resultFrame.pack(side="left",fill="both")
        self.detailFrame = tk.Frame(root)
        self.detailFrame.pack(side="right",fill="both")

        #Label Cantidad
        self.labelCantidad = tk.Label(self.resultFrame)
        self.labelCantidad["text"] = "Cantidad:"
        self.labelCantidad.grid(row=0,column=0,padx=10,pady=10)

        #entryCantidad
        self.entryCantidad = tk.Entry(self.resultFrame)
        self.entryCantidad["textvariable"] = self.cantidad
        #self.entryCantidad.bind("<Key>",self.)
        self.entryCantidad.grid(row=1,column=0,padx=10,pady=10)

        #Label Origen
        self.labelOrigen = tk.Label(self.resultFrame)
        self.labelOrigen["text"] = "Origen:"
        self.labelOrigen.grid(row=0,column=1,padx=10,pady=10)

        #ComboBox Origen
        self.comboBoxOrigen = ttk.Combobox(self.resultFrame)
        self.comboBoxOrigen["textvariable"] = self.origen
        self.comboBoxOrigen["state"] = "readonly"
        self.comboBoxOrigen["values"] = self.divisas
        self.comboBoxOrigen.grid(row=1,column=1,padx=10,pady=10)

        #Label Resultado
        self.labelResultado = tk.Label(self.resultFrame)
        self.labelResultado["text"] = "Resultado:"
        self.labelResultado.grid(row=2,column=0,padx=10,pady=10)

        #Entry Resultado
        self.entryResultado = tk.Entry(self.resultFrame)
        self.entryResultado["textvariable"] = self.resultado
        self.entryResultado["state"] = "readonly"
        self.entryResultado.grid(row=3,column=0,padx=10,pady=10)

        #Label Destino
        self.labelDestino = tk.Label(self.resultFrame)
        self.labelDestino["text"] = "Destino:"
        self.labelDestino.grid(row=2,column=1,padx=10,pady=10)

        #ComboBox Destino
        self.comboBoxDestino = ttk.Combobox(self.resultFrame)
        self.comboBoxDestino["textvariable"] = self.destino
        self.comboBoxDestino["state"] = "readonly"
        self.comboBoxDestino["values"] = self.divisas
        self.comboBoxDestino.grid(row=3,column=1,padx=10,pady=10)

        #Button Calcular
        self.buttonCalcular = ttk.Button(self.resultFrame, command=self.calcularResultado)
        self.buttonCalcular["text"] = "Calcular"
        self.buttonCalcular.grid(row=4,column=0,padx=10,pady=10)

        ############# DETAIL FRAME ###################
        #Label Cadena
        self.labelCadena = tk.Label(self.detailFrame)
        self.labelCadena["text"] = "Cadena a Analizar:"
        self.labelCadena.grid(row=0,padx=10,pady=10)

        #Entry Cadena
        self.entryCadena = tk.Entry(self.detailFrame)
        self.entryCadena["textvariable"] = self.cadena
        #self.entryCadena["state"] = "readonly"
        self.entryCadena.grid(row=1,padx=10,pady=10)

        #Label Detalles
        self.labelDetalles = tk.Label(self.detailFrame)
        self.labelDetalles["text"] = "Detalles del Analisis:"
        self.labelDetalles.grid(row=2,padx=10,pady=10)

        #Textbox Detalles
        self.textboxDetalles = tk.Text(self.detailFrame)
        #self.textboxDetalles["state"] = tk.DISABLED
        self.textboxDetalles.grid(row=3,padx=10,pady=10)

    def updateCadena(self,*args):
        self.operadores["cantidad"] = self.cantidad.get()
        self.operadores["origen"] = self.origen.get()
        self.operadores["destino"] = self.destino.get()

        self.cadena.set(f"{self.operadores["cantidad"]} {self.operadores["origen"]} {self.operadores["destino"]} $")

    def calcularResultado(self):
        self.yax.parser.parse(self.cadena.get(), lexer=self.lexer.lexer)

        detailTable = "\n".join(self.lexer.tokenTable) + "\n"+ "\n".join(self.yax.productionsTable)

        self.resultado.set(self.yax.resultado)
        self.textboxDetalles.delete("1.0", tk.END)
        self.textboxDetalles.insert(tk.INSERT,detailTable)

        #Limpiar las tablas de informacion
        self.lexer.tokenTable = []
        self.yax.productionsTable = []      
        self.lexer.errorsTable = []


