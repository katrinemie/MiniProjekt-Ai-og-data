import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("medical_students_dataset_cleaned.csv")

#Tag et udsnit af data (10%) for at gøre det hurtigere
df = df.sample(frac=0.1, random_state=42)



#median til kolonner med skæv fordeling
for col in ['age', 'bmi', 'heart rate', 'blood pressure']:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())

#mean til mere jævnt fordelte kolonner
for col in ['height', 'weight', 'temperature', 'cholesterol']:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].mean())

#mode til kategoriske kolonner
for col in ['gender', 'blood type', 'diabetes', 'smoking']:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].mode()[0])

#historgram over numersike kolonner
df.select_dtypes(include='number').hist(figsize=(12, 10), bins=30, edgecolor="black")
plt.tight_layout()
plt.show()


df.to_csv("medical_students_dataset_imputed.csv", index=False)