#include <iostream>
#include <stdexcept>
#include <limits>

using namespace std;

int main() {
    while (true) {
        cout<<"Menu:\n";
        cout<<"1. Suma\n";
        cout<<"2. Salir\n";

        int opcion;
        cout<<"Seleccione una opcion: ";

        try {
            cin>>opcion;
            // Verifica si la lectura fue exitosa
            if (cin.fail()) {
                throw runtime_error("Error: Ingrese un numero valido.");
            }

            switch (opcion) {
                case 1: {
                    double num1, num2;
                    cout<<"Ingrese el primer numero: ";
                    cin>>num1;
                    // Verifica si la lectura fue exitosa
                    if (cin.fail()) {
                        throw runtime_error("Error: Ingrese un numero valido.");
                    }

                    cout<<"Ingrese el segundo numero: ";
                    cin>>num2;
                    // Verifica si la lectura fue exitosa
                    if (cin.fail()) {
                        throw runtime_error("Error: Ingrese un numero valido.");
                    }

                    cout<<"La suma es: "<<num1 + num2<<endl;
                    break;
                }
                case 2:
                    cout<<"Saliendo del programa.\n";
                    return 0;
                default:
                    throw runtime_error("Error: Opcion no valida. Intente de nuevo.");
            }
        } catch (const runtime_error& e) {
            // Captura y muestra el mensaje de error
            cerr<<e.what()<< endl;
            // Limpiar el estado de error del cin
            cin.clear();
            // Ignorar el resto de la entrada hasta la nueva linea
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
    }

    return 0;
}
