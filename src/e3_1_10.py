
# "Práctica 3.1.10"
# Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.

def main():
    
    # Entrada:
    precios = [50, 75, 46, 22, 80, 65, 8]

    # Procesamiento:
    precios.sort()

    # Salida:
    print(f"El número menor es {precios[0]} y el número mayor es {precios[len(precios)-1]}.")

if __name__ == "__main__":
    main()