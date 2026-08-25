# TP01 - Ejercicio 05
# El programa determinara con funciones lambda si un numero es oblongo o triangular.

from typing import Callable

def _ingresar_entero(mensaje: str) -> int:
    """
    Contrato:
        Pide al usuario un numero entero hasta que sea valido.
    
    Precondiciones:
        El mensaje tiene que ser cadena de texto.
    
    Postcondiciones:
        Devuelve el entero ingresado por el usuario.
    """
    while True:
        try:
            return int(input(mensaje))

        except ValueError:
            print("Error: se tiene que ingresar un numero entero")


es_oblongo: Callable[[int], bool] = lambda numero: round((1 + 4 * numero) ** 0.5) ** 2 == 1 + 4 * numero if numero > 0 else False

"""
Contrato:
    Va a recibir un numero y determinar si es oblongo, osea si se puede obtener multiplicnado dos numeros naturales consecutivos.

Precondiciones:
    Numero debe ser un numero entero.

Postcondiciones:
    Devuelve True si el numero es oblongo y False en caso contrario.
"""

es_triangular: Callable[[int], bool] = lambda numero: round((1 + 8 * numero) ** 0.5) ** 2 == 1 + 8 * numero if numero > 0 else False

"""
Contrato:
    Recibe un numero y determina si es traigular, osea si se puede expresar con la suma de los numeros naturales consecutivos desde 1 hasta X numero.

Precondiciones:
    Numero debe ser un numero entero.

Postcondiciones:
    Devuelve True si el numero es Triangular y False en caso contrario.
"""

def main() -> None:
    """
    Contrato:
        Pide un numero al usuario y muestra si es oblongo y si es triangular.

    Precondiciones:
        Se tiene que ejercutar como programa principal.

    Postcondiciones:
        Muestra por pantalla si el numero ingresado es oblogno y si es triangular.
    """
    numero = _ingresar_entero("Ingresa el numero a evaluar: ")

    print(f"El numero {numero} es oblongo: {es_oblongo(numero)}")
    print(f"El numero {numero} es triangular: {es_triangular(numero)}")

if __name__ == "__main__":
    main()