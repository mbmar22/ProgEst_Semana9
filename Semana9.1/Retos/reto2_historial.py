# Reto 2 · Historial de navegación
'''
- Al visitar una página nueva:
    - Conservar la anterior en una pila.
    - Al regresar, extraer la última página guardada.

- Implementar:
    - Visitar
    - Regresar
    - Mostrar actual
    - Mostrar historial.

'''

import os, sys, time

historial = []

chosenTime = 0.7

def userChooseContinue():
    input("")

def wait(message, item, repetitions, waitTime):
    print("\n" + message, end = "")
    for i in range(repetitions):
        print(item, end = "", flush = True)
        time.sleep(waitTime)
    userChooseContinue()

def header():
    print("--- Reto 2 · Historial de navegación ---")

def visit(userInput, paginas, history):
    print("Páginas disponibles: ")
    for pagina in paginas:
        print(f"- {pagina}")

    opcion = input("Escriba la URL que desea visitar: ").strip().lower()

    if opcion in paginas:
        history.append(opcion)
        print(f"Visitar: {opcion}")
    else: 
        print("URL no encontrada.")

    wait("Regresando", ".", 3, chosenTime)


def goBack(lista):
    if len(lista) <= 1:
        print("No hay registros anteriores.")
        wait("Regresando", ".", 3, chosenTime)
        return

    lista.pop()
    print(f"Regresar → {lista[-1]}")
    wait("Regresando", ".", 3, chosenTime)
    

def showCurrent(lista):
    if emptyHistory(lista) == 0:
        print("No ha entrado a ninguna página.")
        wait("Regresando", ".", 3, chosenTime)
    else:
        print(f"Página actual: {lista[-1]}")
        wait("Regresando", ".", 3, chosenTime)
        return print(lista[-1])


def emptyHistory(lista):
    return len(lista)


def showHistory(lista):
    print("\n- Historial -")

    if emptyHistory(lista) == 0:
        print("Historial vacío. Nada que mostrar.")

    else:
        for i, pagina in enumerate(lista, start=1):
            print(f"{i}. {pagina}")

    wait("Regresando", ".", 3, chosenTime)


def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    paginas = ["uam.edu.ni", "python.org", "github.com"]

    userInput = None

    options = {
        1: lambda: visit(userInput, paginas, historial),
        2: lambda: goBack(historial),
        3: lambda: showCurrent(historial),
        4: lambda: showHistory(historial),
        5: lambda: sys.exit()
    }

    while True:
        clearTerminal()
        header()
        print("--- NAVEGADOR ---")
        print("1. Visitar.")
        print("2. Regresar.")
        print("3. Mostrar actual.")
        print("4. Mostrar historial.")
        print("5. Salir.")


        print("\nVisitar: ")
        print(" - UAM (uam.edu.ni)")
        print(" - Python(python.org)")
        print(" - Github(github.com)")

        while True:
            try:
                userInput = input("\nNavegador: ")

                if not userInput:
                    print("Ingrese una opción válida.")
                    continue

                userInput = int(userInput)

                if userInput in options:
                    break

                print("Seleccione una opción válida.")
                
            except ValueError:
                print("Ingrese una URL válida.")

        clearTerminal()
        options[userInput]()


menu()