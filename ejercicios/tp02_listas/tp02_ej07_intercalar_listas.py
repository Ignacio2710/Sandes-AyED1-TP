# TP02 - Ejercicio 07
# Intercala los elementos de una lista entre los de otra usando rebanadas

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
        minimo es un numero entero
    
    Postcondiciones:
        Devuelve el numero entero ingresado, siempre mayor o igual al minimo recibido
    """

    while True:
        numero = _ingresar_entero(mensaje)
        if numero >= minimo:
            return numero
        print(f"Error: el valor debe ser mayor o igual a {minimo}")


def _ingresar_lista(nombre: str, cantidad: int) -> list[int]:
    """
    Contrato:
        Arma una lista con la cantidad de numeros enteros que el usuario ingresa por teclado

    Precondiciones:
        Cantidad es un entero mayor o igual a cero

    Postcondiciones:
        Devuelve una lista nueva de longitud cantidad, con los valores en el orden en que se ingresan
    """

    lista = []
    for posicion in range(cantidad):
        lista.append(_ingresar_entero(f"{nombre} - valor {posicion + 1}:"))
    return lista


def _intercalar(lista1: list[int], lista2: list[int]) -> None:
    """
    Contrato:
        Intercala los elementos de lista2 entre los de lista 1 usando solo rebanadas modificando lista1 en lugar de armar una nueva

    Precondiciones:
        Las dos listas tienen numeros enteros, cualquiera de las dos puede estar vacia y pueden tener longitudes distintas

    Postcondiciones:
        Lista 1 queda con sus elementos alternados con los de lista2. Si una de las dos es mas larga, los elementos que sobran quedan al final. lista 2 no se modifica no devuelve nada
    """

    for posicion in range(len(lista2)):
        destino = posicion * 2 + 1
        lista1[destino:destino] = lista2[posicion:posicion + 1]


def main() -> None:
    """
    Contrato:
        Ejercuta el programa principal pide dos listas las intercala y muestra el resultado
    
    Precondiciones:
        El archivo se tiene que ejecutar como principal
    
    Postcondiciones:
        Se muestra por pantalla las dos listas originales y como queda la primera despues de intercalar
    """

    cantidad1 = _ingresar_cantidad("Ingrese la cantidad de numeros de la lista 1: ", 0)
    lista1 = _ingresar_lista("Lista 1", cantidad1)

    cantidad2 = _ingresar_cantidad("Ingresa la cantidad de numeros de la lista 2: ", 0)
    lista2 = _ingresar_lista("Lista 2", cantidad2)

    print()
    print(f"Lista 1 antes: {lista1}")
    print(f"Lista 2: {lista2}")

    _intercalar(lista1, lista2)

    print(f"Lista 1 despues: {lista1}")
    print(f"Lista 2 despues: {lista2}")


if __name__ == "__main__":
    main()