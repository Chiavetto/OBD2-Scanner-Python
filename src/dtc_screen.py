import tkinter as tk
from tkinter import messagebox
import threading
from obd_connection import enviar_comando


def mostrar_diagnostico(parent):
    diag = tk.Toplevel(parent)
    diag.title("Códigos de falla")

    resultado = tk.Text(diag, width=50, height=10)
    resultado.pack(padx=10, pady=10)

    def ejecutar():
        def tarea():
            r = enviar_comando("03")  # Leer códigos de falla
            diag.after(0, lambda: resultado.insert(tk.END, r))
        threading.Thread(target=tarea).start()

    def borrar():
        if messagebox.askyesno("Advertencia", "Esto borrará los códigos de error. ¿Deseás continuar?"):
            def tarea():
                r = enviar_comando("04")  # Borrar códigos
                diag.after(0, lambda: messagebox.showinfo("Resultado", r))
            threading.Thread(target=tarea).start()

    tk.Button(diag, text="Leer códigos", command=ejecutar).pack(pady=5)
    tk.Button(diag, text="Borrar códigos", command=borrar).pack(pady=5)
    tk.Button(diag, text="Atrás", command=diag.destroy).pack(pady=5)
