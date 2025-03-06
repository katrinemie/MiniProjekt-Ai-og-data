import pandas as pd  


file_name = "medical_students_dataset.csv"  
df = pd.read_csv(file_name)

#5 rækker
print("Første 5 rækker af datasættet:")
print(df.head())


print("\nInformation om datasættet:")
print(df.info())


print("\nManglende værdier pr. kolonne:")
print(df.isnull().sum())
