import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDialog, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Hoja de estilo global
    app.setStyleSheet("QDialog { background-color: black; }"
                      "QLabel { color: green; font: 12pt Arial; }"
                      "QLineEdit { background-color: gray; color: black; }"
                      "QPushButton { background-color: gray; color: black; }")

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Calculadora de perdida en operaciones")
            self.setGeometry(100, 100, 400, 200)

            self.label = QLabel(self)
            self.label.setFont(QFont("Arial", 12))
            self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.setCentralWidget(self.label)

            self.calcular_perdida()

        def calcular_perdida(self):
            dialog = PriceInputDialog(self)
            if dialog.exec_() == QDialog.Accepted:
                precio_entrada = dialog.get_precio_entrada()

                cantidad_contratos = 3
                costo_tick = 1.25
                tamanio_tick = 0.25

                distancia_segunda_orden = 40
                distancia_stop_loss = 60

                precio_segunda_orden = precio_entrada - (tamanio_tick * distancia_segunda_orden)
                precio_stop_loss = precio_entrada - (tamanio_tick * distancia_stop_loss)

                perdida_puntos = abs(precio_entrada - precio_stop_loss)
                perdida_usd = perdida_puntos * costo_tick * cantidad_contratos

                texto = f"El precio para la segunda orden es: {precio_segunda_orden}\n" \
                        f"El precio para el stop loss es: {precio_stop_loss}"
                self.label.setText(texto)


    class PriceInputDialog(QDialog):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setWindowTitle("Ingrese el precio de entrada")

            layout = QVBoxLayout(self)

            self.label = QLabel("Ingrese el precio de entrada:")
            layout.addWidget(self.label)

            self.input_field = QLineEdit()
            layout.addWidget(self.input_field)

            self.button = QPushButton("Aceptar")
            self.button.clicked.connect(self.accept)
            layout.addWidget(self.button)

        def get_precio_entrada(self):
            return float(self.input_field.text())

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())





