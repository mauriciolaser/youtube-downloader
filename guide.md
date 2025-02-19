# Guía de Instalación en Windows para YouTube MP3 Downloader

Esta guía te ayudará a configurar tu entorno en Windows para ejecutar la aplicación "YouTube MP3 Downloader" (el código se encuentra en el directorio `src/`).

## Requisitos Previos

- **Python 3:**  
  Descarga e instala la última versión de Python desde [python.org](https://www.python.org/downloads/). Durante la instalación, asegúrate de marcar la opción "Add Python to PATH".

- **ffmpeg:**  
  La aplicación requiere ffmpeg para extraer y convertir el audio. Descarga la versión estática para Windows desde [ffmpeg.org](https://ffmpeg.org/download.html).  
  **Pasos para configurar ffmpeg:**
  1. Extrae el contenido en una carpeta (por ejemplo, `C:\ffmpeg`).
  2. Agrega la ruta `C:\ffmpeg\bin` a la variable de entorno `PATH`:
     - Haz clic derecho en "Este equipo" y selecciona "Propiedades".
     - Haz clic en "Configuración avanzada del sistema" y luego en "Variables de entorno".
     - En "Variables del sistema", localiza y edita la variable `Path` para incluir la ruta a `C:\ffmpeg\bin`.
  3. Reinicia la terminal o el sistema si es necesario para que se reconozca la nueva variable de entorno.

## Instalación de Dependencias de Python

1. **Abrir la Terminal:**  
   Abre el Símbolo del sistema (CMD) o PowerShell.

2. **Instalar Dependencias:**  
   Ejecuta el siguiente comando para instalar los paquetes necesarios:

pip install yt-dlp ffmpeg-python

*Nota:* `tkinter` viene incluido en la mayoría de las instalaciones de Python, por lo que no es necesario instalarlo aparte.

## Ejecución de la Aplicación

1. **Ubicación del Código:**  
Asegúrate de que el código fuente se encuentre en el directorio `src/`.

2. **Ejecutar el Script:**  
Desde la terminal, navega hasta la carpeta `src/` y ejecuta el siguiente comando:

python youtube_mp3_downloader.py

Esto iniciará la interfaz gráfica de la aplicación, donde podrás ingresar el enlace del video de YouTube, seleccionar una carpeta de destino y descargar el audio en formato MP3.

## Solución de Problemas

- **ffmpeg no encontrado:**  
Verifica que la ruta `C:\ffmpeg\bin` esté correctamente agregada al `PATH`. Reinicia la terminal o el sistema si es necesario.

- **Errores con las dependencias:**  
Asegúrate de tener instalada la versión correcta de Python y que todos los paquetes se instalaron sin errores mediante `pip`.

- **Problemas durante la descarga:**  
Verifica que el enlace de YouTube sea válido y que tengas una conexión a Internet estable.

¡Con estos pasos, deberías tener tu entorno de desarrollo listo para ejecutar el "YouTube MP3 Downloader" en Windows!
