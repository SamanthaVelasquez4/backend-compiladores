# convertidor.py
class ConvertidorDivisas:
    def __init__(self):
        # Un diccionario con las tasas de cambio entre algunas divisas
        self.tasas = {
            "DólarEstadounidense": {
                "LempiraHondureño": 24.0,
                "Euro": 0.92,
            },
            "LempiraHondureño": {
                "DólarEstadounidense": 0.042,
                "Euro": 0.038,
            },
            "Euro": {
                "DólarEstadounidense": 1.09,
                "LempiraHondureño": 26.0,
            },
        }

    def convertir(self, cantidad, origen, destino):
        if origen not in self.tasas or destino not in self.tasas[origen]:
            raise ValueError(f"No se encontró la tasa de cambio entre {origen} y {destino}.")
        return cantidad * self.tasas[origen][destino]