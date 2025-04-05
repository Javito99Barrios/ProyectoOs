import psutil
import tkinter as tk
from tkinter import ttk
#importacion de biblioteca

def obtener_procesos():
    # Limpiar tabla
    for item in tree.get_children():
        tree.delete(item)

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            pid = proc.info['pid']
            nombre = proc.info['name']
            cpu = proc.info['cpu_percent']
            memoria = proc.info['memory_percent']
            tree.insert('', 'end', values=(pid, nombre, f"{cpu:.1f}%", f"{memoria:.1f}%"))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

# Crear ventana
ventana = tk.Tk()
ventana.title("Procesos Activos")
ventana.geometry("700x400")

# Tabla con encabezados
columnas = ('PID', 'Nombre', 'CPU (%)', 'Memoria (%)')
tree = ttk.Treeview(ventana, columns=columnas, show='headings')

for col in columnas:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(fill='both', expand=True)

# Botón para refrescar
boton_actualizar = tk.Button(ventana, text="Actualizar", command=obtener_procesos)
boton_actualizar.pack(pady=10)

# Mostrar procesos al iniciar
obtener_procesos()

ventana.mainloop()