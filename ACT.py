import math
from collections import Counter

# Diccionario para convertir direcciones del viento a grados
direcciones_viento = {
    "N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5, "E": 90,
    "ESE": 112.5, "SE": 135, "SSE": 157.5, "S": 180,
    "SSW": 202.5, "SW": 225, "WSW": 247.5, "W": 270,
    "WNW": 292.5, "NW": 315, "NNW": 337.5
}

# Diccionario inverso para convertir grados a direcciones
grados_a_direccion = {v: k for k, v in direcciones_viento.items()}


class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self):
        temperaturas = []
        humedades = []
        presiones = []
        velocidades_viento = []
        direcciones = []

        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:
                if linea.startswith("Estacion"):
                    partes = linea.split()

                    # Extraer datos
                    temperatura = float(partes[11].rstrip(','))
                    humedad = float(partes[13])
                    presion = float(partes[15])
                    velocidad_viento = float(partes[17].split(',')[0])
                    direccion_viento = partes[17].split(',')[1].strip()

                    # Agregar a las listas correspondientes
                    temperaturas.append(temperatura)
                    humedades.append(humedad)
                    presiones.append(presion)
                    velocidades_viento.append(velocidad_viento)
                    direcciones.append(direccion_viento)

        # Calcular promedios
        temp_prom = sum(temperaturas) / len(temperaturas)
        hum_prom = sum(humedades) / len(humedades)
        presion_prom = sum(presiones) / len(presiones)
        vel_viento_prom = sum(velocidades_viento) / len(velocidades_viento)

        # Calcular la dirección predominante del viento
        direcciones_grados = [direcciones_viento[d] for d in direcciones]
        contador_direcciones = Counter(direcciones_grados)
        direccion_predominante = grados_a_direccion[contador_direcciones.most_common(1)[0][0]]

        return temp_prom, hum_prom, presion_prom, vel_viento_prom, direccion_predominante