import pydot

# Función para analizar la sintaxis (validar estructura esperada de los tokens)
def analizar_sintaxis(tokens):
    """
    Analiza la sintaxis de los tokens generados.
    :param tokens: Lista de tuplas con formato (tipo, valor)
    :return: Booleano indicando si la sintaxis es válida.
    """
    estructura_esperada = ["Cantidad", "Origen", "Destino"]
    tipos_tokens = [tipo for tipo, _ in tokens]

    if tipos_tokens == estructura_esperada:
        return True
    else:
        print(f"Error sintáctico: Se esperaba la estructura {estructura_esperada}, pero se obtuvo {tipos_tokens}")
        return False

# Función para generar el árbol sintáctico
def generar_arbol(tokens):
    """
    Genera un árbol sintáctico a partir de los tokens.
    :param tokens: Lista de tuplas con formato (tipo, valor)
    :return: Objeto de gráfico Pydot
    """
    graph = pydot.Dot("arbol_sintactico", graph_type="digraph", rankdir="TB")
    
    # Nodo raíz
    Inicio = pydot.Node("Inicio", shape="ellipse", style="filled", fillcolor="lightblue")
    graph.add_node(Inicio)

    # Nodo para cada tipo de token y su valor
    for tipo, valor in tokens:
        nodo_token = pydot.Node(f"{tipo}", shape="box", style="rounded,filled", fillcolor="lightgrey")
        graph.add_node(nodo_token)
        
        # Nodo adicional para mostrar el valor debajo del tipo de token
        nodo_valor = pydot.Node(f"{valor}", shape="box", style="rounded,filled", fillcolor="lightyellow")
        graph.add_node(nodo_valor)
        
        # Conectar el nodo tipo con el nodo valor
        graph.add_edge(pydot.Edge(nodo_token, nodo_valor))
        
        # Conectar el nodo tipo con el nodo raíz
        graph.add_edge(pydot.Edge(Inicio, nodo_token))  # Conectar al nodo raíz

    return graph

def mostrar_arbol(arbol):
    arbol.write_png("arbol_sintactico.png")  # Guarda el gráfico como PNG