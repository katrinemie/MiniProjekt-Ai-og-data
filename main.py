import pandas as pd

# Begge filer indlæses
cleaned = pd.read_csv("medical_students_dataset_cleaned.csv")
imputed = pd.read_csv("medical_students_dataset_imputed.csv")

# Print antal rækker og kolonner - For at se forskellen på datamængden
print(f"Cleaned datasæt: {cleaned.shape}")
print(f"Imputed datasæt: {imputed.shape}")

