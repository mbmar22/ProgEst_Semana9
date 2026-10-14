stack = []
size = 0
pos = 0

def push(item, stack, size, pos):
    if pos < size:
        stack.append(item)
        pos += 1
    else:
        return "Pila llena..."


def show(stack):
    my_stack = f""
    my_stack += "┌" + "—" * 8 + "┐\n"
    my_stack += "|  PILA  |\n"
    for item in reversed(stack):
        my_stack += f"|" + "—" * 8 + "|\n"
        my_stack += f"| {item:>6} |\n"
    my_stack += "└" + "—" * 8 + "┘"
    return my_stack


def peek(stack):
    if isEmpty(stack):
        return "La pila está vacía"
    return stack[-1]

def isEmpty(stack):
    return not stack

def len_stack(stack):
    if isEmpty(stack):
        return "La pila está vacía..."
    return len(stack)

print(peek(stack))
size = int(input("Dime el tamaño de la pila: "))


def MenuPrincipal():
    while True:
        try:
            item = int(input("Ingrese un valor: "))
            valor = (push(item, stack, size, pos))
            print(valor)
            answer = input("¿Desea ingresar otro valor? [S|N]: ")
            if answer.lower() == "n" or valor == "Pila llena...":
                print(show(stack))
                break
        except ValueError, SystemError:
            print("Intente de nuevo.")

MenuPrincipal()