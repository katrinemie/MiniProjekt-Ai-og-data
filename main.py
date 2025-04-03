import pandas as pd

# Læs begge filer ind
cleaned = pd.read_csv("medical_students_dataset_cleaned.csv")
imputed = pd.read_csv("medical_students_dataset_imputed.csv")

# Print antal rækker og kolonner
print(f"Cleaned datasæt: {cleaned.shape}")
print(f"Imputed datasæt: {imputed.shape}")

