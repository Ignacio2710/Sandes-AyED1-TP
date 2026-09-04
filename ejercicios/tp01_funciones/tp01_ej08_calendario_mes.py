#TP01 - Ejercicio 08
# El programa tiene que imprimir por pantalla el calendario de un mes completo d ecualquier mes y año.
treintayuno = (1, 3, 5, 7, 8, 10, 12)
treinta = (4, 6, 9, 11)
MESES = ('Enero', 'Febrero','Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

def diadelasemana(dia: int, mes: int, año: int) -> int:
    """
    Contrato: 
        Funcion de la consigna va  arecibir una fecha en tres enteros y devolver que dia de la semana cae

    Precondiciones:
        El dia, mes y año tienen que ser una fecha que exista

    Postcondiciones:
        Devuelve un entero entre 0 y 6
    """

    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = año // 100
    año2 = año % 100
    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem


def _es_bisiesto(año: int) -> bool:
    """
    Contrato:
        Recibe año y dice si es bisiesto
    
    Precondiciones:
        El año tiene que ser entero entre 1 y 9999.

    Postcondiciones:
        Devuelve True si es bisiesta y False si no lo es
    """
    assert 1 <= año <= 9999

    if año % 400 == 0:
        return True

    if año % 100 == 0:
        return False

    if año % 4 == 0:
        return True

    return False

def _dias_del_mes(mes: int, año: int) -> int:
    """
    Contrato:
        Recibe un mes y año, dice cuantos dias tiene ese mes

    Precondiciones:
        El mes tiene que ser un entero entre 1 y 12 y el año entre 1 y 9999
    
    Postcondiciones:
        Devuelve 28, 29, 30 o 31

    """

    assert 1 <= mes <= 12
    assert 1 <= año <= 9999

    if mes in treintayuno:
        return 31

    if mes in treinta:
        return 30

    if _es_bisiesto(año):
        return 29

    return 28

def _imprimir_mes(inicio_dia: int, dias: int, mes: int, año: int) -> None:
    """
    Contrato:
        Imprime el calendario completo del mes en fila los 7 dias, con la semana empezando en domingo.

    Precondiciones:
        inicio_dia tiene que estar entre 0 y 6, dias entre 28 y 31, el mes 1 y 12 año entre 1 y 9999.

    Poscondiciones:
        Muestra por pantalla el calendario del mes no devuelve nada.    
    """

    print(f"-- {MESES[mes - 1]} de {año} --")
    print("DOM LUN MAR MIE JUE VIE SAB")

    columna = 0

    while columna < inicio_dia:
        print(f"{" ":>2}", end = " ")
        columna = columna + 1

    dia = 1

    while dia <= dias:
        print(f"{dia:>2}", end = " ")
        columna = columna + 1

        if columna % 7 == 0:
            print()
            columna = 0

        dia = dia + 1

    if columna != 0:
        print()

    return None 

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

def _pedir_mes() -> int:
    """
    Contrato:
        Pide el numero de mes hasta que el usuario ingresa uno valido
    
    Precondiciones:
        No recibe nada los datos los pide al usuario

    Postcondiciones:
        devuelve entero entre 1 y 12
    """
    while True:
        mes = _pedir_entero("Ingrese el numero de mes (1 a 12): ")

        if 1 <= mes <= 12:
            return mes

        print("Error: el mes tiene que ser entre 1 y 12")

def _pedir_año() -> int:
    """
    Contrato:
        Pide el año hasta que el usuario ingrese uno

    Precondiciones:
        No recibe nada, los datos los pide al usuario
    
    Postcondiciones:
        Devuelve un entero entre 1 y 9999

    """
    while True:
        año = _pedir_entero("Ingresa el año (entre 1 y 9999): ")

        if 1  <= año <= 9999:
            return año

        print("Error: El año tiene que ser entre 1 y 9999")

def main() -> None:
    """
    Contrato:
        Ejercuta el programa principal pide mes año y muestra el calendario de ese mes

    Precondiciones:
        El archivo se tiene que ejecutar como principal
    
    Postcondiciones:
        Se muestra por pantalla el calendario del mes pedido. no devuelve nada.
    """

    mes = _pedir_mes()
    año = _pedir_año()

    dia_inicial = diadelasemana(1, mes, año)
    dias = _dias_del_mes(mes, año)

    _imprimir_mes(dia_inicial, dias, mes, año)

    return None

if __name__ == '__main__':
    main()
