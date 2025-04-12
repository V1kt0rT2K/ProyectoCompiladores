from ply import lex;
from utils.config import Config

class Lexer:

    def t_PUNTO(self,t):
        r'\.'
        self.tokenTable.append(f"TOKEN :: Valor: {t.value}\t\t Posicion:{t.lexpos}\t\t Tipo:{t.type}")
        return t

    def t_NUMERO(self,t):
        r'[0-9]+'
        t.value = int(t.value)    
        self.tokenTable.append(f"TOKEN :: Valor: {t.value}\t\t Posicion:{t.lexpos}\t\t Tipo:{t.type}")
        return t
        

    def t_MONEDA(self,t):
        r'Dolares|Lempiras|Euros|Pesos'
        t.value = str(t.value)
        self.tokenTable.append(f"TOKEN :: Valor: {t.value}\t\t Posicion:{t.lexpos}\t\t Tipo:{t.type}")    
        return t
    
    def t_END(self,t):
        r'\$'
        #t.value = str(t.value)
        self.tokenTable.append(f"TOKEN :: Valor: {t.value}\t\t Posicion:{t.lexpos}\t\t Tipo:{t.type}")    
        return t

    def t_COMMENT(self,t):
        r'\s+'
        pass

    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        self.errorsTable.append(f"Illegalcharacter: {t.value[0]} at position {t.lexpos}") 
        t.lexer.skip(1)
        
    def build(self,input):
        self.lexer.input(input)

    def __init__(self):
        self.tokens = Config.tokens
        self.tokenTable = []
        self.errorsTable = []
        self.lexer = lex.lex(module=self)
        
# m = Lexer()
# m.build('1.1DolarLempira')

# while True:
#     tok = m.lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)
    

