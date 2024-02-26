import tkinter as tk
from tkinter import ttk
import psutil

def check_application_status(application_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == application_name:
            return "En ejecucion"
    return "Desconectada"

def update_table():
    for item in table.get_children():
        app_name = table.item(item)['values'][0]
        status_value = check_application_status(app_name)
        table.item(item, values=(app_name, status_value))
        #Consulta el estado de la aplicacion
        if status_value == "En ejecucion":
            table.item(item, tags=('running',))
        else:
            table.item(item, tags=('disconnected',))
    root.after(1000, update_table)

def add_application():
    new_app_name = app_name_entry.get()
    application_list.append((new_app_name, ""))  
    table.insert("", "end", values=(new_app_name, ""))
    app_name_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Estado de Aplicaciones")

application_list = []  #Lista de aplicaciones
table = ttk.Treeview(root, columns=("Aplicacion", "Estado"), show="headings")
table.heading("Aplicacion", text="Aplicacion")
table.heading("Estado", text="Estado")
table.pack()


app_name_label = tk.Label(root, text="Nombre de la Aplicacion:")
app_name_label.pack(pady=5)
app_name_entry = tk.Entry(root)
app_name_entry.pack(pady=5)

add_button = tk.Button(root, text="Agregar Aplicacion", command=add_application)
add_button.pack(pady=5)

table.tag_configure('running', foreground='green')
table.tag_configure('disconnected', foreground='red')

# Actualizar estado constantemente
update_table()

root.mainloop()
