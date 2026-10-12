import os

# Diapositiva 7
print("\n-----  Diapositiva 7  -----")
pila = []

pila.append("Matemáticas")
pila.append("Programación")
pila.append("Base de Datos")

print("Tope: ", pila[-1])
print("Retirado: ", pila.pop())
print("Tope: ", pila)



# Diapositiva 8
print("\n-----  Diapositiva 8  -----")
def desapilar(pila):
    if not pila:
        print("La pila está vacía")
        return None
    return pila.pop()

pila = []
print(desapilar(pila))


# Diapositiva 14
print("\n-----  Diapositiva 14  -----")
from collections import deque

cola = deque()
cola.append("Ana")
cola.append("Luis")
cola.append("María")

print("Primero: ", cola[0])
print("Atendiendo: ", cola.popleft())
print("En espera: ", list(cola))


