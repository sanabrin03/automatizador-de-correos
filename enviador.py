import subprocess
import sys
import os
import time
import mimetypes
import smtplib
from email.message import EmailMessage

# 1. MÓDULO DE INSTALACIÓN 
def instalar_dependencias():
    try:
        import pandas 
    except ImportError:
        print(" Instalando herramientas necesarias...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])

# 2. MÓDULO DE ADJUNTOS 
def agregar_adjuntos(msg, ruta_carpeta):
    """Busca y agrega todos los archivos de la carpeta al mensaje."""
    if os.path.exists(ruta_carpeta):
        for archivo in os.listdir(ruta_carpeta):
            ruta_completa = os.path.join(ruta_carpeta, archivo)
            if os.path.isfile(ruta_completa):
                ctype, _ = mimetypes.guess_type(ruta_completa)
                main, sub = (ctype or 'application/octet-stream').split('/', 1)
                with open(ruta_completa, 'rb') as f:
                    msg.add_attachment(f.read(), maintype=main, subtype=sub, filename=archivo)

# 3. LÓGICA DE ENVÍO INDIVIDUAL 
def procesar_envio(server, fila, correo_user, asunto, cuerpo_usuario):
    """Crea y envía un correo individual."""
    msg = EmailMessage()
    msg['Subject'] = asunto
    msg['From'] = correo_user
    msg['To'] = fila['Email']
    
    saludo = f"Hola {fila['Nombre']},\n\n"
    msg.set_content(saludo + cuerpo_usuario)
    
    # Agregamos los adjuntos usando la función que creamos arriba
    agregar_adjuntos(msg, 'adjuntos')
    
    server.send_message(msg)
    print(f" Enviado a: {fila['Email']}")

# 4. FUNCIÓN PRINCIPAL 
def ejecutar_automatizacion():
    try:
        instalar_dependencias()
        import pandas as pd # Importación segura tras la instalación

        if not os.path.exists('contactos.csv'):
            print("Error: No se encuentra 'contactos.csv'.")
            return

        # Configuración inicial
        print("CONFIGURACIÓN")
        opcion = input("1. Gmail / 2. Outlook: ")
        smtp_server = "smtp.gmail.com" if opcion == "1" else "smtp-mail.outlook.com"
        
        user = input("📧 Correo: ")
        pw = input("🔑 Clave de Aplicación (16 letras): ").replace(" ", "")
        print("\n--- 📝 MENSAJE ---")
        asunto = input("📌 Asunto: ")
        print("💬 Escribe el mensaje (Presiona Enter, luego Ctrl+Z y Enter):")
        cuerpo = sys.stdin.read()

        # Cargamos los datos intentando detectar si usa coma o punto y coma automáticamente
        try:
            df = pd.read_csv('contactos.csv', sep=None, engine='python')
        except:
            df = pd.read_csv('contactos.csv') # Fallback por si acaso
        
        print(f"Iniciando envío...")
        with smtplib.SMTP(smtp_server, 587) as server:
            server.starttls()
            server.login(user, pw)

            for i, fila in df.iterrows():
                if i >= 300: break # Límite de seguridad
                procesar_envio(server, fila, user, asunto, cuerpo)
                time.sleep(2) # Pausa anti-spam

        print(f"¡Proceso completado con éxito!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ejecutar_automatizacion()