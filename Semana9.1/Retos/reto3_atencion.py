# Reto 3 · Sistema de atención al cliente

'''
- Registrar cliente con número de turno y nombre.
- Atender al siguiente (FIFO), consultar siguiente, listar pendientes y contar elementos.
- Validar nombres vacíos y atención con cola vacía.
- reto3_atencion.py
- Menú interactivo.
- Pruebas con 5 clientes.
- Diagrama de entrada/salida.

'''

import os, sys, time

def header():
    print("----- Reto 3 · Sistema de atención al cliente -----".title())


def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def userChooseContinue():
    input("")


waitTime = 0.7

def wait(message, item, repetitions, waitTime):
    print("\n" + message, end = "")
    for i in range(repetitions):
        print(item, end = "", flush = True)
        time.sleep(waitTime)
    userChooseContinue()
    
def emptyList(lista):
    if len(lista) <= 0:
        return True
    else:
        return False



standardWait = wait("Regresando al menú", ".", 3, waitTime)

#---------------------------------------------------------------------------

def registerClient(lista):
    print("-- Registrar Cliente --")

    standardWait

def nextClient(lista):
    print("-- Siguiente Cliente --")
    if emptyList(lista) == True:
        print("\nLa lista de clientes se siente vacía.")
        standardWait
    else:
        print(f"Siguiente cliente: {lista[0]}")
        standardWait


def checkNext():
    print("checkNext")
    standardWait

def checkToDo():
    print("checkToDo")
    standardWait

def countClients():
    print("countClients")
    wait("Regresando al menú", ".", 3, waitTime)


#---------------------------------------------------------------------------


def menu():
    options = {
        1: lambda: registerClient(),
        2: lambda: nextClient(),
        3: lambda: checkNext(),
        4: lambda: checkToDo(),
        5: lambda: countClients(),
        6: lambda: sys.exit(),
    }

    clientes = []

    while True:
        clearTerminal()
        header()
        print("\n1. Registrar cliente.")
        print("2. Atender siguiente cliente.")
        print("3. Consultar siguiente cliente.")
        print("4. Lista de clientes.")
        print("5. Contar clientes.")
        print("6. Salir.")

        userInput = None

        while True:
            try:
                userInput = int(input("\nIngrese una opción: "))

                if userInput in options:
                    break

            except ValueError:
                print("Ingrese una opción válida (1-6).")

        clearTerminal()
        options[userInput]()

menu()