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
        t_pot = self.ui.textEdit_4.toPlainText().strip()
        t_snr = self.ui.textEdit_5.toPlainText().strip()
        t_ber = self.ui.textEdit_3.toPlainText().strip()

        pot_valida = bool(t_pot)
        snr_valida = bool(t_snr)
        ber_valida = bool(t_ber)

        u_pot = float(t_pot) if pot_valida else None
        u_snr = float(t_snr) if snr_valida else None
        u_ber = float(t_ber) if ber_valida else None

        return u_pot, u_snr, u_ber, pot_valida, snr_valida, ber_valida

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

        u_pot, u_snr, u_ber, pot_valida, snr_valida, ber_valida = self.leer_umbrales()

        # Enviar nombre, ruta y los 3 umbrales a main2.py
        self.df, enlaces, problemas = main2.analizar_csv(
            self.nombre_csv, self.ruta_csv, u_pot, u_snr, u_ber,pot_valida,snr_valida,ber_valida,
        )

        # Cargar combo_enlace sin disparar doble actualización
        self.ui.combo_enlace.blockSignals(True)
        self.ui.combo_enlace.clear()
        self.ui.combo_enlace.addItems(enlaces)
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

        enlace = self.ui.combo_enlace.currentText()
        u_pot, u_snr, u_ber, pot_valida, snr_valida, ber_valida = self.leer_umbrales()
        self.graficador.graficar(self.df, enlace, u_pot, u_snr, u_ber,pot_valida,snr_valida,ber_valida)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())