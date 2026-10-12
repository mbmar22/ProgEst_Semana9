stack = []

def push(item, stack, size, pos):
    if pos < size:
        stack.append(item)
    else:
        return "Pila llena..."


size = int(input("Dime el tamaño de la pila: "))

while True:
    item = input("Dime un valor: ")
    push(item, stack, size, pos)
    answer = 