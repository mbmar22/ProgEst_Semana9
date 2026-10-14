from flask import Flask, render_template, request, redirect, url_for, flash
from dataclasses import dataclass, field

app = Flask(__name__)
app.config["SECRET_KEY"] = "cambia-esta-clave-en-produccion"


@dataclass
class Stack:
    """Pila limitada con operaciones básicas LIFO."""
    capacity: int
    items: list[int] = field(default_factory=list)

    @property
    def is_empty(self) -> bool:
        return len(self.items) == 0

    @property
    def is_full(self) -> bool:
        return len(self.items) >= self.capacity

    def push(self, item: int) -> None:
        if self.is_full:
            raise OverflowError("La pila está llena.")
        self.items.append(item)

    def pop(self) -> int:
        if self.is_empty:
            raise IndexError("La pila está vacía.")
        return self.items.pop()

    def peek(self) -> int | None:
        return None if self.is_empty else self.items[-1]


# Demo educativa: la pila vive en memoria del servidor y es compartida por usuarios.
# Para uso multiusuario, reemplazar por almacenamiento asociado a sesión/usuario.
stack: Stack | None = None


@app.route("/", methods=["GET", "POST"])
def index():
    global stack

    if request.method == "POST":
        action = request.form.get("action", "")

        if action == "create":
            try:
                capacity = int(request.form.get("capacity", ""))
                if not 1 <= capacity <= 100:
                    raise ValueError
            except ValueError:
                flash("Ingresá una capacidad entera entre 1 y 100.", "danger")
            else:
                stack = Stack(capacity=capacity)
                flash(f"Pila creada con capacidad de {capacity} elemento(s).", "success")

        elif stack is None:
            flash("Primero creá una pila para poder operar.", "warning")

        elif action == "push":
            raw_value = request.form.get("item", "").strip()
            try:
                item = int(raw_value)
            except ValueError:
                flash("Ingresá un número entero válido.", "danger")
            else:
                try:
                    stack.push(item)
                except OverflowError as error:
                    flash(str(error), "danger")
                else:
                    flash(f"Se agregó {item} a la pila.", "success")

        elif action == "pop":
            try:
                removed = stack.pop()
            except IndexError as error:
                flash(str(error), "warning")
            else:
                flash(f"Se retiró {removed} de la pila.", "success")

        elif action == "clear":
            stack.items.clear()
            flash("La pila quedó vacía.", "success")

        return redirect(url_for("index"))

    return render_template("index.html", stack=stack)


if __name__ == "__main__":
    app.run(debug=True)
