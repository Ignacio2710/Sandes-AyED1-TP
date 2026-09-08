#TP01 - Ejercicio 09
# El programa cuenta cajones de naranja por peso y calculo los camiones a despachar.

import random


naranjas_por_cajon = 100
peso_min = 200
peso_max = 300
capacidad_del_camion = 500000
carga_minima = 400000


def _pedir_entero(mensaje: str) -> int:
    """
    Contrato:
        Pide un entero hasta que el usuario ingrese uno
    
    Precondiciones:
        El mensaje tiene que ser cadena de texto

    Postcondiciones:
        Devuelve numero entero que ingreso el usuario
    """

    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: se tiene que ingresar un entero")

def _ingresar_entero_positivo(mensaje: str) -> int:
    """
    Contrato:
        Pide al usuario un entero positivo.

    Precondiciones:
        El mensaje tiene que ser cadena de texto.

    Postcondiciones:
        Devuelve un entero positivo mayor a cero.
    """
    while True:
            numero =_pedir_entero(mensaje)

            if numero > 0:
                return numero

            print("Error: El numero tiene que ser positivo.")



def _peso_de_naranja() -> int:
    """
    Contrato:
        Da el peso de una naranja.

    Precondiciones:
        no recibe nada.
    
    Postcondiciones:
        devuelve un entero al azar entre 150 y 350 gramos.
    """
    return random.randint(150, 350)
    

def _es_para_cajon(peso: int) -> bool:
    """
    Contrato:
        Dice si una naranja va al cajon o se descarta para hacer jugo.
    
    Precondiciones:
        El peso tiene que ser un entero en gramos.
    
    Postcondiciones:
        Devuelve True si el peso esta entre 200 y 300 gramos, False si no.
    """
    return peso_min <= peso <= peso_max


def _entraen_elcamion(peso_camion: int, peso_cajon: int) -> bool:
    """
    Contrato:
        Dice si un cajon mas entra en el camion que se esta cargando.
    
    Precondiciones:
        Los dos pesos tiene que ser enteros en gramos y no negativos.

    Postcondiciones:
        Devuelve True si cuando se suma el cajon no se pasa de la capacidad
    """
    return peso_camion + peso_cajon <= capacidad_del_camion


def _se_despachan_cajones(peso_camion: int) -> bool:
    """
    Contrato:
        Dice si un camion llego a la carga minima para salir a repartir
    
    Preocndiciones:
        El peso tiene que ser entero en gramos y no negativo

    Postcondiciones:
        Devuelve True si la carga llega al 80% de la capacidad
    """
    return peso_camion >= carga_minima


def _reparto(cosecha: int, camiones_disponibles: int) -> None:
    """
    Contrato:
        Simula la cosecha naranja por naranja, arma cajones los carga en los camiones y muestra el informe de reparto.

    Precondiciones:
        La cosecha y los camiones disponibles tienen que ser enteros mayores a cero
    
    Postcondiciones:
        Muestra por pantalla el resultado de reparto. no devuelve nada.
    """
    jugo = 0
    buenas = 0
    peso_cajon = 0
    peso_camion = 0
    camiones_despachados = 0

    for naranja in range(cosecha):
        peso = _peso_de_naranja()

        if not _es_para_cajon(peso):
            jugo = jugo + 1
        else:
            buenas = buenas + 1
            peso_cajon = peso_cajon + peso

            if buenas % naranjas_por_cajon == 0:

                if not _entraen_elcamion(peso_camion, peso_cajon):
                    if _se_despachan_cajones(peso_camion):
                        camiones_despachados = camiones_despachados + 1

                    peso_camion = 0

                peso_camion = peso_camion + peso_cajon
                peso_cajon = 0

    if peso_camion > 0 and _se_despachan_cajones(peso_camion):
        camiones_despachados = camiones_despachados + 1

    cajones = buenas // naranjas_por_cajon
    sobrante = buenas % naranjas_por_cajon


    _mostrar_informacion(cosecha, jugo, cajones, sobrante, camiones_despachados, camiones_disponibles)

    return None

def _mostrar_informacion(cosecha: int, jugo: int, cajones: int, sobrante: int, camiones_despachados: int, camiones_disponibles: int) -> None:

    """
    Contrato:
        Muestra por pantalla el informe final del reparto.
    
    Precondiciones:
        Todos los parametros tienen que ser enteros no negativos ya calculados.
    
    Postcondiciones:
        Imprimir el informe. No calcula ni devuelve nada.
    """
    print("---- Informe Del Reparto ----")
    print(f"Naranjas cosechadas: {cosecha}")
    print(f"Naranjas para jugo: {jugo}")
    print(f"Cajones Llenos: {cajones}")
    print(f"Naranjas sobrantes para el proximo reparto: {sobrante}")
    print(f"Camiones necesarios: {camiones_despachados}")

    if camiones_despachados > camiones_disponibles:
        print(f"No alcanzan los camiones: faltan {camiones_despachados - camiones_disponibles}.")
    else:
        print(f"Los {camiones_disponibles} camiones disponibles alcanzan. ")

    return None


def main() -> None:
    """
    Contrato:
        Ejercuta el programa principal pide la cosecha, camiones y muestra el informe del reparto

    Precondiciones:
        El archivo se tiene que ejecutar como principal
    
    Postcondiciones:
        Se muestra por pantalla el informe del reparto.
    """

    cosecha = _ingresar_entero_positivo("Ingresa la cantidad de naranjas que fueron cosechadas: ")
    camiones_disponibles = _ingresar_entero_positivo("Ingresa la cantidad de camiones disponibles: ")

    _reparto(cosecha, camiones_disponibles)

    return None

if __name__ == "__main__":
    main()
