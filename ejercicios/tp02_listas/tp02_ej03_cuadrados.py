# TP02 - Ejercicio 03
# Armar una lista con los cuadrados de los numeros entre 1 y N donde N se ingresa por usuario y muestra los ultimos valores de esa lista

ULTIMOS_A_MOSTRAR = 10

def _ingresar_entero(mensaje: str) -> int:
    """
    contrato:
        solicita al usuario un numero entero mayor a cero hasta que se ingrese uno valido

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

def _generar_cuadrados(n: int) -> list[int]:
    """
    Contrato:
        Genera una lista con los cuadrados de los numeros enteros 1 y el n recibido, los dos incluidos

    Precondiciones:
        n es un entero mayor a cero
    
    Postcondiciones:
        Devuelve una lista de logitud n, donde el elemento de la posicion i es el cuadrado de i + 1.
    """
    cuadrados = []
    for numero in range(1, n + 1):
        cuadrados.append(numero * numero)
    return cuadrados

def _ultimos_valores(lista: list[int], cantidad: int) -> list[int]:
    """
    Contrato:
        Arma una nueva lista con los ultimos elementos de la lista recibida.

    Precondiciones:
        cantidad es un entero mayor a cero.
    
    Postcondiciones:
        Devuelve una lista nueva con los ultimos elementos respetando el orden original. si la lista tiene menos elementos que la cantidad pedida,devuelve una copia de 
        la lista completa no modifica la lista recibida
    """
    inicio = len(lista) - cantidad
    if inicio < 0:
        inicio = 0
    return lista[inicio:]


def main() -> None:
    """
    Contrato:
        Ejercuta el programa principal pide N, arma la lista de cuadrados y muestra los ultimos valores.
    
    Precondiciones:
        El archivo se tiene que ejecutar como principal
    
    Postcondiciones:
        Se muestra por pantalla los resultados del ejercicio.
    """

    n = _ingresar_entero("Ingrese el valor de N: ")
    cuadrados = _generar_cuadrados(n)
    print(f"Se generaron {len(cuadrados)} cuadrados.")

    ultimos = _ultimos_valores(cuadrados, ULTIMOS_A_MOSTRAR)
    print(f"Ultimos {len(ultimos)} valores de la lista: ")
    for valor in ultimos:
        print(valor)

if __name__ == "__main__":
    main()