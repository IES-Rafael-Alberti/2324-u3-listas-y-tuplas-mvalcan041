
# "Práctica 3.1.9"
# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

# Función (o no) que pida una palabra str, hacerla .lower, función que incluya las variables de cada letra vacías
# y que además use un for (letra in palabra) que con if y elif sume +1 al contador de cada vocal si la contiene
# con un if letra == 'x'

def vocal(palabra):
    
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    for vocal in palabra:
        if vocal == 'a':
            a = a + 1
        elif vocal == 'e':
            e = e + 1
        elif vocal == 'i':
            i = i + 1
        elif vocal == 'o':
            o = o + 1
        elif vocal == 'u':
            u = u + 1

    lista_vocales = list(a,e,i,o,u)
    return lista_vocales
                        
def str_input() -> str:
    
    palabra = input("Dígame una palabra:\n")
    palabra = palabra.lower()
    
    return palabra

def main():
    
    palabra = str_input()
    
    
    print(vocal(palabra))



if __name__ == "__main__":
    main()

# Por acabar.