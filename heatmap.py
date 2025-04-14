import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("medical_students_dataset.csv")

#Print hvor der mangler data
print(" Manglende værdier pr. kolonne:")
print(df.isnull().sum())

#Vis heatmap der giver et overblik over, hvor der mangler data
plt.figure(figsize=(12, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
plt.title("Heatmap over manglende værdier i datasættet")
plt.xlabel("Kolonner")
plt.ylabel("Rækker")
plt.tight_layout()
plt.show()