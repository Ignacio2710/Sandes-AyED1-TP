# TP01 - Ejercicio 03
# Este programa calcula el gasto mensaul en subte segun la cantidad de viajes.

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

            print("Error: la cantidad de viajes no puede ser negativo")

        except ValueError:
            print("Error: se tiene que ingresar un numero entero.")
    

def _gasto_mes_subte(viajes: int) -> float:

    """
    Contrato: 
        Esta funcion va a recibir la cantidad de viajes que se tomaron en un mes y calcula el total que se gasto en viajes de subte

    Precondiciones: 
        La cantidad de viajes deben ser numeros enteros.
    
    Postcondiciones: 
        La funcion debe devolver el total gastado en viajes aplicando el descuento que corresponda segun la cantidad de viajes que se hayan tomado.
    """
    # La tarifa maxima del subte en buenos aires:
    max_tarifa = 1684

    if viajes >= 1:
        if viajes <= 20:
            total = viajes * max_tarifa

        elif viajes <= 30:
            total = viajes * max_tarifa * 0.80

        elif viajes <= 40:
            total = viajes * max_tarifa * 0.70

        else:
            total = viajes * max_tarifa * 0.60

        return total
    
    else:
        return 0
        
def main() -> None:

    """
    Contrato: 
        Pide la cantidad de viajes que se tomaron en un mes y muestra su gasto total.
    
    Precondiciones: 
        Se tiene que ejecutar como programa principal.
    
    Postcondiciones: 
        muestra por pantalla el gasto total por viajes de subte.
    """

    viajes = _ingresar_entero_no_negativo("Los viajes que realize este mes son: ")

    gasto_por_viaje = _gasto_mes_subte(viajes)

    print(f"El gasto total en viajes es: ${gasto_por_viaje:.2f}")

if __name__ == "__main__":
    main()




