def mostrar_menu():
    print("\n GESTOR DE TAREAS")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("0. Salir")


def mostrar_tareas(tareas):
    if len(tareas) == 0:
        print("\nNo hay tareas.")
        return

    print("\nTareas:")
    for i in range(len(tareas)):
        estado = "✔" if tareas[i]["completada"] else "❌"
        print(f"{i + 1}. {tareas[i]['texto']} [{estado}]")


def agregar_tarea(tareas):
    texto = input("Escribe la nueva tarea: ")
    tarea = {
        "texto": texto,
        "completada": False
    }
    tareas.append(tarea)
    print("Tarea agregada.")

def completar_tarea(tareas):
    if len(tareas) == 0:
        print("No hay tareas para completar.")
        return

    mostrar_tareas(tareas)

    try:
        numero = int(input("Número de la tarea a completar: "))
        indice = numero - 1

        if indice < 0 or indice >= len(tareas):
            print("Número de tarea inválido.")
            return

        if tareas[indice]["completada"]:
            print("⚠️ Esta tarea ya está completada.")
            return

        tareas[indice]["completada"] = True
        print("✅ Tarea marcada como completada.")

    except ValueError:
        print("Debes ingresar un número.")


def eliminar_tarea(tareas):
    if len(tareas) == 0:
        print("No hay tareas para eliminar.")
        return

    mostrar_tareas(tareas)

    try:
        numero = int(input("Número de la tarea a eliminar: "))
        indice = numero - 1

        if indice < 0 or indice >= len(tareas):
            print("Número de tarea inválido.")
            return

        tareas.pop(indice)
        print("🗑️ Tarea eliminada.")

    except ValueError:
        print("Debes ingresar un número.")

def main():
    tareas = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)

        elif opcion == "2":
            agregar_tarea(tareas)

        elif opcion == "3":
            completar_tarea(tareas)

        elif opcion == "4":
            eliminar_tarea(tareas)

        elif opcion == "0":
            print("Saliendo del gestor de tareas.")
            break

        else:
            print("❌ Opción inválida.")

main()
