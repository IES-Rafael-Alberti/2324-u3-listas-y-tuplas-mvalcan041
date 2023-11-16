
# "Práctica 3.1.2"
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.

def mostrar_asig(asignaturas: list) -> list:
    """Función que muestra las asignaturas almacenadas en una lista.

    Args:
        asignaturas (list): Lista con las asignaturas almacenadas.

    Returns:
        list: Retorna la misma lista con las asignaturas almacenadas.
    """
    return asignaturas


def main():

    # Entrada:
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

    # Procesamiento:
    lista_asignaturas = mostrar_asig(asignaturas)
    formateo_asignaturas = ", ".join(lista_asignaturas[0:3])
    formateo_asignaturas += " y " + lista_asignaturas[4]

    # Salida:
    print(f"Yo estudio {formateo_asignaturas}.")

if __name__ == "__main__":
    main()
