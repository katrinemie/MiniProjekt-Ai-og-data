import pandas as pd

# 1. Indlæs datasættet
df = pd.read_csv(r"medical_students_dataset_cleaned.csv")

# 2. Data Imputing - Udfyld manglende værdier

# Numeriske kolonner → udfyld med median
for col in df.select_dtypes(include='number').columns:
    median = df[col].median()
    df[col] = df[col].fillna(median)

# Kategoriske kolonner → udfyld med mest almindelige værdi (mode)
for col in df.select_dtypes(include='object').columns:
    mode = df[col].mode()[0]
    df[col] = df[col].fillna(mode)

# 3. Gem det færdige datasæt
df.to_csv("medical_students_dataset_imputed.csv", index=False)
print("✅ Manglende værdier er udfyldt og datasættet er gemt.")
