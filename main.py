from flask import Flask, jsonify, request, send_file
from src.convertidor import ConvertidorDivisas
from src.analizador_lexico import analizar_lexico
from src.analizador_sintactico import analizar_sintaxis, mostrar_arbol, generar_arbol

app = Flask(__name__)

@app.route("/")
def root():
    return "Servidor levantado correctamente."

@app.route("/convertir")
def convertir():
    cantidad = request.args.get('cantidad')
    origen = request.args.get('origen')
    destino = request.args.get('destino')

    json = {"cantidad": cantidad, "origen": origen, "destino": destino}
    return jsonify(json), 200

@app.route("/post/convertidor", methods = ['POST'])
def convertidor():
    data = request.get_json()

    # Obtener los datos que vienen el request body
    cantidad = data['cantidad']
    origen = data['origen']
    destino = data['destino']

    #convertir
    convertir = ConvertidorDivisas()
    resultado = convertir.convertir(cantidad, origen, destino)

    # Generar tokens para análisis léxico
    entrada = f"{cantidad},{origen},{destino}"
    tokens = analizar_lexico(entrada)
    
    if tokens:
        # Analizar sintaxis
        if analizar_sintaxis(tokens):
            # Generar y mostrar el árbol sintáctico
            arbol = generar_arbol(tokens)
            mostrar_arbol(arbol)
        else:
            return jsonify({'status': False,'message' : "Error Sintáctico : La sintaxis de los tokens no es válida."})
    else:
        return jsonify({'status': False, 'message' : "Error Léxico : La entrada no generó tokens válidos."})

    return jsonify({'status': True, 'message' : "Petición realizada con exito.", 'result': resultado})

@app.route('/get/arbol', methods=['GET'])
def enviar_imagen():
    # Ruta del archivo PNG que quieres enviar
    ruta_imagen = "arbol_sintactico.png"
    return send_file(ruta_imagen, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)

