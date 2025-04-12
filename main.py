from analizadores.lexico import Lexer
from analizadores.sintactico import Yax
import tkinter as tk
from tkinter import ttk, filedialog
from app import App

root = tk.Tk()
root.geometry('800x400')
root.configure(bg='white')
App(root)
root.mainloop()

# lexer = Lexer()
# yax = Yax()

# yax.parser.parse('20.1 Dolares Euros',lexer=lexer.lexer)

# print("\n".join(lexer.tokenTable))
# print("\n".join(yax.productionsTable))