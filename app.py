import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkfont
from analizadores.lexico import Lexer
from analizadores.sintactico import Yax
from utils.config import Config
from utils.generadorArbol import GeneradorArbol
from PIL import Image

class App():
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Divisas - Análisis Léxico/Sintáctico")
        self.root.geometry('1100x600')
        self.root.resizable(0,0)
        self.root.configure(bg='#f0f2f5')
        
        try:
            self.custom_font = tkfont.Font(family="Segoe UI", size=10)
            self.title_font = tkfont.Font(family="Segoe UI", size=12, weight="bold")
        except:
            self.custom_font = tkfont.Font(size=10)
            self.title_font = tkfont.Font(size=12, weight="bold")
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f2f5')
        self.style.configure('TLabel', background='#f0f2f5', font=self.custom_font)
        self.style.configure('TButton', font=self.custom_font, padding=6)
        self.style.configure('TCombobox', font=self.custom_font, padding=5)
        self.style.configure('TEntry', font=self.custom_font, padding=5)
        self.style.map('TButton', 
                      foreground=[('active', '!disabled', 'black')], 
                      background=[('active', '#4a6da7')])
        
        self.primary_color = '#2c3e50'
        self.secondary_color = '#3498db'
        self.accent_color = '#e74c3c'
        self.light_color = '#ecf0f1'
        self.dark_color = '#2c3e50'
        
        self.divisas = Config.divisas
        self.lexer = Lexer()
        self.yax = Yax()
        
        self.cantidad = tk.StringVar(root, "0.0")
        self.cantidad.trace('wu', self.updateCadena)
        self.origen = tk.StringVar(root, "")
        self.origen.trace('wu', self.updateCadena)
        self.destino = tk.StringVar(root, "")
        self.destino.trace('wu', self.updateCadena)
        self.resultado = tk.StringVar(root, "0.0")
        self.cadena = tk.StringVar(root, "$")
        
        self.create_widgets()
    
    def create_widgets(self):

        self.main_frame = ttk.Frame(self.root, padding=(20, 15))
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.conversion_frame = ttk.LabelFrame(self.main_frame, text=" Conversión de Divisas ", 
                                             padding=(15, 10))
        self.conversion_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        
        self.analisis_frame = ttk.LabelFrame(self.main_frame, text=" Análisis Léxico/Sintáctico ", 
                                           padding=(15, 10))
        self.analisis_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        
        self.create_conversion_widgets()
        
        self.create_analysis_widgets()
        
        self.footer_label = ttk.Label(self.main_frame, 
                                     text="Proyecto de Análisis Léxico/Sintáctico - Conversor de Divisas",
                                     foreground='#7f8c8d')
        self.footer_label.grid(row=1, column=0, columnspan=2, pady=(10, 0))
    
    def create_conversion_widgets(self):
        # Cantidad
        ttk.Label(self.conversion_frame, text="Cantidad:", font=self.custom_font).grid(
            row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.entry_cantidad = ttk.Entry(self.conversion_frame, textvariable=self.cantidad, 
                                      font=self.custom_font)
        self.entry_cantidad.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        
        # Moneda origen
        ttk.Label(self.conversion_frame, text="Moneda Origen:", font=self.custom_font).grid(
            row=2, column=0, padx=5, pady=5, sticky="w")
        
        self.combo_origen = ttk.Combobox(self.conversion_frame, textvariable=self.origen, 
                                        values=self.divisas, state="readonly", font=self.custom_font)
        self.combo_origen.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        
        # Moneda destino
        ttk.Label(self.conversion_frame, text="Moneda Destino:", font=self.custom_font).grid(
            row=4, column=0, padx=5, pady=5, sticky="w")
        
        self.combo_destino = ttk.Combobox(self.conversion_frame, textvariable=self.destino, 
                                         values=self.divisas, state="readonly", font=self.custom_font)
        self.combo_destino.grid(row=5, column=0, padx=5, pady=5, sticky="ew")
        
        # Resultado
        ttk.Label(self.conversion_frame, text="Resultado:", font=self.custom_font).grid(
            row=6, column=0, padx=5, pady=5, sticky="w")
        
        self.entry_resultado = ttk.Entry(self.conversion_frame, textvariable=self.resultado, 
                                       state="readonly", font=self.custom_font)
        self.entry_resultado.grid(row=7, column=0, padx=5, pady=5, sticky="ew")
        
        # Botones
        button_frame = ttk.Frame(self.conversion_frame)
        button_frame.grid(row=8, column=0, pady=(10, 0), sticky="ew")
        
        self.btn_calcular = ttk.Button(button_frame, text="Calcular Conversión", 
                                     command=self.calcularResultado, style='Accent.TButton')
        self.btn_calcular.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        self.btn_arbol = ttk.Button(button_frame, text="Generar Árbol", 
                                  command=self.generarArbol)
        self.btn_arbol.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        self.style.configure('Accent.TButton', foreground='white', 
                           background=self.secondary_color)
        self.style.map('Accent.TButton', 
                      background=[('active', self.secondary_color)])
        
        # Configurar pesos de grid
        self.conversion_frame.columnconfigure(0, weight=1)
    
    def create_analysis_widgets(self):
        # Cadena de análisis
        ttk.Label(self.analisis_frame, text="Cadena a Analizar:", font=self.custom_font).grid(
            row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.entry_cadena = ttk.Entry(self.analisis_frame, textvariable=self.cadena, 
                                     font=self.custom_font)
        self.entry_cadena.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        
        # Pestañas para los resultados
        self.notebook = ttk.Notebook(self.analisis_frame)
        self.notebook.grid(row=2, column=0, padx=5, pady=(5, 0), sticky="nsew")
        
        # Pestaña de tokens
        self.tab_tokens = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_tokens, text="Tokens")
        
        self.text_tokens = tk.Text(self.tab_tokens, wrap=tk.WORD, font=self.custom_font, 
                                  padx=10, pady=10, height=10)
        self.scroll_tokens = ttk.Scrollbar(self.tab_tokens, command=self.text_tokens.yview)
        self.text_tokens.configure(yscrollcommand=self.scroll_tokens.set)
        
        self.text_tokens.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll_tokens.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Pestaña de producciones
        self.tab_productions = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_productions, text="Producciones")
        
        self.text_productions = tk.Text(self.tab_productions, wrap=tk.WORD, font=self.custom_font, 
                                       padx=10, pady=10, height=10)
        self.scroll_productions = ttk.Scrollbar(self.tab_productions, command=self.text_productions.yview)
        self.text_productions.configure(yscrollcommand=self.scroll_productions.set)
        
        self.text_productions.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll_productions.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Pestaña de errores léxicos
        self.tab_lex_errors = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_lex_errors, text="Errores Léxicos")
        
        self.text_lex_errors = tk.Text(self.tab_lex_errors, wrap=tk.WORD, font=self.custom_font, 
                                     padx=10, pady=10, height=5, foreground='#c0392b')
        self.scroll_lex_errors = ttk.Scrollbar(self.tab_lex_errors, command=self.text_lex_errors.yview)
        self.text_lex_errors.configure(yscrollcommand=self.scroll_lex_errors.set)
        
        self.text_lex_errors.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll_lex_errors.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Pestaña de errores sintácticos
        self.tab_sint_errors = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_sint_errors, text="Errores Sintácticos")
        
        self.text_sint_errors = tk.Text(self.tab_sint_errors, wrap=tk.WORD, font=self.custom_font, 
                                      padx=10, pady=10, height=5, foreground='#8e44ad')
        self.scroll_sint_errors = ttk.Scrollbar(self.tab_sint_errors, command=self.text_sint_errors.yview)
        self.text_sint_errors.configure(yscrollcommand=self.scroll_sint_errors.set)
        
        self.text_sint_errors.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll_sint_errors.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Configurar pesos de grid
        self.analisis_frame.columnconfigure(0, weight=1)
        self.analisis_frame.rowconfigure(2, weight=1)
    
    def updateCadena(self, *args):
        cantidad = self.cantidad.get()
        origen = self.origen.get()
        destino = self.destino.get()

        self.cadena.set(f"{cantidad} {origen} {destino} $")
    
    def generarArbol(self):
        try:
            g = GeneradorArbol()
            g.generarArbol(self.cadena.get())

            i = Image.open('assets/tree.png')
            i.show()
            messagebox.showinfo("Árbol Generado", "El árbol sintáctico se ha generado como 'tree.png'")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el árbol: {str(e)}")
            self.text_sint_errors.insert(tk.END, f"\nError al generar árbol: {str(e)}")
    
    def calcularResultado(self):
        try:
            
            # Realizar el análisis
            self.yax.parser.parse(self.cadena.get(), lexer=self.lexer.lexer)
            
            # Mostrar tokens
            self.text_tokens.delete(1.0, tk.END)
            if self.lexer.tokenTable:
                self.text_tokens.insert(tk.END, "TOKENS ENCONTRADOS:\n\n")
                self.text_tokens.insert(tk.END, "\n".join(self.lexer.tokenTable))
            else:
                self.text_tokens.insert(tk.END, "No se encontraron tokens.")
            
            # Mostrar producciones
            self.text_productions.delete(1.0, tk.END)
            if self.yax.productionsTable:
                self.text_productions.insert(tk.END, "PRODUCCIONES:\n\n")
                self.text_productions.insert(tk.END, "\n".join(self.yax.productionsTable))
            else:
                self.text_productions.insert(tk.END, "No se encontraron producciones.")
            
            # Mostrar errores léxicos
            self.text_lex_errors.delete(1.0, tk.END)
            if self.lexer.errorsTable:
                self.text_lex_errors.insert(tk.END, "ERRORES LÉXICOS:\n\n")
                self.text_lex_errors.insert(tk.END, "\n".join(self.lexer.errorsTable))
            else:
                self.text_lex_errors.insert(tk.END, "No se encontraron errores léxicos.")
            
            # Mostrar errores sintácticos
            self.text_sint_errors.delete(1.0, tk.END)
            if self.yax.errorsTable:
                self.text_sint_errors.insert(tk.END, "ERRORES SINTÁCTICOS:\n\n")
                self.text_sint_errors.insert(tk.END, "\n".join(self.yax.errorsTable))
            else:
                self.text_sint_errors.insert(tk.END, "No se encontraron errores sintácticos.")
            
            # Actualizar resultado
            self.resultado.set(self.yax.resultado)
            
            # Mostrar advertencia si hay errores
            if self.lexer.errorsTable or self.yax.errorsTable:
                messagebox.showwarning("Advertencia", 
                                    "Se encontraron errores durante el análisis. Revise las pestañas de errores para más detalles.")
                
            
            # Limpiar las tablas despues del nuevo análisis
            self.lexer.tokenTable = []
            self.yax.productionsTable = []
            self.lexer.errorsTable = []
            self.yax.errorsTable = []
            
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante el análisis: {str(e)}")
            self.text_sint_errors.insert(tk.END, f"\nError inesperado: {str(e)}")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()