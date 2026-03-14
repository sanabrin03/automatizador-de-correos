# Automatizador de Correos Inteligente (Python)

Desarrollé esta herramienta para simplificar el envío de correos masivos personalizados, eliminando la necesidad de procesos manuales y garantizando que el usuario final no tenga que tocar ni una sola línea de código.

# Características Principales
1) Instalación Automática: El script detecta si faltan librerías (como Pandas) y las instala por ti.
2) Seguridad: No guarda tus contraseñas. El programa te las solicita de forma segura cada vez que lo ejecutas.
3) Multimedia: Soporta el envío de múltiples archivos adjuntos (PDF, Imágenes, etc.) de forma simultánea.
4) Comportamiento Humano: Incluye retardos programados entre envíos para evitar bloqueos y filtros de spam.

# Guía Rápida para Usuarios
1. Preparación: Coloca tus contactos en el archivo `contactos.csv`.
    - Mete todos los archivos que quieras enviar en la carpeta llamada `adjuntos`.
2. Seguridad: Debes usar una Contraseña de Aplicación (16 caracteres). No uses tu contraseña normal.
    Para eso debes hacer:
    - Gmail: Configuración > Seguridad > Contraseñas de aplicaciones. Si llegas a tener problemas buscandolo usa este enlace: https://myaccount.google.com/apppasswords
    - Outlook: Configuración > Seguridad > Opciones de seguridad avanzada.
3.  Ejecución: Abre una terminal en la carpeta y escribe:
    `python enviador.py`
4.  Uso: El programa te guiará paso a paso para elegir tu proveedor, redactar el asunto y escribir el mensaje. Al finalizar el mensaje, presiona `Enter`, luego `Ctrl+Z` y otra vez `Enter`.
#  Importante: Si usas Excel
Al crear tu lista de contactos en Excel, sigue estos pasos para que el script no falle:
1. Ve a Archivo > Guardar como.
2. En tipo de archivo, elige CSV (delimitado por comas) (*.csv).
3. Nota técnica: Si al ejecutar el script ves un error de "columnas no encontradas", es probable que tu Excel use punto y coma (`;`). No te preocupes, el script está diseñado para entender ambos formatos si lo configuras en la línea 45.


**Desarrollado por Samuel Sanabria | 2026**