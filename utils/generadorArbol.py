from lark import Lark,tree
import subprocess

import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'


class GeneradorArbol():
    
    def __init__(self):
        self.gramatica = """
            conversion: cantidad origen destino END

            cantidad: NUMERO | NUMERO PUNTO NUMERO
            origen: MONEDA
            destino: MONEDA

            NUMERO: /[0-9]+/
            PUNTO: "."
            MONEDA: "Euros"|"Lempiras"|"Dolares"|"Pesos"
            END: "$"

            %import common.WS
            %ignore WS
        """

        self.parser = Lark(self.gramatica,start='conversion')      ##start se refiere al simbolo inicial

    def generarArbol(self,cadena):
        #tree.pydot__tree_to_dot( self.parser.parse("1.2 Dolares Lempiras $"), 'tree.dot')
        #p = subprocess.call(["dot", "-Tpng", "tree.dot"], stdout=open("output.png", "wb"))       #dot -Tpng input.dot > output.png
        tree.pydot__tree_to_png( self.parser.parse(cadena), 'tree.png')

        return self.parser.parse(cadena).pretty()
    
    