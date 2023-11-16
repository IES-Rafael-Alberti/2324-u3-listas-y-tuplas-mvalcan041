
# "Práctica 3.1.3"
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

def ingresar_notas(asignaturas: list) -> list:
    """Función el ingreso de notas según la asignatura.

    Args:
        asignaturas (list): Lista con asignaturas previamente almacenadas.

    Returns:
        list: Lista con las notas en el orden establecido por la lista de las asignaturas almacenadas.
    """
    notas = []
    
    for asignatura in asignaturas:
        nota = input(f"¿Qué nota has sacado en {asignatura}?:\n")
        notas.append(nota)
    
    return notas

def mostrar_notas(asignaturas: list, notas: list) -> str:
    """Función que muestra las notas obtenidas según la asignatura.

    Args:
        asignaturas (list): Lista con asignaturas previamente almacenadas.
        notas (list): Lista con las notas previamente almacenadas.
    """
    print("Notas obtenidas:")
    
    for i in range(len(asignaturas)):
        print(f"En {asignaturas[i]} has sacado un {notas[i]}.")


def main():

    # Entrada:
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

    # Procesamiento:
    notas = ingresar_notas(asignaturas)

    # Salida:
    mostrar_notas(asignaturas, notas)

if __name__ == "__main__":
    main()