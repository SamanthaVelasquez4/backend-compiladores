import ply.yacc as yacc
from src.analizador_lexico import tokens  # Importar los tokens generados por el analizador léxico

# Reglas de la gramática
def p_instruccion(p):
    '''instruccion : CANTIDAD MONEDA MONEDA FIN'''
    p[0] = [("CANTIDAD", float(p[1])), ("ORIGEN", p[2]), ("DESTINO", p[3]), ("FIN", p[4])]

def p_error(p):
    if p:
        print(f"Error sintáctico: Token inesperado '{p.value}' en la posición {p.lexpos}.")
    else:
        print("Error sintáctico: Fin de entrada inesperado.")

# Crear el parser
parser = yacc.yacc()

# Función para analizar sintácticamente
def analizar_sintaxis(entrada):
    """
    Analiza la sintaxis de la entrada.
    :param entrada: Cadena de texto con la instrucción a analizar.
    :return: Resultado del análisis o None si hay errores sintácticos.
    """
    resultado = parser.parse(entrada)
    if resultado:
        print("Análisis sintáctico exitoso:", resultado)
        return resultado
    else:
        print("Análisis sintáctico fallido.")
        return None