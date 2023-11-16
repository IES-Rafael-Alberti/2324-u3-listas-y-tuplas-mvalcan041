
# "Práctica 3.1.1"
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo: Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

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
    formateo_asignaturas = ", ".join(lista_asignaturas)
    formateo_asignaturas += "."

    # Salida:
    print(f"Aquí dejo la lista con las asignaturas: {formateo_asignaturas}")

if __name__ == "__main__":
    main()
    