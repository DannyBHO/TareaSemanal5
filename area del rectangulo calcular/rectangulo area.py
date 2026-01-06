"""
Programa: Cálculo del área de un rectángulo
Descripción: Este programa solicita al usuario la base y la altura de un rectángulo,
valida los datos ingresados y calcula el área utilizando una función.
Se aplican tipos de datos básicos e identificadores con snake_case.
Autor: Estudiante
"""

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    Parámetros:
        base (float): base del rectángulo
        altura (float): altura del rectángulo
    Retorna:
        float: área del rectángulo
    """
    return base * altura


# Solicita datos al usuario
nombre_usuario = input("Ingrese su nombre: ")  # tipo string
base = float(input("Ingrese la base del rectángulo: "))  # tipo float
altura = float(input("Ingrese la altura del rectángulo: "))  # tipo float

# Verifica si los valores ingresados son positivos
datos_validos = base > 0 and altura > 0  # tipo boolean

# Proceso principal
if datos_validos:
    area_rectangulo = calcular_area_rectangulo(base, altura)  # tipo float
    print(f"{nombre_usuario}, el área del rectángulo es: {area_rectangulo}")
else:
    print("Error: la base y la altura deben ser mayores que cero.")

