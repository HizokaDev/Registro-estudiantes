import os
import registro

estudiantes = registro.cargar_datos()

while True:
    os.system("clear")  # Usa "cls" si estás en Windows
    print("\n---- Bot registro de estudiantes Hizoka ----")
    print("1. Agregar un estudiante")
    print("2. Mostrar estudiantes registrados")
    print("3. Mostrar estudiantes registrados en un curso")
    print("4. Mostrar resumen general")
    print("5. Editar registro de estudiante")
    print("6. Eliminar estudiante registrado")
    print("7. Salir")

    opcion = input("Elige una opción (1/2/3/4/5/6/7): ").strip()

    if opcion == "1":
        registro.agregar_estudiante(estudiantes)
    elif opcion == "2":
        registro.mostrar_estudiantes(estudiantes)
    elif opcion == "3":
        registro.mostrar_estudiantes_por_curso(estudiantes)
    elif opcion == "4":
        registro.mostrar_resumen(estudiantes)
    elif opcion == "5":
        registro.editar_estudiante(estudiantes)
    elif opcion == "6":
        registro.eliminar_estudiante(estudiantes)
    elif opcion == "7":
    registro.cargar_datos(estudiantes)
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")

    input("\nPresiona Enter para continuar...")