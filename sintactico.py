from ply import yacc
from lexico import Lexer
from config import Config
from conversor import Conversor

class Yax:

    def p_conversion(self, p):
        '''conversion : cantidad origen destino'''
        p[0] = str(p[1]) + p[2] + p[3]
        print(p[1],p[2],p[3])
        print(
            self.conversor.conversion(
            float(p[1]), p[2],p[3])
            )
        
        self.productionsTable.append(f"conversion: {p[0]}")

    def p_origen(self,p):
        '''origen : MONEDA'''
        p[0] = p[1]
        self.productionsTable.append(f"origen:{p[1]}")

    def p_destino(self,p):
        '''destino : MONEDA'''
        p[0] = p[1]
        self.productionsTable.append(f"destino:{p[1]}")
        

    def p_cantidad(self,p):
        '''cantidad : NUMERO
                    | NUMERO PUNTO NUMERO'''
        if(len(p) == 2):
            p[0] = p[1]
        elif(len(p) == 4):
            p[0] = str(p[1])+p[2]+str(p[3])
        self.productionsTable.append(f"cantidad: {p[0]}")

        
    def p_error(self,p):
        print("Syntax error in input!")

    def __init__(self):
        self.productionsTable = []
        
        self.conversor = Conversor()

        self.tokens = Config.tokens
        self.parser = yacc.yacc(module=self)



lexer = Lexer()
yax = Yax()

yax.parser.parse('20.1 Dolares Euros',lexer=lexer.lexer)

print("\n".join(lexer.tokenTable))
print("\n".join(yax.productionsTable))
