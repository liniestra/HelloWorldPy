from PySide6.QtWidgets import QApplication, QLabel, QWidget
import sys

app = QApplication(sys.argv)

ventana = QWidget()
ventana.setWindowTitle("Mi App")
ventana.resize(400, 200)

label = QLabel("Hola desde PySide6", parent=ventana)
label.move(140, 80)

ventana.show()

app.exec()