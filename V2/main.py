import os
import sys
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow
from FrontEndPrograma import Ui_MainWindow  # Verificá que coincida con tu .py generado
import main2
from graficador import GraficadorEnlaces

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ruta_csv = None
        self.nombre_csv = None
        self.df = None

        # Inicializar las 3 gráficas en los QWidget del .ui
        self.graficador = GraficadorEnlaces(
            self.ui.widget,
            self.ui.widget_3,
            self.ui.widget_4
        )

        # Conectar menú, botón ACTUALIZAR y selector de enlace
        self.ui.actionAbrir_CSV.triggered.connect(self.abrir_csv)
        self.ui.actionCerrar.triggered.connect(self.close)
        self.ui.pushbutton_actualizar.clicked.connect(self.ejecutar_analisis)
        self.ui.combo_enlace.currentTextChanged.connect(self.actualizar_graficas)

    def leer_umbrales(self):
        def a_float(widget, defecto):
            texto = widget.toPlainText().strip()
            return float(texto) if texto else defecto

        u_pot = a_float(self.ui.textEdit_4, -80.0)
        u_snr = a_float(self.ui.textEdit_5, 10.0)
        u_ber = a_float(self.ui.textEdit_3, 1e-4)
        return u_pot, u_snr, u_ber

    def abrir_csv(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Abrir archivo CSV",
            "",
            "Archivos CSV (*.csv);;Todos los archivos (*)"
        )
        if not ruta:
            return

        self.ruta_csv = ruta
        self.nombre_csv = os.path.basename(ruta)
        self.ejecutar_analisis()

    def ejecutar_analisis(self):
        if not self.ruta_csv:
            self.ui.statusbar.showMessage("Primero abrí un archivo CSV desde Archivo -> Abrir CSV")
            return

        u_pot, u_snr, u_ber = self.leer_umbrales()

        # Enviar nombre, ruta y los 3 umbrales a main2.py
        self.df, enlaces, problemas = main2.analizar_csv(
            self.nombre_csv, self.ruta_csv, u_pot, u_snr, u_ber
        )

        # Cargar combo_enlace sin disparar doble actualización
        self.ui.combo_enlace.blockSignals(True)
        self.ui.combo_enlace.clear()
        self.ui.combo_enlace.addItems(enlaces)
        self.ui.combo_enlace.blockSignals(False)

        self.ui.statusbar.showMessage(
            f"Análisis completo ({self.nombre_csv}): {len(enlaces)} enlaces | {len(problemas)} alertas"
        )
        self.actualizar_graficas()

    def actualizar_graficas(self):
        if self.df is None or self.ui.combo_enlace.count() == 0:
            return

        enlace = self.ui.combo_enlace.currentText()
        u_pot, u_snr, u_ber = self.leer_umbrales()
        self.graficador.graficar(self.df, enlace, u_pot, u_snr, u_ber)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())