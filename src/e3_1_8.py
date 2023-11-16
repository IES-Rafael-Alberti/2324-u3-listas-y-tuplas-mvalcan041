# "Práctica 3.1.8"
# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

def comp_palabra(palabra: str) -> bool:
    
    palabra = palabra.lower()
    arbalap = palabra[::-1]

    if arbalap == palabra:
        return True
    else:
        return False

def main():
    palabra = input("Indique una palabra:\n")
    
    if comp_palabra(palabra) == True:
        print("Enhorabuena, su palabra es un palíndromo.")
    else:
        print("Lo siento.")
    
if __name__ == "__main__":
    main()