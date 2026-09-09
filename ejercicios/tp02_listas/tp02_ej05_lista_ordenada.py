# TP05 - Ejercicio 05
# Verifica si una lista esta ordenada en forma ascendente.



def _ingresar_entero(mensaje: str)-> int:
    """
    contrato:
        solicita al usuario un numero entero hasta que se ingrese uno valido.

    Precondiciones:
        no hay Se acepta cualquier entero, positivo negativo o cero
    
    Postcondiciones:
        Devuelve el numero entero ingresado.
    """

    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: se debe ingresar un entero")


def _ingresar_cantidad(mensaje: str, minimo: int) -> int:
    """
    Contrato:
        solicita al usuario una cantidad entera mayor o igual al minimo hasta que se ingrese una valida.

    Precondiciones:
        Minimo es un entero

    Postcondiciones:
        Devuelve el numero entero ingresado, siempre mayor o igual al minimo que se recibe   
    """

    while True:
        numero = _ingresar_entero(mensaje)
        if numero >= minimo:
            return numero
        print(f"Error: el valor debe ser mayor o igual a {minimo}. ")

def _ingresar_lista(cantidad: int) -> list[int]:
    """
    Contrato:
        Arma una lista con cantidad de numeros enteros que el usuario ingresa
    
    Precondiciones:
        Cantidad es un entero mayor o igual a cero
    
    Postcondiciones:
        Devuelve una lista nueva de longitud cantidad, con los valores en el orden en que se ingresaron
    """
    lista = []
    for posicion in range(cantidad):
        lista.append(_ingresar_entero(f"Valor {posicion + 1}: "))
    return lista

def _esta_ordenada(lista: int) -> bool:
    """
    Contrato:
        Determina si los elementos de la lista estan ordenados en forma ascendente.

    Precondiciones:
        Los elementos de la lista tienen que ser comparables entre si, todos numeros o todos cadenas. la lista puede estar vacia

    Postcondiciones:
        Devuelve True si cada elemento es menor o igual al siguiente y False en caso contrario, las listas vacias y las de un solo elemento 
        se consideran ordenadas, no modifica la lista
    """
    for posicion in range(len(lista) - 1):
        if lista[posicion] > lista[posicion + 1]:
            return False
    return True

def _mostrar_resultado(lista: list) -> None:
    """
    Contrato:
        Muestra por pantalla la lista recibida junto con el resultado de _esta_ordenada.

    Precondiciones:
        Los elementos de la lista tienen que ser comparables entre si

    Postcondiciones:
        Imprime un renglon con la lista y su resultado. no devuelve nada ni modifica la lista.
    """
    resultado = _esta_ordenada(lista)
    print(f"ordenada({lista}) devuelve {resultado}")


def main() -> None:
    """
    Contrato:
        Ejercuta el programa principal prueba la funcion con ejemplo de la consigna y despues con una lista del usuario
    
    Precondiciones:
        El archivo se tiene que ejecutar como principal 
    
    Postcondiciones:
        Muestra por pantalla, el resultado de los ejemplos y el de la lista ingresada
    """
    print("Ejemplos de la consigna: ")
    _mostrar_resultado([1, 2, 3])
    _mostrar_resultado(["b", "a"])

    print()
    cantidad = _ingresar_entero("Ingrese la cantidad de numeros de su lista: ", 0)
    numeros = _ingresar_lista(cantidad)

    print(f"Lista ingresada: {numeros}")
    if _esta_ordenada(numeros):
        print("La lista esta ordenada en forma ascendente")
    else:
        print("La lista no esta ordenada de forma ascendente")

if __name__ == "__main__":
    main()