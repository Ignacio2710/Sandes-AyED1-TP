def _gasto_mes_subte(viajes):

    """
    Contrato: Esta funcion va a recibir la cantidad de viajes que se tomaron en un mes y calcula el total que se gasto en viajes de subte
    Precondiciones: La cantidad de viajes deben ser numeros enteros y positivos.
    Postcondiciones: La funcion debe devolver el total gastado en viajes aplicando el descuento que corresponda segun la cantidad de viajes que se hayan tomado.
    """

    max_tarifa = 1684

    if viajes >= 1:
        if viajes <= 20:
            totaltarifa = viajes * max_tarifa

        elif viajes <= 30:
            totaltarifa = viajes * max_tarifa * 0.80

        elif viajes <= 40:
            totaltarifa = viajes * max_tarifa * 0.70

        else:
            totaltarifa = viajes * max_tarifa * 0.60

        return totaltarifa
    
    else:
        return 0
        
def main() -> None:

    """
    Contrato: Pide la cantidad de viajes que se tomaron en un mes y muestra su gasto total.
    Precondiciones: Se tiene que ejecutar como programa principal.
    Postcondiciones: muestra por pantalla el gasto total por viajes de subte.
    """
    viajes = int(input("Los viajes que realize este mes son: "))

    gasto_por_viaje = _gasto_mes_subte(viajes)

    print(f"El gasto total en viajes es: ${gasto_por_viaje}")

if __name__ == "__main__":
    main()




