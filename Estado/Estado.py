import tkinter as tk
from tkinter import ttk
import psutil

def check_application_status(application_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == application_name:
            return "En ejecución"
    return "Desconectada"

def update_table():
    for item in table.get_children():
        app_name = table.item(item)['values'][0]
        status_value = check_application_status(app_name)
        table.item(item, values=(app_name, status_value))
        if status_value == "En ejecución":
            table.item(item, tags=('running',))
        else:
            table.item(item, tags=('disconnected',))
    root.after(1000, update_table)

def add_application():
    new_app_name = app_name_entry.get()
    application_list.append((new_app_name, ""))  # Agregar una tupla
    table.insert("", "end", values=(new_app_name, ""))
    app_name_entry.delete(0, tk.END)

# Crear ventana
root = tk.Tk()
root.title("Estado de Aplicaciones")

# Crear tabla
application_list = []  # Lista de aplicaciones
table = ttk.Treeview(root, columns=("Aplicación", "Estado"), show="headings")
table.heading("Aplicación", text="Aplicación")
table.heading("Estado", text="Estado")
table.pack()

# Crear campo de entrada y botón para agregar aplicaciones
app_name_label = tk.Label(root, text="Nombre de la Aplicación:")
app_name_label.pack(pady=5)
app_name_entry = tk.Entry(root)
app_name_entry.pack(pady=5)

add_button = tk.Button(root, text="Agregar Aplicación", command=add_application)
add_button.pack(pady=5)

# Configurar estilos para la visualización de estados
table.tag_configure('running', foreground='green')
table.tag_configure('disconnected', foreground='red')

# Actualizar estado constantemente
update_table()

# Ejecutar la interfaz
root.mainloop()
