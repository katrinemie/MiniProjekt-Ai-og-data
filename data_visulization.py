import pandas as pd
import matplotlib.pyplot as plt

# === Filsti til CSV ===
input_file = "medical_students_dataset.csv"  # Husk at placere CSV-filen i samme mappe som din .py fil

# === Indlæs datasæt ===
df = pd.read_csv(input_file)

# === Simpel visualisering: Histogram over højde og vægt ===
plt.figure(figsize=(12, 5))

# Histogram over højde
plt.subplot(1, 2, 1)
plt.hist(df['Height'].dropna(), bins=10, color='skyblue', edgecolor='black')
plt.title('Fordeling af højde')
plt.xlabel('Højde (cm)')
plt.ylabel('Antal studerende')

# Histogram over vægt
plt.subplot(1, 2, 2)
plt.hist(df['Weight'].dropna(), bins=10, color='lightgreen', edgecolor='black')
plt.title('Fordeling af vægt')
plt.xlabel('Vægt (kg)')
plt.ylabel('Antal studerende')

plt.tight_layout()
plt.show()

