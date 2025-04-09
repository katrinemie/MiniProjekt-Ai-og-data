import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


filnavn = r"Støjfuld data\DailyDelhiClimateTrain.csv"
df = pd.read_csv(filnavn, parse_dates=['date'])


temperature = df['meantemp']

#FFT
fft_values = np.fft.fft(temperature)
frequencies = np.fft.fftfreq(len(temperature))

fft_filtered = fft_values.copy()
threshold = 0.005  #Lavere threshold 
fft_filtered[np.abs(frequencies) > threshold] = 0

filtered_temp_fft = np.fft.ifft(fft_filtered).real


window_size = 30  
moving_avg = temperature.rolling(window=window_size, center=True).mean()

#Plot FFT vs Moving Average
plt.figure(figsize=(18, 7))
plt.plot(df['date'], filtered_temp_fft, label=f'Filteret temperatur (FFT, threshold={threshold})', color='green')
plt.plot(df['date'], moving_avg, label=f'Moving average (vindue={window_size})', color='orange')
plt.xlabel('Dato')
plt.ylabel('Temperatur (°C)')
plt.title('Sammenligning: FFT vs. Moving Average')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
