# TP02 - Ejercicio 12
# Registra los ingresos diarios de los socios de un club y permite dar de baja a uno

SOCIO_MIN = 10000
SOCIO_MAX = 99999
FIN = 0


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


def _ingresar_socio(mensaje: str, acepta_fin: bool) -> int:
    """
    Contrato:
        Solicita un numero de socio de 5 digitos y opcionalmente acepta FIN para terminar.

    Precondiciones:
        acepta_fin indica si en esta pregunta el valor FIN es una respuesta valida

    Postcondiciones:
        Devuelve un entero entre SOCIO_MIN y SOCIO_MAX o FIN cuando acepta_fin es True y el usuario lo ingreso
    """

    while True:
        numero = _ingresar_entero(mensaje)
        if acepta_fin and numero == FIN:
            return FIN
        if SOCIO_MIN <= numero <= SOCIO_MAX:
            return numero
        print(f"Error: el socio debe tener 5 digitos entre {SOCIO_MIN} y {SOCIO_MAX}")

def _cargar_ingresos() -> list[int]:
    """
    Contrato:
        Registra los numeros de socio que van entrando al club hasta que se ingres FIN

    Precondiciones:
        Ninguna

    Postcondiciones:
        Devuelve una lista nueva con los socios en el orden en que ingresaron puede quedar vacia si no entro nadie
    """

    ingresos = []
    socio = _ingresar_socio(f"Numero de socio ({FIN} para terminar): ", True)
    while socio != FIN:
        ingresos.append(socio)
        socio = _ingresar_socio(f"Numero de socio ({FIN} para terminar): ", True)
    return ingresos

def _socios_distintos(ingresos: list[int]) -> list[int]:
    """
    Contrato:
        Arma una lista con los socios que ingresaron, sin repetir

    Precondiciones:
        La lista contiene numeros de socio y puede estar vacia

    Postcondiciones:
        Devuelve una lista nueva donde cada socio aparece una sola vez, en el orden en que ingreso por primera vez. no modifica la lista recibida
    """

    distintos = []
    for socio in ingresos:
        if socio not in distintos:
            distintos.append(socio)
    return distintos


def _contar_apariciones(ingresos: list[int], socio: int) -> int:
    """
    Contrato:
        Cuenta cuantas veces ingreso al club un socio

    Precondiciones:
        La lista contiene numeros de socio y puede estar vacia

    Postcondiciones:
        Devuelve la cantidad de veces que aparece el socio no modifica la lista
    """

    veces = 0
    for numero in ingresos:
        if numero == socio:
            veces += 1
    return veces

def _en_veces(cantidad: int) -> str:
    """
    Contrato:
        Arma el texto que acompaña a una cantidad de ingresos, en singular o plural

    Precondiciones:
        Cantidad es un entero mayor o igual a cero

    Postcondiciones:
        Devuelve "1 vez" cuando la cantidad es uno y "N veces" en cualquier otro caso
    """

    if cantidad == 1:
        return "1 vez"
    return f"{cantidad} veces"

def _informar_ingresos(ingresos: list[int]) -> None:
    """
    Contrato:
        Informa cuantas veces ingreso cada socio mostrando a cada uno una sola vez

    Precondiciones:
        La lista contiene numeros de socio y puede estar vacia

    Postcondiciones:
        Imprime un renglon por socio distinto. no devuelve nada ni modifica la lista
    """

    distintos = _socios_distintos(ingresos)
    if len(distintos) == 0:
        print("No ingreso ninguno socio")
    else:
        for socio in distintos:
            print(f"El socio {socio} ingreso {_en_veces(_contar_apariciones(ingresos, socio))}")

def _eliminar_socio(ingresos: list[int], socio: int) -> int:
    """
    Contrato:
        Elimina de la lista todos los ingresos de un socio, modifica la lista original

    Precondiciones:
        La lista contiene numeros de socio y puede estar vacia

    Postcondiciones:
        La lista queda sin ningun ingreso de ese socio, conserva el orden de los demas, devuelve la cantidad de ingresos eliminados
    """

    eliminados = 0

    for posicion in range(len(ingresos) -1, -1, -1):
        if ingresos[posicion] == socio:
            ingresos.pop(posicion)
            eliminados += 1
    return eliminados

def _dar_de_baja(ingresos: list[int]) -> None:
    """
    Contrato:
        Pide el numero de un socio dado de baja elimina todos sus ingresos y muestra los registros antes y despues

    Precondiciones:
        La lista contiene los ingresos registrados

    Postcondiciones:
        La lista queda sin los ingresos de ese socio imprime los dos registros y cuantos ingresos se eliminaron, no devuelve nada
    """

    socio = _ingresar_socio("Numero de socio dado de baja: ", False)

    print(f"Registros antes de la baja: {ingresos}")
    eliminados = _eliminar_socio(ingresos, socio)
    print(f"Registros despues de la baja: {ingresos}")

    if eliminados == 0:
        print(f"El socio {socio} no tenia ingreos registrados")
    elif eliminados == 1:
        print(f"Se elimino 1 ingreso del socio {socio}")
    else:
        print(f"Se eliminaron {eliminados} ingresos del socio {socio}")

def main() -> None:
    """
    Contrato:
        Ejercuta el programa principal carga los ingresos del dia, informa cuantas veces ingreso cada socio y da de baja a un socio.
    
    Precondiciones:
        El archivo se tiene que ejecutar como principal
    
    Postcondiciones:
        Se muestra por pantalla el informe de ingresos y el resultado de la baja
    """
    print("Registro de ingresos al club")
    ingresos = _cargar_ingresos()

    print()
    print("Ingresos por socio:")
    _informar_ingresos(ingresos)

    print()
    print("Baja de un socio")
    _dar_de_baja(ingresos)

if __name__ == "__main__":
    main()