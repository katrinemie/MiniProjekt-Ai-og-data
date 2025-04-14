import pandas as pd  
import matplotlib.pyplot as plt


df = pd.read_csv("medical_students_dataset.csv")


print("Første 10 rækker i datasættet:")
print(df.head())


print("\nManglende værdier pr. kolonne:")
print(df.isnull().sum())

#Tjekker for duplikerede rækker
duplikater = df.duplicated().sum()
print(f"\nAntal duplikerede rækker: {duplikater}")

#statistisk oversigt over numeriske kolonner
print("\nStatistisk overblik:")
print(df.describe())


if 'Gender' in df.columns:
    print("\nFordeling af køn:")
    print(df['Gender'].value_counts())

    df['Gender'].value_counts().plot(kind='bar', title='Fordeling af køn')
    plt.tight_layout()
    plt.show()

#Hvis kolonnen 'Age' findes, vises boxplot
if 'Age' in df.columns:
    plt.boxplot(df['Age'].dropna(), labels=['Age'])
    plt.title('Boxplot over alder')
    plt.tight_layout()
    plt.show()



