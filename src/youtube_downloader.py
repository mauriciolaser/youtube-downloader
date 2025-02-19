import os
import platform
import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp
import ffmpeg


def detect_filesystem():
    """Detecta el sistema de archivos según el sistema operativo."""
    system = platform.system()
    if system == "Windows":
        return "NTFS (Windows)"
    elif system == "Darwin":
        return "APFS/HFS+ (MacOS)"
    elif system == "Linux":
        return "EXT4/XFS/BTRFS (Linux)"
    else:
        return "Sistema desconocido"


def download_audio():
    """Descarga el audio de un video de YouTube en formato MP3 usando yt-dlp."""
    url = entry.get()
    if not url:
        messagebox.showerror("Error", "Por favor, ingrese un enlace de YouTube.")
        return

    save_path = filedialog.askdirectory()
    if not save_path:
        messagebox.showerror("Error", "Debe seleccionar una carpeta de destino.")
        return

    try:
        output_path = os.path.join(save_path, "%(title)s.%(ext)s")
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Éxito", "Descarga completada.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")


# Interfaz gráfica
root = tk.Tk()
root.title("YouTube MP3 Downloader")
root.geometry("400x200")

tk.Label(root, text="Ingrese el enlace de YouTube:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

download_button = tk.Button(root, text="Descargar como MP3", command=download_audio)
download_button.pack(pady=10)

filesystem_label = tk.Label(root, text=f"Sistema de archivos: {detect_filesystem()}")
filesystem_label.pack(pady=5)

root.mainloop()
