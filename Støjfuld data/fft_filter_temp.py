import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


filnavn = r"Støjfuld data\DailyDelhiClimateTrain.csv"
df = pd.read_csv(filnavn)


df["date"] = pd.to_datetime(df["date"]) 
df.set_index("date", inplace=True)


temp = df["meantemp"].values
n = len(temp)

#FFT :)
fft_temp = np.fft.fft(temp)
frequencies = np.fft.fftfreq(n)

#Filtering
filtered_fft = fft_temp.copy()
cutoff = int(n * 0.05)  
filtered_fft[cutoff:-cutoff] = 0


filtered_temp = np.fft.ifft(filtered_fft).real

#Plotteet
plt.figure(figsize=(14, 6))
plt.plot(df.index, temp, label="Original temperatur", color="tab:blue", alpha=0.5)
plt.plot(df.index, filtered_temp, label="Filtreret temperatur (FFT)", color="green")
plt.xlabel("Dato")
plt.ylabel("Temperatur (°C)")
plt.title("Temperatur over tid, med frekvensbaseret filtrering :)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("fft_filter_resultat.png")
plt.show()
