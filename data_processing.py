import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Indlæs datasættet
df = pd.read_csv("medical_students_dataset.csv")

# 2. Databehandling (Data Cleaning)

# Fjern kolonner hvor alle værdier mangler
df = df.dropna(axis=1, how='all')

# Fjern duplikerede rækker
df = df.drop_duplicates()

# Fjern outliers i tal-kolonner (IQR-metoden)
for col in df.select_dtypes(include='number').columns:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    df = df[(df[col] >= lower) & (df[col] <= upper)]

# Fjern rækker med manglende værdier
df = df.dropna()

# Gem det rensede datasæt
df.to_csv("medical_students_dataset_cleaned.csv", index=False)
print("Datasættet er renset og gemt.")

# 3. Visualisering af data

# 3.1 Histogram over alder
plt.hist(df['Age'], bins=10, color='lightblue', edgecolor='black')
plt.title('Aldersfordeling')
plt.xlabel('Alder')
plt.ylabel('Antal studerende')
plt.tight_layout()
plt.show()

# 3.2 Søjlediagram over køn
if 'Gender' in df.columns:
    gender_counts = df['Gender'].value_counts()
    bars = plt.bar(gender_counts.index, gender_counts.values, color='orange', edgecolor='black')

    # Sæt tal over søjlerne
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 5, str(int(height)),
                 ha='center', va='bottom')

    plt.title('Fordeling af køn')
    plt.xlabel('Køn')
    plt.ylabel('Antal studerende')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

# 3.3 Boxplot af BMI
if 'BMI' in df.columns:
    plt.boxplot(df['BMI'].dropna(), vert=False)
    plt.title('Boxplot af BMI')
    plt.xlabel('BMI')
    plt.tight_layout()
    plt.show()

# 3.4 Korrelation mellem tal-kolonner
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Korrelation mellem talværdier')
plt.tight_layout()
plt.show()

