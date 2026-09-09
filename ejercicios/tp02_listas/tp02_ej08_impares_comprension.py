# TP02 - Ejercicio 08
# Construye por comprension la lsita de los numneros impares entre 100 y 200

PRIMER_IMPAR = 101
LIMITE = 201
PASO = 2

def _impares() -> list[int]:
    """
    Contrato:
        Construye por comprension la lista de los numeros impares comprendidos entre 100 y 200

    Precondiciones:
        ninguna
    
    Postcondiciones:
        Devuelve una lista nueva con los impares desde PRIMER_IMPAR hasta LIMITE sin incluirlo, en orden ascendente
    """
    return  [numero for numero in range(PRIMER_IMPAR, LIMITE, PASO)]



def main() -> None:
    """
    Contrato:
        Ejercuta el programa principal arma la lista de impares y la muestra
    
    Precondiciones:
        El archivo se tiene que ejecutar como principal
    
    Postcondiciones:
        Se muestra por pantalla la lista de impares y cuantos son.
    """
    impares = _impares()

    print(f"Impares entre 100 y 200: {impares}")
    print(f"La lista tiene {len(impares)} numeros")


if __name__ == "__main__":
    main()