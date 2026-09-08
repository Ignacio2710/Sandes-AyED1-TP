# TP02 - Ejercicio 02
# Genera una lista de N numeros al azar del 1 al1 00 verifica si tiene elementos repeditos y arma una nueva lista con los elementos unicos de la original

import random

VALOR_MIN = 1
VALOR_MAX = 100

def _ingresar_entero(mensaje: str) -> int:
    """
    contrato:
        solicita al usuario un entero mayor a cero por teclado hasta que se ingrese uno

    Precondiciones:
        ninguna
    
    Postcondicioens:
        Devuelve el numero entero ingresado, siempre que sea mayor a cero
    """

    while True:
        try:
            numero = int(input(mensaje))
        except ValueError:
            print("Error: se debe ingresar un entero.")
        else:
            if numero > 0:
                return numero
            print("Error: la cantidad debe ser mayor a cero")


def _generar_lista_azar(cantidad: int) -> list[int]:
    """
    Contrato:
        Genera una lista con la cantidad de numeros enteros al azar que se pide, comprendidos entre VALOR_MIN y VALOR_MAX

    Precondiciones:
        Cantidad es un entero mayor a cero
    
    Postcondiciones:
        Devuelve una lista de longitud cantidad, donde cada elemento esta entre VALOR_MIN y VALOR_MAX y los incluye

    """
    lista = []
    for _ in range(cantidad):
        lista.append(random.randint(VALOR_MIN, VALOR_MAX))
    return lista


def _tiene_repetidos(lista: list[int]) -> bool:
    """
    Contrato:
        Determina si la lista que recibe contiene algun elemento repetido.

    Precondiciones:
        Ninguna, la lista puede estar vacia.
    
    Postcondiciones:
        Devuelve True si hay almenos un elemento que aparece mas de una ves y False en caso contrario no modifica la lista
    """

    for i in range(len(lista)):
        for num in range(i + 1, len(lista)):
            if lista[i] == lista[num]:
                return True
    return False


def _elementos_unicos(lista: list[int]) -> list[int]:
    """
    Contrato:
        Arma una nueva lista con los elementos unicos de l alista recibida, sin importar el orden en el que queden

    Precondiciones:
        Ninguna, la lista puede estar vacia

    Postcondiciones:
        Devuelve una lista nueva donde cada valor de la original aparece una sola ves no modifica la lista recibida
    """

    unicos = []
    for elementos in lista:
        if elementos not in unicos:
            unicos.append(elementos)
    return unicos

def main() -> None:
    """
    Contrato:
        Ejercuta el programa principal pide N, genera la ista al azar informa si tiene repetidos y muestra la lista de elementos unicos

    Precondiciones:
        El archivo se tiene que ejecutar como principal
    
    Postcondiciones:
        Se muestra por pantalla los resultados del ejercicio.
    """
    cantidad = _ingresar_entero("Ingrese la cantidad de numeros para generara: ")
    numeros = _generar_lista_azar(cantidad)
    print(f"Lista generada: {numeros}")

    if _tiene_repetidos(numeros):
        print("La lista tiene elementos repetidos.")
    else:
        print("La lista no tiene elementos repetidos.")
    print(f"Lista: {numeros}")

    unicos = _elementos_unicos(numeros)
    print(f"Elementos unicos: {unicos}")
    print(f"cantidad de elementos unicos {len(unicos)}")
    print(f"Lista original: {numeros}")


if __name__ == "__main__":
    main()