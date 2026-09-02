#TP01 - Ejercicio 07
# Calcular el dia siguiente a una fecha y usar esa funcion para dos programas: Sumarle N dias a una fecha y contar los dias que hay entre 2 fechas.

def _pedir_entero(mensaje: str) -> int:
    """
    Contrato:
        Pide un numero entero hasta que el usuario ingrese uno.
    
    Precondiciones:
        El mensaje tiene que ser cadena de texto.
    
    Postcondiciones:
        Devuelve el numero entero que ingreso el usuario
    """
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: se tiene que ingresar un numero entero.")

def _bisiesto(año: int) -> bool:
    """
    Contrato:
        Recibe un año y dice si es bisiesto.
    
    Precondiciones:
        El año tiene que ser un entero entre 1 y 9999.

    Postcondiciones:
        Devuelve True si el año es bisiesto y False si no lo es.
    """

    if año % 400 == 0:
        return True

    elif año % 100 == 0:
        return False

    elif año % 4 == 0:
        return True

    else:
        return False

def _dias_que_tiene(mes: int, año: int) -> int:
    """
    Contrato:
        Recibe un mes y año y dice cuantos dias tiene el mes
    
    Precondiciones:
        El mes tiene que ser un entero entre 1 y 12 y el año un entero entre 1 y 9999.

    Postcondiciones:
        Devuelve 28, 29, 30 o 31.
    """
    if mes == 2:
        if _bisiesto(año):
            return 29
        else:
            return 28
    if mes == 4:
        return 30

    if mes == 6:
        return 30

    if mes == 9:
        return 30

    if mes == 11:
        return 30

    return 31

def _fecha_existe(dia: int, mes: int, año: int) -> bool:
    """
    Contrato:
        Recibe el dia, mes y año de una fecha y verifica si esa fecha existe

    Precondiciones:
        El dia, mes y año tinen que ser numeros enteros.  <
    
    Postcondiciones:
        devuelve True si la fecha existe y false si no.
    """
    if año < 1:
        return False

    if año > 9999:
        return False
    if mes < 1:
        return False
    if mes > 12:
        return False

    if dia < 1:
        return False
    
    if dia > _dias_que_tiene(mes, año):
        return False
    
    return True

def diasiguiente_dia(dia: int, mes: int, año: int) -> int:
    """
    Contrato:
        Recibe una fecha y devuelve el dia del dia siguiente.
    
    Precondiciones:
        El dia, mes y año tienen que formar una fecha que exista.
    
    Postcondiciones:
        Devuelve el dia siguiente si el mes no termino, y 1 si el mes termino.
    """
    if dia < _dias_que_tiene(mes, año):
        return dia + 1
    return 1

def diasiguiente_mes(dia: int, mes: int, año: int) -> int:
    """
    Contrato:
        Recibe una fecha en tres enteros y devuellve el mes dle dia siguiente.
    
    Precondiciones:
        El dia, mes y año tienen que formar una fecha que exista.
    
    Postcondiciones:
        Devuelve el mismo mes si le mes no termino, el mes que sigue si termino y 1 si ademas era diciembre.
    """
    if dia < _dias_que_tiene(mes, año):
        return mes
    if mes < 12:
        return mes + 1
    return 1

def diasiguiente_año(dia: int, mes: int, año: int) -> int:
    """
    Contrato:
        Recibe una fecha en tres enteros y devuelve el año del dia siguiente.

    Precondiciones:
        El dia, mes y año tyienen que formar una fecha existente.
    
    Postcondiciones:
        Devuelve el mismo año al menos que la fecha sea 31 de diciembre, donde va a devolver el año que sigue.
    """
    if dia < _dias_que_tiene(mes, año):
        return año

    if mes < 12:
        return año

    return año + 1

def _es_anterior(dia1: int, mes1: int, año1: int, dia2: int, mes2: int, año2: int) -> bool:
    """
    Contrato:
        Recibe dos fechas siendo enteros y dice si la priemra es anterior a la segunda.

    Precondiciones:
        Las dos fechas deben existir.
    
    Postcondiciones:
        Devuelve True si la primera es anterior a la segunda, y False si es igual o posterior.
    """
    if año1 < año2:
        return True
    if año1 > año2:
        return False
    if mes1 < mes2:
        return True
    if mes1 > mes2:
        return False
    if dia1 < dia2:
        return True
    return False

