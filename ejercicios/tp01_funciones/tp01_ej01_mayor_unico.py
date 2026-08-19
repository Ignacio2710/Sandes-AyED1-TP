# TP01 - Ejercicio 01
# Devuelve el mayor de tres numeros enteros y positivos solo si es unico.

def _ingresar_enteropositivo(mensaje: str) -> int:
    """
    Contrato:
        Pide al usuario un entero positivo.

    Precondiciones:
        El mensaje tiene que ser cadena de texto.

    Postcondiciones:
        Devuelve un entero positivo mayor a cero que fue ingresado.
    """
    numero = 0

    while numero <= 0:
        try:
            numero = int(input(mensaje))

            if numero <= 0:
                print("Error: el numero tiene que ser positivo.")

        except ValueError:
            print("Error: se tiene que ingresar un numero entero.")

    return numero


def _mayor_unico(num: int, num1: int, num2: int) -> int:
    """
    Contrato: 
        Esta funcion debe recibir tres numeros los cuales tienen que ser enteros y positivos, 
        Devolviendo el mayor de los tres solo si es unico.

    Precondiciones: 
        Los tres numeros deben ser enteros y positivos.

    Postcondiciones:
        El mayor debe aparecer una sola vez y devolverlo.
        Si el mayor aparece mas de una vez devuelve -1.
    """
    if num > num1:
        if num > num2:
            numero_mayor = num
        elif num2 > num:
            numero_mayor = num2
        else:
            numero_mayor = -1
    else:
        if num1 > num:
            if num1 > num2:
                numero_mayor = num1
            elif num2 > num1:
                numero_mayor = num2
            else:
                numero_mayor = -1
        else:
            if num2 > num:
                numero_mayor = num2
            else:
                numero_mayor = -1

    return numero_mayor        

def main() -> None:
    """
    Contrato: 
        Pide tres numeros a el usuario y muestra el mayor unico

    Precondiciones: 
        Se tiene que ejecutar como programa principal

    Postcondiciones: 
        Muestra por pantalla el mayor unico, en caso de no haber muestra un mensaje informativo.
    """

    num = _ingresar_enteropositivo("Ingresa un numero entero que sea positivo: ")
    num1 = _ingresar_enteropositivo("Ingresa tu segundo numero entero y positivo: ")
    num2 = _ingresar_enteropositivo("Ingresa tu tercer numero entero y positivo: ")

    resultado = _mayor_unico(num, num1, num2)

    if resultado == -1:
        print("No existe mayor unico se encuentra repetido.")

    else:
        print(f"El mayor y unico es: {resultado}")

if __name__ == "__main__":
    main()