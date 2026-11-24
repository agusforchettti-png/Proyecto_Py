# pylint: disable=no-member
import os
import sys
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow
from FrontEndPrograma import Ui_MainWindow
import main2
from graficador import GraficadorEnlaces


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        """
        Inicializa el FrontEnd mediante Pyside y establece los valores por defecto de variables
        """
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
        widgets = [
            self.ui.Umbral_pot_min,
            self.ui.Umbral_pot_max,
            self.ui.Umbral_snr_min,
            self.ui.Umbral_snr_max,
            self.ui.Umbral_ber_min,
            self.ui.Umbral_ber_max,
        ]

        umbrales = []
        validos = []

        for w in widgets:
            texto = w.toPlainText().strip()
            if texto:
                umbrales.append(float(texto))
                validos.append(True)
            else:
                umbrales.append(None)
                validos.append(False)

        return umbrales, validos
    
    def abrir_csv(self):
        """
        Abre el Archivo .csv al desplegar una ventana de busqueda para archivos
        facilitando la busqueda ya que el usuario no debe ingresar la ruta del archivo
        """
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
        self.ui.label_nombre_archivo.setText(self.nombre_csv)
        self.ejecutar_analisis()

    def ejecutar_analisis(self):
        """
        Analiza los datos del archivo seleccionado y de no haber un 
        archivo CSV seleccionado muestra un aviso
        """
        if not self.ruta_csv:
            self.ui.statusbar.showMessage("Primero abrí un archivo CSV desde Archivo -> Abrir CSV")
            return

        umbrales, validos = self.leer_umbrales()
        self.df, enlaces, problemas = main2.analizar_csv(
            self.nombre_csv, self.ruta_csv, umbrales, validos
        )

        # Cargar combo_enlace sin disparar doble actualización
        self.ui.combo_enlace.blockSignals(True)
        self.ui.combo_enlace.clear()
        for enlace in enlaces:
            num = int(enlace[1:]) if enlace[1:].isdigit() else enlace
            texto = f"{enlace} - Enlace {num}"   # Ej: "E01 - Enlace 1"
            # Si preferís "EN1 - Enlace 1", usá: texto = f"EN{num} - Enlace {num}"
            self.ui.combo_enlace.addItem(texto, enlace)  # Muestra texto, guarda "E01"
        self.ui.combo_enlace.blockSignals(False)

        # Cargar el reporte en el cuadro INFORME con viñetas
        if problemas:
            items_html = "".join(f"<li>{p}</li>" for p in problemas)
            html = f"""
            <div style="font-size: 14px;">
                <p style="margin:0 0 4px 0;"><b>Enlaces con problemas</b></p>
                <ul style="margin:0; padding-left:18px;">
                    {items_html}
                </ul>
            </div>
            """
        else:
            html = '<div style="font-size: 14px;"><b>Sin problemas detectados</b><br>Todos los enlaces cumplen los umbrales.</div>'

        self.ui.textEdit_informe.setHtml(html)

        self.ui.statusbar.showMessage(
            f"Análisis completo ({self.nombre_csv}): {len(enlaces)} enlaces procesados | {len(problemas)} alertas"
        )
        self.actualizar_graficas()

    def actualizar_graficas(self):
        """
        Ajusta los valores de las 3 graficas del proyecto mostrando el 
        cambio de las 3 dichas variables del archivo respecto al tiempo en el
        que se tomaron
        """
        if self.df is None or self.ui.combo_enlace.count() == 0:
            return

        enlace = self.ui.combo_enlace.currentData()
        umbrales, validos = self.leer_umbrales()
        self.graficador.graficar(self.df, enlace,umbrales, validos)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())