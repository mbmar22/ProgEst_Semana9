# Visualizador de colas FIFO con Flask

## Requisitos
- Python 3.10 o superior
- Navegador moderno
- Conexión a Internet para cargar Bootstrap desde CDN (y reconocimiento de voz, según navegador)

## Instalación y ejecución

1. Descomprimí el proyecto.
2. Abrí una terminal dentro de la carpeta del proyecto.
3. Creá y activá un entorno virtual (opcional, recomendado):

   Windows:
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Instalá las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

5. Ejecutá la aplicación:

   ```bash
   python app.py
   ```

6. Abrí http://127.0.0.1:5000 en el navegador.

## Voz
La API Web Speech no funciona en todos los navegadores. Probá una versión reciente de Chrome o Edge y permití el micrófono. Para producción, configurá `FLASK_SECRET_KEY` con una clave segura y usá HTTPS.

## Buenas prácticas incluidas
- Validación de entradas vacías.
- Cola independiente por sesión de navegador.
- `deque.popleft()` para desencolar en O(1), en lugar de `list.pop(0)`.
- Respuestas JSON y mensajes de error claros.
- Renderizado de texto con `textContent` para evitar insertar el contenido del usuario como HTML.
- Modo debug desactivado por defecto.
