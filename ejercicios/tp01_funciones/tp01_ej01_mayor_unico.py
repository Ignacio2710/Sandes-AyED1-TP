
def _mayor_unico(num, num1, num2):
    """
    Contrato: Esta funcion debe recibir tres numeros los cuales tienen que ser enteros y positivos, 
    Devolviendo el mayor de los tres solo si es unico.

    Precondiciones: Los tres numeros deben ser enteros y positivos.

    Postcondiciones:El mayor debe aparecer una sola vez y devolverlo.
                    Si el mayor aparece mas de una vez devuelve -1.
    """
    if num > num1:
        if num > num2:
            numero_mayor = num
        else:
            numero_mayor = -1
    else:
        if num1 > num:
            if num1 > num2:
                numero_mayor = num1
            else:
                numero_mayor = -1
        else:
            if num2 > num:
                numero_mayor = num2
            else:
                numero_mayor = -1

    return numero_mayor        

num = int(input("Ingrese un numero entero que sea positivo: "))
num1 = int(input("Ingresa tu segundo numero entero y positivo: "))
num2 = int(input("Ingreesa tu tercer numero entero y positivo: "))

resultado = _mayor_unico(num, num1, num2)

if resultado == -1:
    print(f"No existe mayor unico:{_mayor_unico(num, num1, num2)}")

else:
    print(f"El mayor y unico es: {_mayor_unico(num, num1, num2)}")
