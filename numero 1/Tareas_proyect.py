import json
import os

ARCHIVO = "tareas.json"


def cargar_tareas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []


def guardar_tareas(tareas):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)


def mostrar_tareas(tareas):
    if not tareas:
        print("\nNo hay tareas registradas.\n")
        return

    print("\n===== LISTA DE TAREAS =====")
    for i, tarea in enumerate(tareas, start=1):
        estado = "✅" if tarea["completada"] else "❌"
        print(f"{i}. {tarea['titulo']} {estado}")
    print()


def agregar_tarea(tareas):
    titulo = input("Ingrese la nueva tarea: ")

    tareas.append({
        "titulo": titulo,
        "completada": False
    })

    guardar_tareas(tareas)
    print("Tarea agregada correctamente.\n")


def completar_tarea(tareas):
    mostrar_tareas(tareas)

    if not tareas:
        return

    try:
        indice = int(input("Número de tarea completada: ")) - 1

        if 0 <= indice < len(tareas):
            tareas[indice]["completada"] = True
            guardar_tareas(tareas)
            print("Tarea marcada como completada.\n")
        else:
            print("Número inválido.\n")

    except ValueError:
        print("Debe ingresar un número.\n")


def eliminar_tarea(tareas):
    mostrar_tareas(tareas)

    if not tareas:
        return

    try:
        indice = int(input("Número de tarea a eliminar: ")) - 1

        if 0 <= indice < len(tareas):
            tarea = tareas.pop(indice)
            guardar_tareas(tareas)
            print(f"'{tarea['titulo']}' eliminada.\n")
        else:
            print("Número inválido.\n")

    except ValueError:
        print("Debe ingresar un número.\n")


def menu():
    tareas = cargar_tareas()

    while True:
        print("===== ADMINISTRADOR DE TAREAS =====")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)

        elif opcion == "2":
            agregar_tarea(tareas)

        elif opcion == "3":
            completar_tarea(tareas)

        elif opcion == "4":
            eliminar_tarea(tareas)

        elif opcion == "5":
            print("Hasta luego.")
            break

        else:
            print("Opción no válida.\n")


if __name__ == "__main__":
    menu()