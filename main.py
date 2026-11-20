import csv
import os
import sys
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow
from FrontEndPrograma import Ui_MainWindow  # Cambiá por el nombre de tu archivo generado

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ruta_csv = None  # Para guardar la ruta del archivo cargado

        # Conectar las acciones del menú Archivo
        self.ui.actionAbrir_CSV.triggered.connect(self.abrir_csv)
        self.ui.actionCerrar.triggered.connect(self.close)

    def abrir_csv(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Abrir archivo CSV",
            "",
            "Archivos CSV (*.csv);;Todos los archivos (*)"
        )

        # Si el usuario cancela, ruta viene vacío
        if not ruta:
            return

        self.ruta_csv = ruta
        nombre_archivo = os.path.basename(ruta)

        # Mostrar el nombre en tu barra de estado (statusbar)
        self.ui.statusbar.showMessage(f"Archivo cargado: {nombre_archivo}")

        # (Opcional) Si tenés un QLabel o QLineEdit para mostrar el nombre del archivo:
        # self.ui.label_archivo.setText(nombre_archivo)

        # Leer el contenido del CSV
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)  # o csv.reader(archivo)
            filas = list(lector)
            print(f"Se leyeron {len(filas)} filas de {nombre_archivo}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())