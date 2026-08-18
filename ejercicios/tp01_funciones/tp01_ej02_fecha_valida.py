def _año_bisiesto (año):

    """
    Contrato: Esta funcion recibira un numeor entero positivo correspondiente a un año, verificando si el año es bisiesto.
    Precondiciones: El año tiene que ser un numero entero y positivo entre 1 y 9999.
    Postcondiciones: La funcion devuelve True si el año es bisiesto y False si no lo es.
    """

    if año % 400 == 0:
        return True

    elif año % 100 == 0:
        return False

    elif año % 4 == 0:
        return True

    else:
        return False

def _mes_delaño (mes):

    """
    Contrato: Esta funcion recibe un numero entero positivo de un mes y verifica si este mismo es valido.
    Precondiciones: El mes debe estar entre el 1 y el 12.
    Postcondiciones: La funcion devuelve True si el mes es valido y en caso de no serlo False.
    """

    if mes < 1:
        return False

    elif mes > 12:
        return False
    
    else:
        return True
    

def _dia_delaño (dia, mes, año):

    """
    Contrato: Esta funcion recibe tres numeros enteros y positivos correspondientes al mes, dia y año de una fecha verificando si el dia es valido para el mes.
    Precondiciones: El dia tiene que ser un numero entero positivo, el mes tiene que ser entre 1 y 12 y el año debe estar entre 1 y 9999.
    Postcondiciones: La funcion devuelve True si el dia es valido para el mes y año que recibe, y False en caso de no serlo.
    """

    if mes == 1:
        if dia >= 1:
            if dia <= 31:
                return True
    if mes == 2:
        if _año_bisiesto(año):
            if dia >=1:
                if dia <= 29:
                    return True
        else:
            if dia >= 1:
                if dia <= 28:
                    return True

    if mes == 3:
        if dia >= 1:
            if dia <= 31:
                return True
    if mes == 4:
        if dia >= 1:
            if dia <= 30:
                return True
    if mes == 5:
        if dia >= 1:
            if dia <= 31:
                return True
            
    if mes == 6:
        if dia >= 1:
            if dia <= 30:
                return True
    if mes == 7:
        if dia >= 1:
            if dia <= 31:
                return True
    if mes == 8:
        if dia >= 1:
            if dia <= 31:
                return True

    if mes == 9:
        if dia >= 1:
            if dia <= 30:
                return True

    if mes == 10:
        if dia >= 1:
            if dia <= 31:
                return True
    if mes == 11:
        if dia >= 1:
            if dia <= 30:
                return True

    if mes == 12:
        if dia >= 1:
            if dia <= 31:
                return True

    return False


"""< >"""


def _verificar_fecha(dia, mes, año):

    """
    Contrato: esta funcion va a recibir tres numeros enteros positivos de acuerdo al dia, mes, año de una fecha y 
    verificar si es una fecha valida.
    Precondiciones: se debe tener en cuenta que el dia, mes y año tienen que ser numeros enteros y positivos
    y contar conque el mes debe ser entre 1 y 12 (incluyendolos), y el año entre 1 y 9999.
    Postcondiciones: El programa devuelve True si la fecha es correcta y False si no lo es.
    """
    if año < 1:
        return False
    
    elif año > 9999:
        return False
    
    if _mes_delaño(mes):
        if _dia_delaño(dia, mes, año):
            return True
        
    return False

def main() -> None:

    """
    Contrato: Pide tres numeros siendo estos el dia, mes y año de una fecha.
    Precondiciones: Se tiene que ejecutar como programa pricipal.
    Postcondiciones: Muestra por pantalla si la fecha es valida con True en caso de no serlo muestra False.
    """

    dia = int(input("Ingresa el dia: "))
    mes = int(input("Ingresa el mes: "))
    año = int(input("Ingrsa el año: "))

    print(f"La fecha enviada para verificar es: {_verificar_fecha(dia, mes, año)}")

if __name__ == "__main__":
    main()