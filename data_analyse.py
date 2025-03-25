import pandas as pd  
import matplotlib.pyplot as plt

# 1. Læs datasættet
df = pd.read_csv("medical_students_dataset.csv")

# 2. Vis de første 5 rækker (for at få en idé om strukturen)
print("Første 5 rækker:")
print(df.head())

# 3. Tjek for manglende værdier (NaN)
print("\nAntal manglende værdier pr. kolonne:")
print(df.isnull().sum())

# 4. Tjek for duplikerede rækker
antal_dupl = df.duplicated().sum()
print(f"\nAntal duplikerede rækker: {antal_dupl}")

# 5. Tjek for outliers (enkelt kig med statistik)
print("\nStatistisk oversigt (df.describe()):")
print(df.describe())

# 6. Eksempel på at se fordeling af en kategori (f.eks. 'Gender' hvis den findes)
if 'Gender' in df.columns:
    print("\nFordeling af køn (Gender):")
    print(df['Gender'].value_counts())

    # Simpel søjlediagram
    df['Gender'].value_counts().plot(kind='bar', title='Fordeling af køn')
    plt.show()

# 7. (Valgfrit) Eksempel på boxplot af en numerisk kolonne (f.eks. 'Age')
if 'Age' in df.columns:
    plt.boxplot(df['Age'].dropna(), labels=['Age'])
    plt.title('Boxplot - Age')
    plt.show()

print("\n--- Færdig med datatjek ---")




