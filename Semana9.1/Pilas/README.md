# Visualizador de pilas con Flask

## Requisitos
- Python 3.10 o superior
- Conexión a internet para cargar Bootstrap desde CDN

## Instalación y ejecución (Windows / PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```
Abrí http://127.0.0.1:5000 en el navegador.

## Nota
La pila se almacena en memoria y es compartida por todas las personas que accedan a esta demo. Reiniciar el servidor borra su contenido. Para una aplicación multiusuario, asociá la pila a la sesión o guardala en una base de datos.
