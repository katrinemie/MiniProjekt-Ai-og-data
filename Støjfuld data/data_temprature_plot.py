import pandas as pd
import matplotlib.pyplot as plt
import os


file_path = r"Støjfuld data\DailyDelhiClimateTrain.csv"


if os.path.exists(file_path):
    print("YAY. Filen findes")
    df = pd.read_csv(file_path)

    
    print("Kolonnenavne i filen:", df.columns)

    
    date_col = None
    temp_col = None
    for col in df.columns:
        if "date" in col.lower():
            date_col = col
        if "temp" in col.lower():
            temp_col = col

    if not date_col or not temp_col:
        print("feeeejl, dataFrame mangler en dato  eller temperatur kolonne.")
    else:
        print(f"Bruger '{date_col}' som dato og '{temp_col}' som temperatur.")

        #dato til datetime format
        df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

        
        df = df.dropna(subset=[date_col, temp_col])

        
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
    print("Filen findes ikke. øv øv")
