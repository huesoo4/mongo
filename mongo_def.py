from pymongo import MongoClient
from datetime import datetime


cliente = MongoClient("mongodb://127.0.0.1:27017/")
db = cliente["universidad"]
coleccion = db["estudiantes"]

def insertar_documento():

    print("\n--- Insertar estudiante ---")


    id_estudiante = -1

    while id_estudiante < 0:

        try:
            id_estudiante = int(input("ID: "))

        except ValueError:
            print("ERROR: Introduce un número entero.")
            id_estudiante = -1


    edad = -1

    while edad < 0:

        try:
            edad = int(input("Edad: "))

        except ValueError:
            print("ERROR: Introduce un número entero.")
            edad = -1


    activo = input("¿Activo? (s/n): ").lower() == "s"


    asignaturas = input(
        "Asignaturas separadas por coma: "
    ).split(",")


    ciudad = input("Ciudad: ")
    codigo_postal = input("Código postal: ")
    pais = input("País: ")


    nota_exam = -1

    while nota_exam < 0 or nota_exam > 100:

        try:
            nota_exam = round(
                float(input("Nota examen: ")), 2
            )

        except ValueError:
            print("ERROR: Introduce una nota válida.")
            nota_exam = -1


    nota_quiz = -1

    while nota_quiz < 0 or nota_quiz > 100:

        try:
            nota_quiz = round(
                float(input("Nota quiz: ")), 2
            )

        except ValueError:
            print("ERROR: Introduce una nota válida.")
            nota_quiz = -1


    nota_homework = -1

    while nota_homework < 0 or nota_homework > 100:

        try:
            nota_homework = round(
                float(input("Nota homework: ")), 2
            )

        except ValueError:
            print("ERROR: Introduce una nota válida.")
            nota_homework = -1

    nuevo_alumno = {
        "_id": id_estudiante,
        "name": input("Nombre: "),
        "age": edad,
        "active": activo,
        "email": None,
        "registration_date": datetime.now(),
        "subjects": asignaturas,
        "address": {
            "city": ciudad,
            "postal_code": codigo_postal,
            "country": pais
        },
        "scores": [
            { "type": "exam", "score": nota_exam },
            { "type": "quiz", "score": nota_quiz },
            { "type": "homework", "score": nota_homework }
        ]
    }

    coleccion.insert_one(nuevo_alumno)
    print("Estudiante insertado correctamente.")


def eliminar_documento():
    print("\n--- Eliminar estudiante ---")
    id_estudiante = int(input("Introduce el _id del estudiante a eliminar: "))

    resultado = coleccion.delete_one({"_id": id_estudiante})

    if resultado.deleted_count > 0:
        print("Estudiante eliminado correctamente.")
    else:
        print("No se encontró ningún estudiante con ese _id.")


def modificar_documento():

    print("\n--- Modificar estudiante ---")

    id_estudiante = -1

    while id_estudiante < 0:
        try:
            id_estudiante = int(input("Introduce el _id del estudiante: "))
        except ValueError:
            print("ERROR: Debes introducir un número entero.")
            id_estudiante = -1


    nueva_edad = -1

    while nueva_edad < 0:
        try:
            nueva_edad = int(input("Nueva edad: "))
        except ValueError:
            print("ERROR: Debes introducir un número entero.")
            nueva_edad = -1


    resultado = coleccion.update_one(
        {"_id": id_estudiante},
        { "$set": { "age": nueva_edad }})


    if resultado.modified_count > 0:
        print("Estudiante actualizado correctamente.")
    else:
        print("No se modificó ningún documento.")


def mostrar_documentos(cursor):
    for doc in cursor:
        print(doc)