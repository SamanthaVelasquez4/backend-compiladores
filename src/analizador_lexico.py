import ply.lex as lex

# Definir los tokens
tokens = (
    'CANTIDAD',
    'MONEDA',
    'FIN',
)

# Definir las expresiones regulares para cada token
t_CANTIDAD = r'\d+\.?\d+'
t_MONEDA = r'DólarEstadounidense|LempiraHondureño|Euro'
t_FIN = r'\bfin\b'

# Ignorar espacios en blanco y saltos de línea
t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at position {t.lexpos}")
    t.lexer.skip(1)  # O bien, puedes usar t.lexer.skip(n) para ignorar n caracteres

# Crear el lexer
lexer = lex.lex()

def analizar_lexico(entrada):
    lexer.input(entrada)
    tokensFinales = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokensFinales.append((tok.type, tok.value))
        print(tokensFinales)
    return tokensFinales
