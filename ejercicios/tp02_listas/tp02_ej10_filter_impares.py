# TP02 - Ejercicio 10
# Genera una lista de numeros al azar y arma otra con los impares usando filter()

import random 
VALOR_MIN = 1
VALOR_MAX = 100

def _ingresar_entero(mensaje: str) -> int:
    """
    Contrato:
        solicita al usuario un entero hasta que se ingrese uno valido

    Precondiciones:
        Ninguna se acepta enteros positivos, negativos o cero

    Postcondiciones:
        Devuelve el numero entero que se ingreso
    """

    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: se debe ingresar un entero.")


def _ingresar_cantidad(mensaje: str, minimo: int) -> int:
    """
    Contrato:
        Solicita al usuario una cantidad entera mayor o igual al minimo hasta que se ingrese una valida

    Precondiciones:
        Minimo es un numero entero

    Postcondiciones:
        Devuelve el numero entero ingresado, siempre mayor o igual al minimo recibido
    """

    while True:
        numero = _ingresar_entero(mensaje)
        if numero >= minimo:
            return numero
        print(f"Error: el valor debe ser mayor o igual a {minimo}")


def _es_impar(numero: int) -> bool:
    """
    Contrato:
        Determina si un numero entero es impar

    Precondiciones:
        numero es un numero entero
    
    Postcondiciones:
        Devuelve True si el numero es impar y False si es par
    """

    return numero % 2 != 0


def _filtrar_impares(lista: list[int]) -> list[int]:
    """
    Contrato:
        Arma una lista nueva con los elementos impares de la lista que recibe, usando  filter()

    precondiciones:
        La lista contiene numeros enteros y puede estar vacia
    
    Postcondiciones:
        Devuelve una lista nueva con impares en el mismo orden que tenian en la original, no modifica la lista recibida
    """

    return list(filter(_es_impar, lista))


def _generar_lista_al_azar(cantidad: int) -> list[int]:
    """
    Contrato:
        genera una lista con cantidad de numeros enteros al azar que pide, entre VALOR_MIN y VALOR_MAX

    Precondiciones:
        Cantidad es un entero mayor o igual a cero

    Postcondiciones:
        Devuelve una lista nueva de longitud cantidad, donde cada elemento esta entre VALOR_MIN y VALOR_MAX, los dos incluidos
    """
    lista = []
    for _ in range(cantidad):
        lista.append(random.randint(VALOR_MIN, VALOR_MAX))
    return lista


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal genera la lista al azar, filtra impares y muestra las dos listas
    
    Precondiciones:
        El archivo se tiene que ejecutar como principal
    
    Postcondiciones:
        Se muestra por pantalla la lista generada y la de impares
    """

    cantidad = _ingresar_cantidad("Ingresa la cantidad de numeros a generar: ", 1)
    numeros = _generar_lista_al_azar(cantidad)
    impares = _filtrar_impares(numeros)

    print(f"Lista generada: {numeros}")
    print(f"Impares de la lista: {impares}")
    print(f"De {len(numeros)} numeros, {len(impares)} son impares")

if __name__ == "__main__":
    main()