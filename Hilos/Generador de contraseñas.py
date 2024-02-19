import multiprocessing
import threading
import random
import string
import tkinter as tk
import queue


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_passwords(num_passwords, length, output_queue):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    output_queue.put(passwords)


def on_generate_click():
    num_passwords = int(entry.get())
    length = 12  #Longitud
    output_queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=generate_passwords, args=(num_passwords, length, output_queue))
    process.start()
    process.join()  #Espera que los procesos terminen
    passwords = output_queue.get()
    for password in passwords:
        text_box.insert(tk.END, f"{password}\n")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Password Generator")

    label = tk.Label(root, text="Cuantas contraseñas deseas generar?:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    generate_button = tk.Button(root, text="Generar", command=on_generate_click)
    generate_button.pack()

    text_box = tk.Text(root, height=10, width=40)
    text_box.pack()

    root.mainloop()
