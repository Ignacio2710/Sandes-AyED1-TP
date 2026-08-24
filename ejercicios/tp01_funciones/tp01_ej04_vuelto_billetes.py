# TP01 - Ejercicio 04
# Calcula el vuelto de una compra usando la menor cantidad de billetes.

def _ingresar_entero_no_negativo(mensaje: str) -> int:
    
    """
    Contrato:
        Pide al usuario un numero entero mayor o igual a cero hasta que se ingrese uno valido.
    
    Precondiciones:
        El mensaje debe ser una cadena de texto.

    Postcondiciones:
        Devuelve un entero no negativo ingresado por el usuario.
    """
    while True:
        try:
            numero = int(input(mensaje))

            if numero >= 0:
                return numero

            print("Error: el monto no puede ser negativo")

        except ValueError:
            print("Error: se tiene que ingresar un numero entero.")


def _billetes(dinero: int, compra: int) -> None:

    """
    Contrato: 
        Esta funcion recibira el total de una compra y el dinero que se recibe del cliente, y va a calcular el vuelto usando el menor numero de billetes posibles
    
    Precondiciones: 
        La compra y el dinero que se reciben tienen que ser numeros enteros y positivos. El valor de billetes son: $5000, $1000, $500, $200, $100, $50, $10.
    
    Postcondiciones: 
        La funcion va a mostrar por pantalla el total del vuelto y la cantidad de billetes de cada valor que son entregados. Si el dinero es insuficiente
        muestra mensaje de error, si el cambio no puede entregarse con los valores de dinero disponibles muestra mensaje de error y el sobrante.
    """

    billete_5000 = 5000
    billete_1000 = 1000
    billete_500 = 500
    billete_200 = 200
    billete_100 = 100
    billete_50 = 50
    billete_10 = 10

    if dinero < compra:
        return print(f"Falta dinero para realizar tu compra: ${compra - dinero}.")
    
    else:
        vuelto = dinero - compra

        total_vuelto = vuelto

        vuelto_5000 = vuelto // billete_5000 
        vuelto = vuelto % billete_5000

        vuelto_1000 = vuelto // billete_1000
        vuelto = vuelto % billete_1000

        vuelto_500 = vuelto // billete_500
        vuelto = vuelto % billete_500

        vuelto_200 = vuelto // billete_200
        vuelto = vuelto % billete_200

        vuelto_100 = vuelto // billete_100
        vuelto = vuelto % billete_100

        vuelto_50 = vuelto // billete_50
        vuelto = vuelto % billete_50

        vuelto_10 = vuelto // billete_10
        vuelto = vuelto % billete_10

    if vuelto != 0:
        return print(f"No se puede entregar el cambio exacto sobran: ${vuelto}.")

    else:
        print(f"El total de vuelto es: ${total_vuelto}")
        print(f"Billetes de $5000: {vuelto_5000}")
        print(f"Billetes de $1000: {vuelto_1000}")
        print(f"Billetes de $500: {vuelto_500}")
        print(f"Billetes de $200: {vuelto_200}")
        print(f"Billetes de $100: {vuelto_100}")
        print(f"Billetes de $50: {vuelto_50}")
        print(f"Billetes de $10: {vuelto_10}")


def main() -> None:

    """
    Contrato: 
        Esta funcion solicita al usuario el total de la compra y dinero con el que paga para calcular el vuelto.
    
    Precondiciones: 
        Se debe ejecutar el programa como programa principal.
    
    Postcondiciones: 
        Se muestra por pantalla el total del vuelto y la cantidad de billetes de cada valor que se entregan, 
        o un mensaje de error si no es posible entregar dicho cambio.
    """
    compra = _ingresar_entero_no_negativo("El dinero de la compra es: ")
    dinero = _ingresar_entero_no_negativo("Ingresa el dinero con el que se pagara: ")

    _billetes(dinero, compra)

if __name__ == "__main__":
    main()