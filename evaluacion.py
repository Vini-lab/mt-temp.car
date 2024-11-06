from config import RANGO_CARRO_PEQUENO, RANGO_CAMIONETA

def evaluar_temperatura(temperatura, tipo_vehiculo):
    resultado = ""
    sugerencia = ""

    if tipo_vehiculo == "Carro Pequeño":
        rango = RANGO_CARRO_PEQUENO
    elif tipo_vehiculo == "Camioneta":
        rango = RANGO_CAMIONETA
    else:
        return "Tipo de vehículo no válido", ""
    
    # Evaluación de temperatura
    if rango[0] <= temperatura <= rango[1]:
        resultado = "Condición Normal"
    elif temperatura > rango[1]:
        resultado = "¡Sobrecalentamiento!"
        sugerencia = "Posible causa: Falta de agua en el sistema de enfriamiento o exceso de carga."
    else:
        resultado = "Temperatura Baja"
        sugerencia = "Posible causa: El motor podría no estar alcanzando su temperatura óptima. Verificar condiciones de funcionamiento."

    return resultado, sugerencia
