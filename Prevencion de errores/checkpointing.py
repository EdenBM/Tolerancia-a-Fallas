import pickle

def guardar_estado(nombre_archivo, datos):
    with open(nombre_archivo, 'wb') as archivo:
        pickle.dump(datos, archivo)

def cargar_estado(nombre_archivo):
    with open(nombre_archivo, 'rb') as archivo:
        return pickle.load(archivo)

def funcion_principal():
    checkpoint_archivo = 'checkpoint.pkl'
    intentos_maximos = 12
    intentos = 0

    while intentos < intentos_maximos:
        try:
            #Simular error
            raise Exception("Error simulado")

        except Exception as e:
            print(f"Se produjo un error: {e}")
            print("Guardando estado y reiniciando...")
            guardar_estado(checkpoint_archivo, (intentos + 1))
            intentos = cargar_estado(checkpoint_archivo)
            print(f"Reiniciando desde el intento {intentos + 1}")

def main():
    funcion_principal()

if __name__ == "__main__":
    main()
