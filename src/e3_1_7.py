
# "Práctica 3.1.7"
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

def main():

    # Entrada:
    abecedario = list("abcdefghijklmnñopqrstuvwxyz")

    # Procesamiento:
    abecedario_limpio = []
    
    for i, letra in enumerate(abecedario, start=1):
        if i % 3 != 0:
            abecedario_limpio.append(letra)

    # Salida:
    print(abecedario_limpio)


if __name__ == "__main__":
    main()
