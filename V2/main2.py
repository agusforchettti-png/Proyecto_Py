import pandas as pd

def analizar_csv(nombre_archivo, ruta_archivo, umbral_potencia, umbral_snr, umbral_ber):
    print(f"Abriendo {nombre_archivo} desde {ruta_archivo}")
    df = pd.read_csv(ruta_archivo)

    # Lista de enlaces únicos para cargar el combo_enlace
    enlaces = sorted(df["enlace"].astype(str).unique().tolist())

    # Ejemplo de análisis contra los 3 umbrales
    problemas = []
    for enlace, grupo in df.groupby("enlace"):
        if (grupo["potencia"] < umbral_potencia).any():
            problemas.append(f"{enlace}: Potencia baja (< {umbral_potencia} dBm)")
        if (grupo["snr"] < umbral_snr).any():
            problemas.append(f"{enlace}: SNR bajo (< {umbral_snr} dB)")
        if (grupo["ber"] > umbral_ber).any():
            problemas.append(f"{enlace}: BER alta (> {umbral_ber})")

    return df, enlaces, problemas