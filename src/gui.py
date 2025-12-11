import tkinter as tk
from tkinter import messagebox
import threading
from obd_connection import conectar_elm327, puerto
from dtc_screen import mostrar_diagnostico
from sensors_screen import mostrar_sensores


def mostrar_opciones(root):
    win = tk.Toplevel(root)
    win.title("Opciones de Diagnóstico")

    tk.Button(win, text="Diagnóstico", width=20,
              command=lambda: mostrar_diagnostico(root)).pack(pady=10)

    tk.Button(win, text="Sensores en tiempo real", width=20,
              command=lambda: mostrar_sensores(root)).pack(pady=10)


def run_gui():
    root = tk.Tk()
    root.title("Diagnóstico OBD2")
    root.geometry("400x300")

    def buscar():
        def tarea():
            from obd_connection import puerto as p
            p = conectar_elm327()
            if p:
                messagebox.showinfo("Dispositivo", "Dispositivo OBD2 encontrado")
                mostrar_opciones(root)
            else:
                messagebox.showerror("Error", "No se pudo encontrar el dispositivo")
        threading.Thread(target=tarea).start()

    tk.Button(root, text="Encontrar dispositivo", command=buscar).pack(pady=20)

    root.mainloop()
