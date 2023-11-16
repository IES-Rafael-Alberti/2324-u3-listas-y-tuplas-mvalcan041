
# "Práctica 3.1.4"
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

def ingresar_numeros_ganadores():
    """Función que permite el input de números a una lista, acaba si se le da una cadena vacía y controla si se le da algo que no sea un número, en su caso lo marcará como un error de valor.

    Returns:
        list: Retorna una lista de números.
    """
    numeros_ganadores = []
    
    while True:
        try:
            numero = input("Indica un número ganador (ó presione la tecla intro para terminar):\n")
            if numero == "":
                break
            
            numero = int(numero)
            if numero < 0:
                raise Exception("Error, has indicado un número negativo.")
            
            numeros_ganadores.append(numero)
        
        except ValueError:
            print("Error, ingrese un número válido.")
        except Exception as e:
            print(e)
    
    return numeros_ganadores


def main():

    # Entrada:
    numeros_ganadores = ingresar_numeros_ganadores()

    # Procesamiento:
    numeros_ganadores.sort()

    # Salida:
    if numeros_ganadores:
        print("Aquí están los números de la lotería ordenados de menor a mayor:")
        for numero in numeros_ganadores:
            print(f" - {numero}")

    else:
        print("No has indicado ningún número ganador.")

if __name__ == "__main__":
    main()