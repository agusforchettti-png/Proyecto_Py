from PySide6.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class GraficadorEnlaces:
    def __init__(self, cont_potencia, cont_snr, cont_ber):
        self.ax_pot, self.canvas_pot = self._crear_canvas(cont_potencia)
        self.ax_snr, self.canvas_snr = self._crear_canvas(cont_snr)
        self.ax_ber, self.canvas_ber = self._crear_canvas(cont_ber)

    def _crear_canvas(self, contenedor):
        # Si el QWidget del .ui no tiene layout asignado, se lo creamos acá
        if contenedor.layout() is None:
            layout = QVBoxLayout(contenedor)
            layout.setContentsMargins(0, 0, 0, 0)

        figura = Figure(figsize=(5, 2.2), dpi=100)
        canvas = FigureCanvas(figura)
        ax = figura.add_subplot(111)
        contenedor.layout().addWidget(canvas)
        return ax, canvas

    def graficar(self, df, enlace, umbral_potencia, umbral_snr, umbral_ber):
        datos = df[df["enlace"].astype(str) == str(enlace)]
        if datos.empty:
            return

        x = range(len(datos))

        # 1. Gráfica de Potencia
        self.ax_pot.clear()
        self.ax_pot.plot(x, datos["potencia"], color="#1e3a8a", label="Potencia (RSSI)")
        self.ax_pot.axhline(umbral_potencia, color="gray", linestyle="--", label="Umbral")
        self.ax_pot.set_ylabel("dBm")
        self.ax_pot.legend(loc="lower left", fontsize=8)
        self.canvas_pot.figure.tight_layout()
        self.canvas_pot.draw()

        # 2. Gráfica de SNR
        self.ax_snr.clear()
        self.ax_snr.plot(x, datos["snr"], color="#3b82f6", label="SNR")
        self.ax_snr.axhline(umbral_snr, color="gray", linestyle="--", label="Umbral")
        self.ax_snr.set_ylabel("dB")
        self.ax_snr.legend(loc="lower left", fontsize=8)
        self.canvas_snr.figure.tight_layout()
        self.canvas_snr.draw()

        # 3. Gráfica de BER (escala logarítmica)
        self.ax_ber.clear()
        self.ax_ber.plot(x, datos["ber"], color="#9333ea", label="BER")
        self.ax_ber.axhline(umbral_ber, color="gray", linestyle="--", label="Umbral")
        self.ax_ber.set_yscale("log")
        self.ax_ber.set_ylabel("BER")
        self.ax_ber.legend(loc="lower left", fontsize=8)
        self.canvas_ber.figure.tight_layout()
        self.canvas_ber.draw()