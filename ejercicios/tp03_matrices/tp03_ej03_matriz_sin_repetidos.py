# TP03 - Ejercicio 03
# Rellena una matriz de N x N con enteros al azar del intervalo [0, N*) sin repetir

import random

def _ingresar_entero(mensaje: str) -> int:
    """
    Contrato:
        Solicita al usuario un numero entero por teclado hasta que sea uno valido

    Precondiciones:
        Ninguna. se acepta cualquier entero positivo, negativo o cero.

    Postcondiciones:
        Devuelve el numero entero ingresado
    """

    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: se debe ingresar un numero entero.")

def _ingresar_cantidad(mensaje: str, minimo: int) -> int:
    """
    Contrato:
        Solicita al usuario un numero entero mayor o igual al minimo hasta que se ingrese uno valido

    Precondiciones:
        Minimo es un numero entero

    Postcondiciones:
        Devuelve el numero entero ingresado, siempre mayor o igual al minimo recibido
    """

    while True:
        numero = _ingresar_entero(mensaje)
        if numero >= minimo:
            return numero
        print(f"Error: el valor debe ser mayor o igual a: {minimo}")


def _generar_matriz_sinrepetidos(n: int) -> list[list[int]]:
    """
    Contrato:
        Genera una matriz de n x n con los enteros del intervalo [0, n * n) al azar, de forma tal que ningun numero se repita

    Precondiciones:
        n es un numero entero mayor que cero

    Postcondiciones:
        Devuelve una matriz de n filas por n columnas que contiene exactamente una vez cada numero entero desde 0 hasta n * n - 1, en un orden al azar
    """

    numeros = list(range(n * n))
    random.shuffle(numeros)

    matriz = []
    for fila in range(n):
        inicio = fila * n
        matriz.append(numeros[inicio:inicio + n])
    return matriz

def _imprimir_matriz(matriz: list[list[int]]) -> None:
    """
    Contrato:
        Muestra por pantalla la matriz recibida una fila por renglon

    Precondiciones:
        Matriz es una lista de listas de numeros

    Postcondiciones:
        No modifica la matriz solo la imprime
    """

    for fila in matriz:
        renglon = ""
        for valor in fila:
            renglon += f"{valor:>6}"
        print(renglon)


def main() -> None:
    """
    Contrato:
        Ejecuta el programa como principal  generando la matriz sin repetidos y imprimiendola por pantalla

    Precondiciones:
        El archivo debe ejecutarse como programa principal

    Postcondiciones:
        Muestra por pantalla los resultados del ejercicio
    """

    n = _ingresar_cantidad("Ingrese el tamaño N de la matriz: ", 1)

    matriz = _generar_matriz_sinrepetidos(n)

    print(f"\nMatriz de {n} x {n} con los numeros del 0 al {n * n - 1} sin repetir:")
    _imprimir_matriz(matriz)

if __name__ == "__main__":
    main()