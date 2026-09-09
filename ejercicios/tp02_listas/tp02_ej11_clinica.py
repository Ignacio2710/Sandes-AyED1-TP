# TP02 - Ejercicio 11
# registra la atencion de pacientes de una clinica por urgencia o por turno

AFILIADO_MIN = 1000
AFILIADO_MAX = 9999
FIN = -1
URGENCIA = 0
TURNO = 1

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

def _ingresar_afiliado(mensaje: str) -> int:
    """
    Contrato:
        Solicita un numero de afiliado de 4 digitos, o FIN para terminar

    Precondiciones:
        Ninguna

    Postcondiciones:
        Devuelve un entero entre AFILIADO_MIN y AFILIADO_MAX o FIN si el usuario quiere terminar
    """
    while True:
        numero = _ingresar_entero(mensaje)
        if numero == FIN or AFILIADO_MIN <= numero <= AFILIADO_MAX:
            return numero
        print(f"Error: el afiliado debe tener 4 digitos, entre {AFILIADO_MIN} y {AFILIADO_MAX}")

def _ingresar_tipo_atencion() -> int:
    """
    Contrato:
        Solicita el tipo de atencion al paciente: URGENCIA o TURNO

    Precondiciones:
        ninguna
    
    Postcondiciones:
        Devuelve URGENCIA o TURNO nunca otro valor
    """
    while True:
        tipo = _ingresar_entero(f"Tipo de atencion ({URGENCIA} = urgencia, {TURNO} = turno): ")
        if tipo == URGENCIA or tipo == TURNO:
            return tipo
        print(f"Error: solo se acepta {URGENCIA} para urgencia o {TURNO} para turno")


def _cargar_pacientes(urgencias: list[int], turnos: list[int]) -> None:
    """
    Contrato:
        Registra una recepcion a los pacientes que se anuncian agregando cada afiliado a la lista de urgencias o a la de turnos segun haya sido atendido

    Precondiciones:
        Las dos listas existen y estan vacias o con atenciones anteriores

    Postcondiciones:
        Las dos listas quedan con los afiliados agregados en el orden en que llegaron la carga termina cuando
        se ingresa FIN como numero de afiliado, no devuelve nada
    """

    afiliado = _ingresar_afiliado(f"Numero de afiliado ({FIN} para terminar): ")
    while afiliado != FIN:
        if _ingresar_tipo_atencion() == URGENCIA:
            urgencias.append(afiliado)
        else:
            turnos.append(afiliado)
        afiliado = _ingresar_afiliado(f"Numero de afiliado ({FIN} para terminar): ")


def _mostrar_listado(titulo: str, lista: list[int]) -> None:
    """
    Contrato:
        Muestra por pantalla el listado de afiliados de una lista, precedido por su titulo

    Precondiciones:
        La lista contiene numeros de afiliado y puede estar vacia
    
    Postcondiciones:
        Imprime el titulo y los afiliados en el orden en que llegaron, o un aviso si no hubo ninguno no devuelve nada
        ni modifica la lista
    """

    print(titulo)
    if len(lista) == 0:
        print("No se atendio a ningun paciente")
    else:
        for afiliado in lista:
            print(f"{afiliado}")


def _contar_apariciones(lista: list[int], afiliado: int) -> int:
    """
    Contrato:
        Cuenta cuantas veces aparece un numero de afiliado en la lista recibida

    Precondiciones:
        La lista contiene numeros de afiliado y puede estar vacia
    
    Postcondiciones:
        Devuelve la cantidad de veces que aparece el afiliado. no modifica la lista
    """

    veces = 0
    for numero in lista:
        if numero == afiliado:
            veces += 1
    return veces

def _en_veces(cantidad: int) -> str:
    """
    Contrato:
        Arma el texto que acompaña a una cantidad de atenciones, en singular o plural

    Precondiciones:
        Cantidad es un entero mayor o igual a cero

    Postcondiciones:
        Devuelve "1 vez" cuando la cantidad es uno y "N veces" en cualquier otro caso
    """
    if cantidad == 1:
        return "1 vez"
    return f"{cantidad} veces"

def _buscar_afiliados(urgencias: list[int], turnos: list[int]) -> None:
    """
    Contrato:
        Busca numeros de afiliado e informa cuantas veces fue atendido por urgencia y cuantas por turno, hasta que se ingrese un FIN

    Precondiciones:
        Las dos listas contienen los afiliados atendidos.

    Postcondiciones:
        Muestra por pantalla el resultado de cada busqueda. no devuelve nada ni modifica las listas
    """

    afiliado = _ingresar_afiliado(f"Afiliado a buscar ({FIN} para terminar): ")
    while afiliado != FIN:
        por_urgencia = _contar_apariciones(urgencias, afiliado)
        por_turno = _contar_apariciones(turnos, afiliado)

        if por_urgencia == 0 and por_turno == 0:
            print(f"El afiliado {afiliado} no fue atendido")
        else:
            print(f"El afiliado {afiliado} fue atendido {_en_veces(por_urgencia)} por urgencia" 
                  f"y {_en_veces(por_turno)} por turno.")

        afiliado = _ingresar_afiliado(f"Afiliado a buscar ({FIN} para terminar): ")


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal registra a los pacientes, muestra los dos listados y despues permite buscar afiliados
    
    Precondiciones:
        El archivo se tiene que ejecutar como principal
    
    Postcondiciones:
        Se muestra por pantalla los listados de urgencias y turnos ademas el resultado de cada busqueda
    """

    urgencias = []
    turnos = []

    print("Recepcion de pacientes")
    _cargar_pacientes(urgencias, turnos)

    print()
    _mostrar_listado("Pacientes atendidos por urgencia:", urgencias)
    _mostrar_listado("Pacientes atendidos por turno:", turnos)

    print()
    print("Busqueda de afiliados")
    _buscar_afiliados(urgencias, turnos)

    print("Programa terminado")

if __name__ == "__main__":
    main()