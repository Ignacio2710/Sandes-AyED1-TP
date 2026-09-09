# TP02 - Ejercicio 09
# Genera por comprension los multiplos de 7 que no son multiplos de 5 entre A y B


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

def _ingresar_entero_minimo(mensaje: str, minimo: int) -> int:
    """
    Contrato:
        Solicita al usuario un numero entero mayor o igual al minimo hasta que se ingresa uno valido

    Precondiciones:
        el minimo es un numero entero
    
    Postcondiciones:
        Devuelve el numero entero ingresado, siempre mayor o igual al minimo recibido
    """
    while True:
        numero = _ingresar_entero(mensaje)
        if numero >= minimo:
            return numero
        print(f"Error: el valor debe ser mayor o igual a {minimo}")


def _multiplos_de7_no_de5(desde: int, hasta: int) -> list[int]:
    """
    Contrato:
        Contruye por comprension la lista de los multiplos de 7 que no son multiplos de 5, comprendidos entre desde y hasta los dos incluidos

    Precondiciones:
        Desde y hasta son nnumeros enteros y hasta es mayor o igual que desde
    
    Postcondiciones:
        Devuelve una lista nueva en orden ascendente puede quedar vacia si en ese rango no hay ningun numero que cumpla las dos condiciones.
    """

    return [numero for numero in range(desde, hasta + 1) if numero % 7 == 0 and numero % 5 != 0]


def main() -> None:
    """
    Contrato:
        Ejercuta el programa principal pide A y B imprime los multiplos de 7 que no son de 5
    
    Precondiciones:
        El archivo se tiene que ejecutar como principal
    
    Postcondiciones:
        Se muestra por pantalla el rango pedido y la lista resultante
    """
    a = _ingresar_entero("Ingrese el valor de A:")
    b = _ingresar_entero_minimo("Ingrese el valor de B:", a)

    multiplos = _multiplos_de7_no_de5(a, b)

    print(f"Multiplos de 7 que no son de 5 entre {a} y {b}:")
    print(multiplos)
    print(f"Se encontraron {len(multiplos)} numeros")

if __name__ == "__main__":
    main()