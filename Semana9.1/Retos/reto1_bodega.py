# Reto 1 · Control de cajas en bodega
'''
Problema:
- Crear un menú: 
    - Apilar caja - Listo
    - Desapilar - Listo
    - Consultar tope - Listo
    - Mostrar pila - Listo
    - Salir. - Listo.

- No aceptar:
    - Códigos vacíos - Listo 
    - Ni duplicados - Listo

- Mostrar cantidad de cajas - Listo
- Validar pila vacía. - Listo.
'''
import os, sys, time

def header():
    print("----- Reto 1 · Control de cajas en bodega -----")


def exitOption():
    print("Si desea salir escriba 's'.")


def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


'''def chooseOption(userInput, option, function):
    if userInput == option:
        function
'''

def chooseOption(option, function):
    function()

def wait(message, item, repetitions, waitTime):
    print("\n" + message, end = "")
    for i in range(repetitions):
        print(item, end = "", flush = True)
        time.sleep(waitTime)
    userChooseContinue()


def desapilar(pila):
    if not pila:
        print("La pila está vacía")
        return None
    return pila.pop()


def userChooseContinue():
    input("")


def emptyPile(box):
    contador = 0
    for i in box:
        contador += 1
    return contador


''' ----------------------------------------------------------------------------------- '''

def pileBox(box):
    print("--- 1. Apilar caja ---")
    exitOption()
    while True:
        add = input("¿Qué desea apilar?: ")
        if add.lower() == "s": # Que pasa si el valor que desea ingresar es 's'?
            if emptyPile(box) == 0:
                wait("Redirigiendo al menú principal", ".", 3, 0.6)
            else:
                wait("¡Datos guardados con éxito!", ".", 3, 0.6)
            break
        else:
            add = add.lstrip()
            add = add.rstrip()
            if add in box:
                print("Ya existe un valor igual.\n")
            elif add.isspace() == True or add == "":
                print("No se admiten espacios vacíos.\n")
            else:
                box.append(add)

    return box


def unpileBox(box):
    print("--- 2. Desapilar caja ---")
    if not box:
        print("Pila vacía. Agrega un elemento para desapilarlo.")
    else:
        print(f"Elemnto desapilado: '{box.pop()}'.")   
    wait("Redirigiendo al menú principal", ".", 3, 0.7)
    return box


def consultTop(box):
    print("--- 3. Consultar tope ---")
    if emptyPile(box) == 0: # Tal vez hacer de esto una función porque se usa varias veces.
        print("Pila vacía.")
    else:
        print(f"El tope de la caja es: {box[-1]}.")
    wait("Redirigiendo al menú principal", ".", 3, 0.7)


def showPile(box):
    print("--- 4. Mostrar pila ---")
    
    print(box)

    if emptyPile(box) == 0:
        print("La pila está vacía")

    else:
        print(f"La pila contiene {emptyPile(box)} elementos.")

    wait("Redirigiendo al menú principal", ".", 3, 0.7)


''' ----------------------------------------------------------------------------------- '''

box = []

def menu():
    options = {
    1: lambda: pileBox(box),
    2: lambda: unpileBox(box),
    3: lambda: consultTop(box),
    4: lambda: showPile(box),
    5: lambda: sys.exit()
    }

    while True:
        clearTerminal()
        header()
        print("1. Apilar caja.")
        print("2. Desapilar caja.")
        print("3. Consultar tope.")
        print("4. Mostrar pila.")
        print("5. Salir.")

        while True:
            userInput = None
            try:
                userInput = input("\nIngrese una opción: ") 

                if userInput.isspace() == True:
                    print("No se admiten espacios vacíos.")
                
                userInput = int(userInput)

                if userInput in options:
                    break

            except ValueError:
                print("Ingrese una opción válida (1-5).\n")

        clearTerminal()
        options[userInput]()

menu()



