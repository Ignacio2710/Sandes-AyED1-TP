# TP03 - Ejercicio 04
# Genera al azar la produccion semanal de N fabricas de bicicletas y calcula totales, maximos por dia y por fabrica y el minimo de cada una.

import random

DIAS = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
MAXIMO_DIARIO = 150


def _ingresar_entero(mensaje: str) -> int:
    """
    Contrato:
        Solicita al usuario un numero entero por teclado hasta que sea uno valido

    Precondiciones:
        Ninguna

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


def _cargar_produccion(cantidad_fabricas: int) -> list[list[int]]:
    """
    Contrato:
        Genera al azar la produccion de una semana para cada fabrica (punto a)

    Precondiciones:
        cantidad_fabricas es un numero entero mayor a cero

    Postcondiciones:
        Devuelve una matriz con una fila por fabrica y una columna por dia, los valores son entre 0 y el maximo diario no solicita datos
    """

    matriz = []
    for fabrica in range(cantidad_fabricas):
        fila = []
        for dia in range(len(DIAS)):
            fila.append(random.randint(0, MAXIMO_DIARIO))
        matriz.append(fila)
    return matriz


"""
def _mostrar_produccion(matriz: list[list[int]]) -> None:
    
    Contrato:
        Muestra por pantalla la produccion de cada fabrica dia por dia

    Precondiciones:
        Matriz tiene una fila por fabrica y una columna por cada dia de DIAS

    Postcondiciones:
        No modifica l amatriz solo la imprime
    """


def _totales_por_fabrica(matriz: list[list[int]]) -> list[int]:
    """
    Contrato:
        Calcula el total de bicicletas fabricadas por cada fabrica en la semana (punto b)
    
    Precondiciones:
        Matriz tiene una fila por fabrica y una columna por dia

    Postcondiciones:
        Devuelve una lista con un total por fabrica en el mismo orden que filas no modifica la matriz
    """

    totales = []
    for fila in matriz:
        total = 0
        for valor in fila:
            total += valor
        totales.append(total)
    return totales


"""
def mayor_produccion_en_un_dia():

    Contrato:
        Busca la mayor cantidad producida por una fabrica en un solo dia (punto c)

    Precondiciones:
    
    Postcondiciones:
        Devuelve ua lista de tres elementos el numero de fabrica, numero de dia y cantidad producida no modifiaca la matriz

        
def _totales_por_dia():
    
    Contrato :
        Calcula el total de bicicletas fabricadas cada dia sumando todas las fabricas

    Precondiciones:
        Matriz tiene al menos una fila y todas las filas tienen la misma longitud

    Postcondiciones:
        Devuelve una lista con un total por dia en el mismo orden que las columnas no modifica la matriz
    
"""


def _dia_mas_productivo(totales: list[int]) -> int:
    """
    Contrato:
        Determina cual es el dia mas productivo considerando todas las fabricas (punto d)

    Precondiciones:
        Totales des una lista no vacia con el total producido en cada dia

    Postcondiciones:
        Devuelve el numero del dia con mayor total si hay empate devuelve el primero no modifica la lista
    """

    mejor_dia = 0
    for dia in range(len(totales)):
        if totales[dia] > totales[mejor_dia]:
            mejor_dia = dia
    return mejor_dia


def _minimos_por_fabrica(matriz: list[list[int]]) -> list[int]:
    """
    Contrato:
        Arma por comprension una lista con la menor cantidad fabricada por cada fabrica (punto e)

    Precondiciones:
        Matriz tiene una fila por fabrica y ninguna fila esta vacia

    Postcondiciones:
        Devuelve una lista con un minimo por fabrica, en el mismo orden que las filas no modifica la matriz
    """

    return [min(fila) for fila in matriz]


def main() -> None:
    """
    Contrato:
        Ejecuta el programa como principal 

    Precondiciones:
        El archivo debe ejecutarse como programa principal

    Postcondiciones:
        Muestra por pantalla los resultados del ejercicio
    """

    cantidad_fabricas = _ingresar_cantidad("Ingrese la cantidad de fabricas: ", 1)

    matriz = _cargar_produccion(cantidad_fabricas)
    print("\nProduccion de la semana (punto a):")
    print(matriz)

    print("\nTotal por fabrica (punto b): ")
    totales_fabrica = _totales_por_fabrica(matriz)
    for fabrica in range(len(totales_fabrica)):
        print(f"La fabrica {fabrica + 1} fabrico {totales_fabrica[fabrica]} bicicletas.")

    print("\nMenor cantidad fabricada por cada fabrica (punto e): ")
    print(_minimos_por_fabrica(matriz))

if __name__ == "__main__":
    main()