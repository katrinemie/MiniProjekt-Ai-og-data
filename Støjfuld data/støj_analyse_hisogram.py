import pandas as pd
import matplotlib.pyplot as plt


filnavn = r"Støjfuld data\DailyDelhiClimateTrain.csv"

df = pd.read_csv(filnavn, parse_dates=["date"])


print("Kolonner i datasættet:", df.columns)


if "meantemp" in df.columns:
    df = df.rename(columns={"meantemp": "temperature"})

#standardafvigelseen 
std_dev = df["temperature"].std()
print(f"Standardafvigelse: {std_dev:.2f}")

#Plottet til histogrammet
plt.figure(figsize=(8, 5))
df["temperature"].hist(bins=50, color="blue", alpha=0.7)
plt.title("Histogram over temperaturer")
plt.xlabel("Temperatur (°C)")
plt.ylabel("Antal målinger")
plt.grid(True)


plt.savefig("støj_analyse.png")
print("Plot gemt som 'støj_analyse.png'")
