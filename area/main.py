"""
Programa: Cálculo del área de un rectángulo
Descripción: Solicita datos al usuario, valida la información
y calcula el área usando funciones y clases.
Autor: Estudiante
"""

from modelo.rectangulo import Rectangulo
from servicios.calculos import calcular_area_rectangulo


# Solicitar datos al usuario
nombre_usuario = input("Ingrese su nombre: ")
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# Validación de datos
datos_validos = base > 0 and altura > 0

if datos_validos:
    rectangulo = Rectangulo(base, altura)
    area = calcular_area_rectangulo(rectangulo.base, rectangulo.altura)
    print(f"{nombre_usuario}, el área del rectángulo es: {area}")
else:
    print("Error: la base y la altura deben ser mayores que cero.")
