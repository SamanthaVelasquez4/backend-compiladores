import re
# Función para análisis léxico
def analizar_lexico(entrada):
    """
    Analiza léxicamente la entrada según el patrón definido.
    :param entrada: Cadena de texto que se va a analizar
    :return: Lista de tokens como tuplas (tipo, valor)
    """
    print("entrada", entrada)
    # Patrón modificado para manejar separadores por coma
    patron = r"(?P<Cantidad>\d+\.?\d+),\s*(?P<Origen>DólarEstadounidense|LempiraHondureño|Euro),\s*(?P<Destino>LempiraHondureño|DólarEstadounidense|Euro)"
    match = re.match(patron, entrada)
    if not match:
        raise ValueError("Error sintáctico: El formato de entrada no coincide con la estructura esperada")
    
    # Retorna los tokens como pares (nombre, valor)
    tokens = [(key, value) for key, value in match.groupdict().items()]
    return tokens
