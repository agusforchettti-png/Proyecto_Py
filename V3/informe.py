import pandas as pd

def analizar_csv(nombre_archivo, ruta_archivo, umbrales, validos):
    df = pd.read_csv(ruta_archivo)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    enlaces = sorted(df["enlace"].astype(str).unique().tolist())

    problemas = []
    for enlace, grupo in df.groupby("enlace"):
        min_pot = grupo["potencia_dbm"].min()
        max_pot = grupo["potencia_dbm"].max()
        min_snr = grupo["snr_db"].min()
        max_snr = grupo["snr_db"].max()
        min_ber = grupo["ber"].min()
        max_ber = grupo["ber"].max()

        if validos[0] and min_pot < umbrales[0]:
            problemas.append(f"{enlace}: Potencia baja ({min_pot:.1f} dBm)")
        if validos[1] and max_pot > umbrales[1]:
            problemas.append(f"{enlace}: Potencia alta ({max_pot:.1f} dBm)")
        if validos[2] and min_snr < umbrales[2]:
            problemas.append(f"{enlace}: SNR bajo ({min_snr:.1f} dB)")
        if validos[3] and max_snr > umbrales[3]:
            problemas.append(f"{enlace}: SNR alto ({max_snr:.1f} dB)")
        if validos[4] and min_ber < umbrales[4]:
            problemas.append(f"{enlace}: BER baja ({min_ber:.1e})")
        if validos[5] and max_ber > umbrales[5]:
            problemas.append(f"{enlace}: BER alta ({max_ber:.1e})")

    return df, enlaces, problemas