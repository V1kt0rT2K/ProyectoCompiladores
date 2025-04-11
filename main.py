from analizadores.lexico import Lexer
from analizadores.sintactico import Yax

lexer = Lexer()
yax = Yax()

yax.parser.parse('20.1 Dolares Euros',lexer=lexer.lexer)

print("\n".join(lexer.tokenTable))
print("\n".join(yax.productionsTable))