def _programa_a() -> None:
    """
    Contrato:
        se le suma a una fecha la cantidad de dias que pida el usuario, va avanzando de a un dia con las funciones, diasiguiente_dia(), diasiguiente_mes() y diasiguiente_año().
    
    Precondiciones:
        no recibe nada, los datos los pide al usuario.
    
    Postcondiciones:
        Muestra por pantalla la fecha a la que se llega despues de sumar los dias.

    """
    while True:
        print("ingresar la fecha de partida: ")
        dia = _pedir_entero("Dia: ")
        mes = _pedir_entero("Mes: ")
        año = _pedir_entero("Año: ")

        if _fecha_existe(dia,mes,año):
            break

        print("Error: esa fecha no existe. ")

    cantidad = _pedir_entero("Cuantos dias queres sumarle: ")

    while cantidad < 0:
        print("Error: la cantidad de dias no puede ser negativa.")
        cantidad = _pedir_entero("Cuantos dias queres sumarle: ")

    sumados = 0

    while sumados < cantidad:
        nuevo_dia = diasiguiente_dia(dia, mes, año)
        nuevo_mes = diasiguiente_mes(dia, mes, año)
        nuevo_año = diasiguiente_año(dia, mes, año)

        dia = nuevo_dia
        mes = nuevo_mes
        año = nuevo_año

        sumados = sumados + 1

    print(f"sumando {cantidad} dias se llega al {dia}/{mes}/{año}.")

def _programa_b() -> None:
    """
    Contrato:
        Cuenta cuantos dias hay entre dos fechas, arrancando de la mas vieja y avanzando de a un dia hasta llegar a la otra.

    Precondiciones:
        No recibe nada, los datos los pide por teclado.

    Postcondiciones:
        muestra por pantalla la cantidad de dias que separan a las dos fechas.
    """
    while True:
        print("Ingresa la primera fecha: ")
        dia1 = _pedir_entero("Dia: ")
        mes1 = _pedir_entero("Mes: ")
        año1 = _pedir_entero("Año: ")

        if _fecha_existe(dia1, mes1, año1):
            break

        print("Error, esa fecha no existe")

    while True:
        print("Ingresa la segunda fecha: ")
        dia2 = _pedir_entero("Dia: ")
        mes2 = _pedir_entero("Mes: ")
        año2 = _pedir_entero("Año: ")

        if _fecha_existe(dia2, mes2, año2):
            break

        print("Error: esa fecha no existe")

    if _es_anterior(dia2, mes2, año2, dia1, mes1, año1):
        guardado_dia = dia1
        guardado_mes = mes1
        guardado_año = año1

        dia1 = dia2
        mes1 = mes2
        año1 = año2

        dia2 = guardado_dia
        mes2 = guardado_mes
        año2 = guardado_año

    dias = 0

    while _es_anterior(dia1, mes1, año1, dia2, mes2, año2):
        nuevo_dia = diasiguiente_dia(dia1, mes1, año1)
        nuevo_mes = diasiguiente_mes(dia1, mes1, año1)
        nuevo_año = diasiguiente_año(dia1, mes1, año1)

        dia1 = nuevo_dia
        mes1 = nuevo_mes
        año1 = nuevo_año 

        dias = dias + 1

    print(f"Entre las dos fechas hay {dias} dias.")



def main() -> None:
    """
    Contrato:
        Ejecuta los programas del ejercicio, uno despues el otro.

    Precondiciones:
        Se tiene que ejecutar como programa principal

    Postcondiciones:
        Muestra por pantalla el resultado de sumarle dias a una fecha y el de contar los dias entre dos fechas
    """
    print("a. Sumar N dias a una fecha")
    _programa_a()

    print("b. Cantidad de dias entre dos fechas")
    _programa_b()

if __name__ == "__main__":
    main()
       