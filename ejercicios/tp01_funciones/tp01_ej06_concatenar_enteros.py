# TP01 - Ejercicio 06
# El programa va a concatenar dos numeros enteros y pisitivos usando operaciones aritmeticas

def _ingresar_entero_positivo(mensaje: str) -> int:
    """
    Contrato:
        Pide al usuario un entero positivo.

    Precondiciones:
        El mensaje tiene que ser cadena de texto.

    Postcondiciones:
        Devuelve un entero positivo mayor a cero que fue ingresado.
    """
    while True:
        try:
            numero = int(input(mensaje))

            if numero > 0:
                return numero

            print("Error: El numero tiene que ser positivo.")

        except ValueError:
            print("Error: se tiene que ingresar un numero entero.")

def _concatenar(primero: int, segundo: int) -> int:
    """
    Contrato:
        La funcion recibe 2 numeros enteros y positivos, devolviendo un numero como resultado luego de concatenarlos, sin convertilo en texto.
    
    Precondiciones:
        Primero y segundo tienen que ser numeros enteros y mayores que 0.
    
    Postcondiciones:
        Devuelve el numero formado por los digitos del priemro seguidos por los digitos del segundo.

    """
    multiplicador = 1
    resto = segundo

    while resto > 0:
        multiplicador = multiplicador * 10
        resto = resto // 10

    return primero * multiplicador + segundo

def main() -> None:
    """
    Contrato:
        Pide dos numero enteros y positivos y muestra el resultado de concatenarlos.

    Precondiciones:
        Se tiene que ejercutar como programa principal.

    Postcondiciones:
        Muestra por pantalla el resultado de concatenar los dos ingresados.
    """
    primero = _ingresar_entero_positivo("Ingresa el primer numero: ")
    segundo = _ingresar_entero_positivo("Ingresa el segundo numero: ")

    print(f"La concatenacion de {primero} y {segundo} es: {_concatenar(primero, segundo)}")

if __name__ == "__main__":
    main()
