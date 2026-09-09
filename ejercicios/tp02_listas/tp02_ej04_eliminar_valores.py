# TP02 - Ejercicio 04
# Elimina de una lista de numeros enteros los valores que aparecen en una segunda lista, modifica la lista original sin crear una copia.

def _ingresar_entero(mensaje: str, minimo: int | None = None) -> int:
    """
    contrato:
        solicita al usuario un numero entero hasta que se ingrese uno valido.

    Precondiciones:
        minimo es un numero entero o None si se acepta cualquier entero
    
    Postcondiciones:
        Devuelve el numero entero ingresado, mayor o igual al minimo cuando se indico uno.
    """

    while True:
        try:
            numero = int(input(mensaje))
        except ValueError:
            print("Error: se debe ingresar un entero.")
        else:
            if minimo is None or numero >= minimo:
                return numero
            print(f"Error: el valor debe ser mayor o igual a {minimo}.")


def _ingresar_lista(nombre: str, cantidad: int) -> list[int]:
    """
    Contrato:
        Arma una lista con la cantidad de numeros enteros que el usuario ingresa por teclado.

    Precondiciones:
        Cantidad es un entero mayor o igual a cero
    
    Postcondiciones:
        Devuelve una lista nueva de logitud cantidad, con los valores en el orden en que se ingresan
    """ 

    lista = []
    for posicion in range(cantidad):
        lista.append(_ingresar_entero(f"{nombre} - valor {posicion + 1}: "))
    return lista


def _eliminar_valores(lista: list[int], a_eliminar: list[int]) -> int:
    """
    Contrato:
        Elimina de la lista recibida todos los elementos que aparecen en la lista a_eliminar, modificando la lista original en lugar de devolver una copia

    Precondiciones:
        Las dos listas contienen numeros enteros. cualquiera de las dos puede estar vacia.
    
    Postcondiciones:
        La lista original queda sin valores indicaos, conservando el orden de los que sobreviven devuelve la cantidad de elementos que se eliminaron

    """

    eliminados = 0

    for posicion in range(len(lista) - 1, -1, -1):
        if lista[posicion] in a_eliminar:
            lista.pop(posicion)
            eliminados += 1
    return eliminados


def main() -> None:
    """
    Contrato:
        Ejercuta el programa principal pide las dos listas muestra la lista original elimina los valores indicados y muestra la lista resultante
    
    Precondiciones:
        El archivo se tiene que ejecutar como principal
    
    Postcondiciones:
        Se muestra por pantalla la lista original, la lista de valores a eliminar y la resultante
    """

    cantidad_original = _ingresar_entero("Ingrese la cantidad de numeros de la lista original: ", 1)
    numeros = _ingresar_lista("Lista original", cantidad_original)

    cantidad_a_eliminar = _ingresar_entero("Ingresar la cantidad de valores a eliminar: ", 0)
    a_eliminar = _ingresar_lista("Valores a eliminar", cantidad_a_eliminar)

    print(f"Lista original: {numeros}")
    print(f"Valores a eliminar: {a_eliminar}")

    eliminados = _eliminar_valores(numeros, a_eliminar)

    print(f"Se eliminaron {eliminados} elementos.")
    print(f"Lista resultante: {numeros}")

if __name__ == "__main__":
    main()