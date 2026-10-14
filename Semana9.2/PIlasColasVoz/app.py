import os
from collections import deque

from flask import Flask, jsonify, render_template, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", "cambia-esta-clave-en-produccion")


def encolar(queue, element):
    """Agrega un elemento al final de la cola."""
    element = str(element).strip()
    if not element:
        raise ValueError("El elemento no puede estar vacío.")
    queue.append(element)


def desencolar(queue):
    """Retira y devuelve el primer elemento; None si está vacía."""
    if not queue:
        return None
    return queue.popleft()


def esta_vacia(queue):
    """Indica si la cola no contiene elementos."""
    return len(queue) == 0


def obtener_cola():
    """Carga la cola de la sesión como deque para operar en FIFO."""
    return deque(session.get("cola", []))


def guardar_cola(queue):
    """Guarda la cola en la sesión como una lista serializable."""
    session["cola"] = list(queue)
    session.modified = True


@app.get("/")
def inicio():
    return render_template("index.html", cola=session.get("cola", []))


@app.post("/api/encolar")
def api_encolar():
    data = request.get_json(silent=True) or {}
    element = data.get("elemento", "")
    if not isinstance(element, (str, int, float)):
        return jsonify(error="El elemento debe ser texto o un número."), 400

    queue = obtener_cola()
    try:
        encolar(queue, element)
    except ValueError as exc:
        return jsonify(error=str(exc)), 400

    guardar_cola(queue)
    return jsonify(cola=list(queue), mensaje=f"Se encoló: {str(element).strip()}"), 201


@app.post("/api/desencolar")
def api_desencolar():
    queue = obtener_cola()
    element = desencolar(queue)
    if element is None:
        return jsonify(error="La cola está vacía."), 400

    guardar_cola(queue)
    return jsonify(cola=list(queue), elemento=element, mensaje=f"Se desencoló: {element}")


@app.get("/api/cola")
def api_mostrar_cola():
    queue = session.get("cola", [])
    return jsonify(cola=queue, vacia=len(queue) == 0, cantidad=len(queue))


@app.post("/api/vaciar")
def api_vaciar():
    guardar_cola(deque())
    return jsonify(cola=[], mensaje="La cola se vació correctamente.")


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
