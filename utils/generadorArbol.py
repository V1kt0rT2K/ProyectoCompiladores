from lark import Lark,tree
import os
import sys

if(sys.platform.startswith('win32')):
    os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'
elif(sys.platform.startswith('darwin')):
    os.environ["PATH"] += os.pathsep + '/usr/local/bin'
elif(sys.platform.startswith('linux')):
    os.environ["PATH"] += os.pathsep + '/usr/bin'


class GeneradorArbol():
    def __init__(self):
        self.gramatica = """
            conversion: cantidad origen destino END

            cantidad: NUMERO | NUMERO PUNTO NUMERO
            origen: MONEDA
            destino: MONEDA

            NUMERO: /[0-9]+/
            PUNTO: "."
            MONEDA: "Euros"|"Lempiras"|"Dolares"|"Pesos"|"Yenes"|"Libras"|"Bitcoin"
            END: "$"

            %import common.WS
            %ignore WS
        """
        self.parser = Lark(self.gramatica, start='conversion')      ##start se refiere al simbolo inicial

    def generarArbol(self,cadena):
        #tree.pydot__tree_to_dot( self.parser.parse("1.2 Dolares Lempiras $"), 'tree.dot')
        #p = subprocess.call(["dot", "-Tpng", "tree.dot"], stdout=open("output.png", "wb"))       #dot -Tpng input.dot > output.png
        os.makedirs('assets', exist_ok=True)
        tree.pydot__tree_to_png( self.parser.parse(cadena), 'assets/tree.png')

        return self.parser.parse(cadena).pretty()
    
    