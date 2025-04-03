import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === 1. Indlæs datasættet ===
input_file = "medical_students_dataset.csv"  # Husk at placere filen i samme mappe
df = pd.read_csv(input_file)

# === 2. Data Cleaning ===

# Fjern tomme kolonner (alle værdier NaN)
df = df.dropna(axis=1, how='all')

# Fjern duplikerede rækker
df = df.drop_duplicates()

# Fjern outliers i numeriske kolonner (IQR-metoden)
for col in df.select_dtypes(include='number').columns:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

# Fjern rækker med tomme værdier
df = df.dropna()

# Gem det rensede datasæt
output_file = "medical_students_dataset_cleaned.csv"
df.to_csv(output_file, index=False)
print(f" Datasættet er renset og gemt som: {output_file}")

# === 3. Visualisering ===

# 3.1 Histogram over alder
plt.figure(figsize=(6, 4))
plt.hist(df['Age'], bins=10, color='lightblue', edgecolor='black')
plt.title('Aldersfordeling')
plt.xlabel('Alder')
plt.ylabel('Antal studerende')
plt.tight_layout()
plt.show()

# 3.2 Søjlediagram over køn
if 'Gender' in df.columns:
    plt.figure(figsize=(6, 4))
    gender_counts = df['Gender'].value_counts()
    bars = plt.bar(gender_counts.index, gender_counts.values, color='orange', edgecolor='black')

    # Tilføj tal ovenpå søjlerne
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 5, f'{int(height)}', 
                 ha='center', va='bottom', fontsize=9)

    plt.title('Fordeling af køn blandt studerende')
    plt.xlabel('Køn')
    plt.ylabel('Antal studerende')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# 3.3 Scatter plot: Højde vs. Vægt
if 'Height' in df.columns and 'Weight' in df.columns:
    plt.figure(figsize=(6, 5))
    plt.scatter(df['Height'], df['Weight'], alpha=0.6, color='green')
    plt.title('Sammenhæng mellem højde og vægt')
    plt.xlabel('Højde (cm)')
    plt.ylabel('Vægt (kg)')
    plt.tight_layout()
    plt.show()

# 3.4 Boxplot af BMI
if 'BMI' in df.columns:
    plt.figure(figsize=(5, 4))
    plt.boxplot(df['BMI'].dropna(), vert=False)
    plt.title('Boxplot af BMI')
    plt.xlabel('BMI')
    plt.tight_layout()
    plt.show()

# 3.5 Heatmap over korrelationer
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Korrelation mellem numeriske variable')
plt.tight_layout()
plt.show()
