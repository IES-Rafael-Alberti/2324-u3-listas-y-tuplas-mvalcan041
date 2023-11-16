
# "Práctica 3.1.5"
# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

def main():

    # Entrada:
    lista_numeros = list(range(1, 11))
    
    # Procesamiento:
    lista_numeros_invertidos = list(reversed(lista_numeros))
    resultado = ", ".join(map(str, lista_numeros_invertidos))
        
    # Salida:
    print(resultado + ".")

if __name__ == "__main__":
    main()
