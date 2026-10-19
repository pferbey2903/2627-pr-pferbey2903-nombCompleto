
def formatear_nombre(nombre: str, apellido1: str, apellido2: str) -> str:
    """
    Formatea el nombre completo de una persona
    :param nombre: El nombre introducido
    :param apellido1: El primer apellido introducido
    :param apellido2: El segundo apellido introducido
    :return: un str de los 3 parámetros formateados, nombre, apellido1 y apellido2  
    """
    nombre: str = nombre.strip().title()
    apellido1: str = apellido1.strip().title()
    apellido2: str = apellido2.strip().title()

    return f"{nombre} {apellido1} {apellido2}"

def main():
    """Función principal"""

    nombre = str(input("Introduce tu nombre: "))
    apellido1 = str(input("Introduce tu primer apellido: "))
    apellido2 = str(input("Introduce tu segundo apellido: "))


    print(f"{formatear_nombre(nombre, apellido1, apellido2)}")

if __name__ == "__main__":
    main()