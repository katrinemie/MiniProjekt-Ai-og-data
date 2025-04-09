import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Indlæs datasættet fra den angivne sti
filnavn = r"Støjfuld data\DailyDelhiClimateTrain.csv"
df = pd.read_csv(filnavn)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Vælg temperaturkolonnen
temp = df['meantemp'].values
n = len(temp)

# Udfør FFT
fft_temp = np.fft.fft(temp)
frequencies = np.fft.fftfreq(n)

# Lav en kopi til filtrering
filtered_fft = fft_temp.copy()

# Nulstil højfrekvent støj – fx behold kun de 5% laveste frekvenser
cutoff = int(n * 0.05)
filtered_fft[cutoff:-cutoff] = 0

# Invers FFT for at genskabe signal
filtered_temp = np.fft.ifft(filtered_fft).real

# Plot original og filtreret temperatur
plt.figure(figsize=(14, 6))
plt.plot(df.index, temp, label='Original temperatur', alpha=0.5)
plt.plot(df.index, filtered_temp, label='Filtreret temperatur (FFT)', color='green')
plt.xlabel('Dato')
plt.ylabel('Temperatur (°C)')
plt.title('Temperatur over tid - med frekvensbaseret filtrering (FFT)')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('fft_filter_resultat.png')
plt.show()
