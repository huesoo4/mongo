from mongo_def import *
import os


def menu():

    opcion = ""

    while opcion != "9":

        print("\n========== MENÚ MONGODB ==========\n")
        print("1. Insertar estudiante")
        print("2. Eliminar estudiante")
        print("3. Modificar estudiante")
        print("4. Consulta simple")
        print("5. Consulta con arrays")
        print("6. Consulta con documentos embebidos")
        print("7. Consulta con array de documentos")
        print("8. Consulta de agrupación")
        print("9. Salir")

        opcion = input("\nElige una opción: ")

        os.system("clear")

        if opcion == "1":
            insertar_documento()

        elif opcion == "2":
            eliminar_documento()

        elif opcion == "3":
            modificar_documento()

        elif opcion == "4":
            consulta_simple()

        elif opcion == "5":
            consulta_array()

        elif opcion == "6":
            consulta_documento_embebido()

        elif opcion == "7":
            consulta_scores()

        elif opcion == "8":
            consulta_agrupacion()

        elif opcion == "9":
            print("Saliendo del programa...")

        else:
            print("Opción no válida")


if __name__ == "__main__":
    menu()