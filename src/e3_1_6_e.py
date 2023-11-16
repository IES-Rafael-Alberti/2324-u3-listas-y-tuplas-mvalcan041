
# "Práctica 3.1.6"
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

def ingresar_notas(asignaturas: list) -> list:
    """Función el ingreso de notas según la asignatura.

    Args:
        asignaturas (list): Lista con asignaturas previamente almacenadas.

    Returns:
        list: Lista con las notas en el orden establecido por la lista de las asignaturas almacenadas.
    """
    notas = []
    
    for asignatura in asignaturas:
        nota = int(input(f"¿Qué nota has sacado en {asignatura}?:\n"))
        notas.append(nota)

    return notas

def comp_notas(notas: list) -> list:
    """Función que comprueba si alguna nota es menor que 5 y las almacena en una lista nueva.

    Args:
        notas (list): Lista con notas previamente almacenadas, de la función 'ingresar_notas'.

    Returns:
        list: Lista nueva llamada 'pendientes' con las notas que son menores a 5.
    """
    pendientes = []
    
    for nota in notas:
        if nota < 5:
            pendientes.append(nota)
    
    return pendientes

def comp_asignaturas(pendientes: list, asignaturas: list) -> list:
    """_summary_

    Args:
        pendientes (list): _description_
        asignaturas (list): _description_

    Returns:
        list: _description_
    """
    asignaturas_pendientes = []

    for i in range(len(asignaturas)):
        if pendientes[i] < 5:
            asignaturas_pendientes.append(asignaturas[i])

    return asignaturas_pendientes

def main():

    # Entrada:
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

    # Procesamiento:
    notas = ingresar_notas(asignaturas)
    pendientes = comp_notas(notas)
    asignaturas_pendientes = comp_asignaturas(pendientes, asignaturas)

    # Salida:
    if asignaturas_pendientes:
        print("Debes repetir las siguientes asignaturas:")
        for asignatura in asignaturas_pendientes:
            print(f" - {asignatura}")
    
    else:
        print("¡Enhorabuena, has aprobado todas las asignaturas!")

if __name__ == "__main__":
    main()

# Ver bien, error en el procesamiento; asignaturas_pendientes.
# Me doy cuenta que estoy quizás complicándome a la hora de hacer hasta 3 funciones para devolver una lista con las asignaturas que tienen menos de un 5 de nota.
# El código ahora mismo da que si i.e. saco un 3 en 'Historia' y un 2 en 'Lengua', la función 'comp_asignaturas' devuelve 2 asignaturas pendientes, pero no las suspensas.
# En ese caso en concreto devolverá 'Matemáticas' y 'Física', que son casualmente las 2 primeras posiciones de la lista 'asignaturas', dado que son 2 las suspensas.
# Lo esperado sería en 'asignaturas_pendientes' ['Historia', 'Lengua'].