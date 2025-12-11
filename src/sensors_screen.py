import tkinter as tk
import threading
from obd_connection import enviar_comando


def mostrar_sensores(parent):
    win = tk.Toplevel(parent)
    win.title("Sensores en Tiempo Real")

    text = tk.Text(win, width=50, height=10)
    text.pack(padx=10, pady=10)

    def leer():
        def tarea():
            comandos = ["010C", "010D"]  # RPM y velocidad (PID comunes)
            r = ""
            for cmd in comandos:
                resp = enviar_comando(cmd)
                r += f"Comando {cmd}: {resp}\n"
            win.after(0, lambda: text.insert(tk.END, r))
        threading.Thread(target=tarea).start()

    tk.Button(win, text="Leer Sensores", command=leer).pack(pady=5)
    tk.Button(win, text="Atrás", command=win.destroy).pack(pady=5)
