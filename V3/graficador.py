from PySide6.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates


class GraficadorEnlaces:
    def __init__(self, cont_potencia, cont_snr, cont_ber):
        self.ax_pot, self.canvas_pot = self._crear_canvas(cont_potencia)
        self.ax_snr, self.canvas_snr = self._crear_canvas(cont_snr)
        self.ax_ber, self.canvas_ber = self._crear_canvas(cont_ber)
        self.canvas_pot.setVisible(False)
        self.canvas_snr.setVisible(False)
        self.canvas_ber.setVisible(False)

    def _crear_canvas(self, contenedor):
        if contenedor.layout() is None:
            layout = QVBoxLayout(contenedor)
            layout.setContentsMargins(0, 0, 0, 0)

        figura = Figure(figsize=(5, 2.2), dpi=100)
        canvas = FigureCanvas(figura)
        ax = figura.add_subplot(111)
        contenedor.layout().addWidget(canvas)
        return ax, canvas

    def _estilizar_eje(self, ax, canvas, ylabel, escala_log=False, labelsize_y=7):
        """
        Define como va a ser el aspecto de los ejes de las 3 graficas
        """
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d - %H:%M"))
        ax.xaxis.set_major_locator(
            mdates.HourLocator(interval=12)
        )  # Una marca cada 12 hs para que no se encimen
        if escala_log:
            ax.set_yscale("log")
        ax.set_ylabel(ylabel, fontsize=8)
        ax.tick_params(axis="both", labelsize=7)  # Achica números de X e Y
        ax.tick_params(axis="y", which="both", labelsize=labelsize_y)
        ax.margins(x=0)  # Sin espacios vacíos a los lados
        ax.grid(True, linestyle=":", alpha=0.5)
        ax.legend(loc="lower left", fontsize=7)
        canvas.figure.tight_layout(
            pad=0.3
        )  # Reduce bordes externos para agrandar el cuadro
        canvas.draw()

    def graficar(self, df, enlace, umbrales, validos):
        """
        Define el aspecto de las tres graficas y sus umbrales
        """
        datos = df[df["enlace"].astype(str) == str(enlace)]
        if datos.empty:
            return
        self.canvas_pot.setVisible(True)
        self.canvas_snr.setVisible(True)
        self.canvas_ber.setVisible(True)
        x = datos["timestamp"]

        # 1. Gráfica de Potencia
        self.ax_pot.clear()
        self.ax_pot.plot(
            x,
            datos["potencia_dbm"],
            color="#1e3a8a",
            linewidth=1.3,
            label="Potencia (RSSI)",
        )
        if validos[0]:
            self.ax_pot.axhline(
                umbrales[0], color="red", linestyle="--", linewidth=1, label="Umbral"
            )
        if validos[1]:
            self.ax_pot.axhline(
                umbrales[1], color="red", linestyle="--", linewidth=1, label="Umbral"
            )
        self._estilizar_eje(self.ax_pot, self.canvas_pot, "dBm")

        # 2. Gráfica de SNR
        self.ax_snr.clear()
        self.ax_snr.plot(
            x, datos["snr_db"], color="#3b82f6", linewidth=1.3, label="SNR"
        )
        if validos[2]:
            self.ax_snr.axhline(
                umbrales[2], color="red", linestyle="--", linewidth=1, label="Umbral"
            )
        if validos[3]:
            self.ax_snr.axhline(
                umbrales[3], color="red", linestyle="--", linewidth=1, label="Umbral"
            )
        self._estilizar_eje(self.ax_snr, self.canvas_snr, "dB")

        # 3. Gráfica de BER
        self.ax_ber.clear()
        self.ax_ber.plot(x, datos["ber"], color="#9333ea", linewidth=1.3, label="BER")
        if validos[4]:
            self.ax_ber.axhline(
                umbrales[4], color="red", linestyle="--", linewidth=1, label="Umbral"
            )
        if validos[5]:
            self.ax_ber.axhline(
                umbrales[5], color="red", linestyle="--", linewidth=1, label="Umbral"
            )
        self._estilizar_eje(
            self.ax_ber, self.canvas_ber, "BER", escala_log=True, labelsize_y=6
        )
