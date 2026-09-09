# TP02 - Ejercicio 06
# Normaliza una lista de numeros enteros para que sus elementos sumen 1.0

def _ingresar_entero(mensaje: str) -> int:
    """
    contrato:
        solicita al usuario un numero entero hasta que se ingrese uno valido.

    Precondiciones:
        se acepta cualquier entero, positivo, negativo o cero
    
    Postcondiciones:
        Devuelve el numero entero ingresado
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
        print(f"Error: el valor debe ser mayor o igual a {minimo}.")


def _ingresar_lista(cantidad: int) -> list[int]:
    """
    Contrato:
        Arma una lista con la cantidad de numeros enteros que el usuario ingresa, repitiendo el pedido
        mientras la suma de esos numeros sea cero
    
    Precondiciones:
        Cantidad es un entero mayor o igual a uno

    Postcondiciones:
        Devuelve una lista nueva de longitud cantidad, con los valores en el orden en que se ingresan y con suma distinta de cero lista para ser normalizada
    """
    while True:
        lista = []
        for posicion in range(cantidad):
            lista.append(_ingresar_entero(f"Valor {posicion + 1}: "))
        if sum(lista) != 0:
            return lista
        print("Error: los valores suman cero y no es posible normalizar carga la lista de nuevo")


def _normalizar(lista: list[int]) -> list[float]:
    """
    Contrato:
        Arma una lista nueva donde cada elemento es la proporcion que le corresponde al elemento original. de manera que todos juntos sumen 1.0

    Precondiciones:
        La lista tiene al menos un elemento y la suma de sus elementos es distinta a cero

    Postcondiciones:
        Devuelve una lista nueva de numeros reales, de la misma longitud que la original y en el mismo orden, cuyos elementos suman 1.0. no modifica la lista recibida
    """

    total = sum(lista)
    normalizada = []
    for numero in lista:
        normalizada.append(numero / total)
    return normalizada


def main() -> None:
    """
    Contrato:
        Ejercuta el programa principal   lista que ingresa el usuario
    
    Precondiciones:
        El archivo se tiene que ejecutar como principal
    
    Postcondiciones:
        Se muestra por pantalla la lista original, la normalizada y la suma de los elementos
    """

    cantidad = _ingresar_cantidad("Ingrese la cantidad de numeros de su lista: ", 1)
    numeros = _ingresar_lista(cantidad)
    normalizada = _normalizar(numeros)

    print()
    print(f"Lista original: {numeros}")
    print(f"Lista normalizada: {normalizada}")
    print(f"Los elementos de la lista normalizada suman {round(sum(normalizada), 10)}")

if __name__ == "__main__":
    main()