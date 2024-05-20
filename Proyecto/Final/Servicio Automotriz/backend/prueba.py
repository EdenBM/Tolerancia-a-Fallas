from PySide2.QtCore import QObject, Signal
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget


class ClaseCliente(QObject):
    valor_changed = Signal(int)  # Señal para indicar que el valor ha cambiado

    def __init__(self):
        super().__init__()
        self._valor = 0

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, nuevo_valor):
        self._valor = nuevo_valor
        # Emitir la señal cuando el valor cambia
        self.valor_changed.emit(self._valor)


class ClaseA(QWidget):
    def __init__(self, cliente):
        super().__init__()
        self.cliente = cliente
        self.btn = QPushButton("Cambiar Valor")
        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        self.setLayout(layout)

        self.btn.clicked.connect(self.cambiar_valor)

    def cambiar_valor(self):
        self.cliente.valor = 42  # Cambiar el valor del cliente


class ClaseB(QWidget):
    def __init__(self, cliente):
        super().__init__()
        self.cliente = cliente
        self.cliente.valor_changed.connect(self.on_valor_changed)

    def on_valor_changed(self, nuevo_valor):
        # Código que se ejecuta cuando el valor del cliente cambia
        print("El valor del cliente ha cambiado:", nuevo_valor)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.cliente = ClaseCliente()

        self.widget_a = ClaseA(self.cliente)
        self.widget_b = ClaseB(self.cliente)

        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.widget_a)
        layout.addWidget(self.widget_b)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle("Ejemplo")
        self.setGeometry(200, 200, 400, 300)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
