import pandas as pd
import matplotlib.pyplot as plt


filnavn = r"Støjfuld data\DailyDelhiClimateTrain.csv"
df = pd.read_csv(filnavn, parse_dates=["date"])

#7 dages vindue
df["glidende_gns"] = df["meantemp"].rolling(window=7).mean()

#Plot :)
plt.figure(figsize=(15, 6))
plt.plot(df["date"], df["meantemp"], label="Original temperatur", alpha=0.5)
plt.plot(df["date"], df["glidende_gns"], label="Glidende gennemsnit (7 dage)", color="red")
plt.title("Temperatur over tid - med glidende gennemsnit")
plt.xlabel("Dato")
plt.ylabel("Temperatur (°C)")
plt.legend()
plt.tight_layout()
plt.savefig("temperatur_glidende_gns.png")
plt.show()
