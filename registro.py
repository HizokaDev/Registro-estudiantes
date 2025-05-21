# registro.py
import json

def guardar_datos(estudiantes, archivo="estudiantes.json"):
    with open(archivo, "w") as f:
        json.dump(estudiantes, f)
    print("Datos guardados correctamente.")

def cargar_datos(archivo="estudiantes.json"):
    try:
        with open(archivo, "r") as f:
            estudiantes = json.load(f)
        print("Datos cargados correctamente.")
        return estudiantes
    except FileNotFoundError:
        print("No se encontró un archivo anterior. Empezando con lista vacía.")
        return {}

def saludar():
    print("Hola desde el archivo registro.py")
    
def agregar_estudiante(estudiantes):
    nombre = input("Nombre del estudiante: ").strip().lower()

    if nombre in estudiantes:
        print("Ese estudiante ya está registrado.")
        return

    while True:
        edad = input("Edad: ").strip()
        if edad.isdigit():
            break
        else:
            print("Por favor, ingresa un número válido para la edad.")

    curso = input("Curso: ").strip().lower()

    estudiantes[nombre] = {
        "edad": edad,
        "curso": curso,
    }
    print("Estudiante registrado con éxito.")

def agregar_estudiante(estudiantes):
    nombre = input("Nombre del estudiante: ").strip().lower()
    if nombre in estudiantes:
        print("Ese estudiante ya está registrado.")
        return

    while True:
        edad = input("Edad: ").strip()
        if edad.isdigit():
            break
        else:
            print("Por favor, ingresa un número válido para la edad.")

    curso = input("Curso: ").strip().lower()

    estudiantes[nombre] = {
        "edad": edad,
        "curso": curso,
    }
    print(f"Estudiante {nombre.title()} agregado correctamente.")


def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("\nNo hay estudiantes registrados aún.")
        return

    print("\nEstudiantes registrados:")
    for nombre, datos in estudiantes.items():
        print(f"\nNombre: {nombre.title()}")
        print(f"Edad: {datos['edad']}")
        print(f"Curso: {datos['curso'].title()}")


def mostrar_estudiantes_por_curso(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados aún.")
        return

    curso = input("Ingresa el nombre del curso que deseas consultar: ").strip().lower()
    encontrados = [nombre.title() for nombre, datos in estudiantes.items() if datos["curso"] == curso]

    if encontrados:
        print(f"\nEstudiantes inscritos en el curso '{curso}':")
        for nombre in encontrados:
            print(f"- {nombre}")
    else:
        print(f"\nNo se encontraron estudiantes en el curso '{curso}'.")


def mostrar_resumen(estudiantes):
    if not estudiantes:
        print("\nNo hay estudiantes registrados aún.")
        return

    total = len(estudiantes)
    cursos = {}
    suma_edades = 0

    for datos in estudiantes.values():
        curso = datos["curso"]
        edad = int(datos["edad"])
        suma_edades += edad
        cursos[curso] = cursos.get(curso, 0) + 1

    promedio_edad = suma_edades / total

    print("\n--- Resumen general ---")
    print(f"Total de estudiantes: {total}")
    print(f"Edad promedio: {promedio_edad:.1f} años")
    print("Estudiantes por curso:")
    for curso, cantidad in cursos.items():
        print(f"- {curso.title()}: {cantidad}")


def editar_estudiante(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados aún.")
        return

    estudiante = input("Ingresa el nombre del estudiante que deseas editar: ").strip().lower()

    if estudiante not in estudiantes:
        print(f"No se encontró al estudiante '{estudiante.title()}'.")
        return

    print(f"\nEstudiante encontrado: {estudiante.title()}")
    print("¿Qué deseas editar?")
    print("1. Edad")
    print("2. Curso")
    opcion = input("Elige una opción (1/2): ").strip()

    if opcion == "1":
        nueva_edad = input("Ingresa la nueva edad: ").strip()
        if nueva_edad.isdigit():
            estudiantes[estudiante]["edad"] = nueva_edad
            print("Edad actualizada correctamente.")
        else:
            print("Edad inválida. Debe ser un número.")
    elif opcion == "2":
        nuevo_curso = input("Ingresa el nuevo curso: ").strip().lower()
        estudiantes[estudiante]["curso"] = nuevo_curso
        print("Curso actualizado correctamente.")
    else:
        print("Opción inválida.")


def eliminar_estudiante(estudiantes):
    estudiante = input("Ingresa el estudiante que deseas eliminar: ").lower()
    if estudiante not in estudiantes:
        print(f"\nNo se encontraron estudiantes con ese nombre.")
    else:
        print(f"¿Estás seguro que deseas eliminar a {estudiante.title()}?")
        opcion = input("si/no: ").lower()
        if opcion == "si":
            del estudiantes[estudiante]
            print("Estudiante eliminado.")
        else:
            print("No se eliminó al estudiante.")