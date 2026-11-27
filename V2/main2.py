import pandas as pd

def analizar_csv(nombre_archivo, ruta_archivo, umbral_potencia, umbral_snr, umbral_ber,pot_valida,snr_valida,ber_valida):
    df = pd.read_csv(ruta_archivo)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    enlaces = sorted(df["enlace"].astype(str).unique().tolist())

    problemas = []     
    for enlace, grupo in df.groupby("enlace"):
        min_pot = grupo["potencia_dbm"].min()
        min_snr = grupo["snr_db"].min()
        max_ber = grupo["ber"].max()

        if pot_valida and min_pot < umbral_potencia:
            problemas.append(f"{enlace}: Potencia baja ({min_pot:.1f} dBm)")
        if snr_valida and min_snr < umbral_snr:
            problemas.append(f"{enlace}: SNR bajo ({min_snr:.1f} dB)")
        if ber_valida and max_ber > umbral_ber:
            problemas.append(f"{enlace}: BER alta ({max_ber:.1e})")

    return df, enlaces, problemas