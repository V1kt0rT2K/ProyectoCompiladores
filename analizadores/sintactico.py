from ply import yacc
from analizadores.lexico import Lexer
from utils.config import Config
from utils.conversor import Conversor

class Yax:

    def p_conversion(self, p):
        '''conversion : cantidad origen destino END'''
        p[0] = str(p[1]) + p[2] + p[3]
        self.resultado = self.conversor.conversion(float(p[1]), p[2],p[3])
        
        self.productionsTable.append(f"PRODUCTION :: conversion : {p[0]}")

    def p_origen(self,p):
        '''origen : MONEDA'''
        p[0] = p[1]
        self.productionsTable.append(f"PRODUCTION :: origen :{p[1]}")

    def p_destino(self,p):
        '''destino : MONEDA'''
        p[0] = p[1]
        self.productionsTable.append(f"PRODUCTION :: destino :{p[1]}")
        

    def p_cantidad(self,p):
        '''cantidad : NUMERO
                    | NUMERO PUNTO NUMERO'''
        if(len(p) == 2):
            p[0] = p[1]
        elif(len(p) == 4):
            p[0] = str(p[1])+p[2]+str(p[3])
        self.productionsTable.append(f"PRODUCTION :: cantidad : {p[0]}")

        
    def p_error(self,p):
        print("Syntax error in input!")
        self.errorsTable.append(f"Syntax error in input")

    def __init__(self):
        self.productionsTable = []
        self.errorsTable = []

        self.resultado = 0
        self.conversor = Conversor()
        self.tokens = Config.tokens
        
        self.parser = yacc.yacc(module=self)




