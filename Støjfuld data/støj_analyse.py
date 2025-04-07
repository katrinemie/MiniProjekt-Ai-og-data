import pandas as pd
import matplotlib.pyplot as plt

# Indlæs data
filnavn = r"Støjfuld data\DailyDelhiClimateTrain.csv"
  # Opdater med den korrekte sti
df = pd.read_csv(filnavn, parse_dates=["date"])

# Udskriv kolonnenavne for at dobbelttjekke
print("Kolonner i datasættet:", df.columns)

# Omdøb kolonner hvis nødvendigt
if "meantemp" in df.columns:
    df = df.rename(columns={"meantemp": "temperature"})

# Beregn standardafvigelsen
std_dev = df["temperature"].std()
print(f"Standardafvigelse: {std_dev:.2f}")

# Plot histogram for at vurdere støjen
plt.figure(figsize=(8, 5))
df["temperature"].hist(bins=50, color="blue", alpha=0.7)
plt.title("Histogram over temperaturer")
plt.xlabel("Temperatur (°C)")
plt.ylabel("Antal målinger")
plt.grid(True)

# Gem figuren i stedet for at vise den
plt.savefig("støj_analyse.png")
print("Plot gemt som 'støj_analyse.png'")
