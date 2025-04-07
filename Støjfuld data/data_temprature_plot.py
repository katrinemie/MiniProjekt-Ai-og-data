import pandas as pd
import matplotlib.pyplot as plt
import os

# Definer stien til CSV-filen
file_path = r"C:\Users\katri\Documents\2 semester\Ai og data\MiniProjekt-Ai-og-data\MiniProjekt-Ai-og-data\Støjfuld data\DailyDelhiClimateTrain.csv"

# Tjek om filen findes
if os.path.exists(file_path):
    print("Filen findes! Læser data...")
    df = pd.read_csv(file_path)

    # Udskriv kolonnenavne for at finde de rigtige navne
    print("Kolonnenavne i filen:", df.columns)

    # Forsøg at finde kolonner, selv hvis de er skrevet anderledes
    date_col = None
    temp_col = None
    for col in df.columns:
        if "date" in col.lower():
            date_col = col
        if "temp" in col.lower():
            temp_col = col

    if not date_col or not temp_col:
        print("Fejl: DataFrame mangler en dato- eller temperatur-kolonne.")
    else:
        print(f"Bruger '{date_col}' som dato og '{temp_col}' som temperatur.")

        # Konverter dato til datetime-format
        df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

        # Fjern eventuelle rækker med manglende værdier i dato eller temperatur
        df = df.dropna(subset=[date_col, temp_col])

        # Brug dato som indeks
        df.set_index(date_col, inplace=True)

        #plot
        plt.figure(figsize=(12,6))
        plt.plot(df.index, df[temp_col], label="Temperatur", color="tab:blue")

        #Forbedret formatering
        plt.title("Temperatur over tid")
        plt.xlabel("Dato")
        plt.ylabel("Temperatur (°C)")
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True, linestyle="--", alpha=0.7)

        plt.show()
else:
    print("Filen findes IKKE! Tjek stien og prøv igen.")
