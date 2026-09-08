# TP02 - Ejercicio 01
# Carga una lista con numeros al azar y opera sobre ella: producto de sus elementos
# eliminacion de todas las aparciciones de un valor y verificacion de si su contenido es capicua.

import random

ELEMENTOS_MIN = 10
ELEMENTOS_MAX = 99
VALOR_MIN = 1000
VALOR_MAX = 9999


def _ingresar_entero(mensaje: str) -> int:
    """
    contrato:
        solicita al usuario un entero por teclado hasta que se ingrese uno

    Precondiciones:
        ninguna
    
    Postcondicioens:
        Devuelve el numero entero ingresado por el usuario
    """

    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: se debe ingresar un numero entero")

def _cargar_lista_azar() -> list[int]:
    """
    Contrato:
        genera una lista de numeros enteros al azar de cuatro digitos, la cantidad de elementos tambien es un numero al azar de dos digitos
    
    Precondiciones:
        ninguna

    Postcondiciones:
        devuelve una lista que su longitud esta entre elementos_min y elementos_max y cada elementos esta entre valor_min y valor_max

    """

    cantidad = random.randint(ELEMENTOS_MIN, ELEMENTOS_MAX)
    lista = []
    for _ in range(cantidad):
        lista.append(random.randint(VALOR_MIN, VALOR_MAX))
    return lista

def _producto_elementos(lista: list[int]) -> int:
    """
    Contrato:
        Calcula el producto de todos los elementos de la lista que se recibe.
    
    Precondiciones:
        la lista contiene unicamente numeros enteros.
    
    Postcondiciones:
        Devuelve el producto de los elementos. si la lista esta vacia devuelve 1, que es el elemento neutro de la multiplicacion. no modifica la lista
    """

    producto = 1
    for elemento in lista:
        producto = producto * elemento
    return producto

def _eliminar_apariciones(lista: list[int], valor: int) -> int:
    """
    Contrato:
        elimina de la lista todas las apariciones del valor recibido, sin utilizar listas auxiliares

    Precondiciones:
        la lista contieen solo numeros enteros
    
    postcondiciones:
        Modifica la lista original quitando los elementos iguales y conserva el orden de los restantes. devuelve la cantidad de elementos eliminados
    """

    eliminados = 0
    for i in range(len(lista) -1, -1, -1):
        if lista[i] == valor:
            lista.pop(i)
            eliminados = eliminados + 1
    return eliminados

def _es_capicua(lista: list[int]) -> bool:
    """
    Contrato:
        Determina si el contenido de una lista es capicua, osea si se lee iugal de izquierda a derecha que de derecha a izquierda. no usa listas auxiliares

    Precondiciones:
        ninguna la lista puede estar vacia

    Postcondiciones:
        Devuelve True si la lista es capicua y False en caso contrario no modifica la lista
    """

    izquierda = 0
    derecha = len(lista) - 1
    capicua = True
    while izquierda < derecha and capicua:
        if lista[izquierda] != lista[derecha]:
            capicua = False
        izquierda = izquierda + 1
        derecha = derecha - 1
    return capicua

def main() -> None:
    """
    Contrato:
        Ejercuta el programa principal invoca cada funcion e imprime la lista despues de cada invocacion

    Precondiciones:
        El archivo se tiene que ejecutar como principal
    
    Postcondiciones:
        Se muestra por pantalla los resultados del ejercicio.
    """
    numeros = _cargar_lista_azar()
    print(f"cantidad de elementos: {len(numeros)}")
    print(f"Lista: {numeros}")

    producto = _producto_elementos(numeros)
    print(f"Producto: {producto}")
    print(f"lista: {numeros}")

    valor = _ingresar_entero("Ingrese el valor para eliminar: ")
    eliminados = _eliminar_apariciones(numeros, valor)
    print(f"Se eliminaron {eliminados} apariciones del valor {valor}")
    print(f"Lista: {numeros}")

    if _es_capicua(numeros):
        print("La lista es capicua")
    else:
        print("La lista no es capicua")
    print(f"Lista: {numeros}")

if __name__ == "__main__":
    main()