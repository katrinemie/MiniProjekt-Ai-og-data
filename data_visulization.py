import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

#Opret forbindelse til MySQL 
db = mysql.connector.connect(
    host="localhost",
    user="root"
)
cursor = db.cursor()

#Opret databasen hvis den ikke allerede findes, og vælg den
cursor.execute("CREATE DATABASE IF NOT EXISTS testdatabase")
cursor.execute("USE testdatabase")

#tabellen til medicinstuderende
cursor.execute("""
CREATE TABLE IF NOT EXISTS medical_students (
    student_id INT,
    age FLOAT,
    gender VARCHAR(10),
    height FLOAT,
    weight FLOAT,
    blood_type VARCHAR(3),
    bmi FLOAT,
    temperature FLOAT,
    heart_rate INT,
    blood_pressure FLOAT,
    cholesterol FLOAT,
    diabetes VARCHAR(5),
    smoking VARCHAR(5)
)
""")

print(" Databasen og tabellen er klar.")

#Læs det færdigimputerede datasæt
df = pd.read_csv("medical_students_dataset_imputed.csv")

#Ensret kolonnenavne, så vi undgår fejl
df.columns = df.columns.str.lower().str.strip()

#Indsæt data i SQL-tabellen
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO medical_students (
            student_id, age, gender, height, weight,
            blood_type, bmi, temperature, heart_rate,
            blood_pressure, cholesterol, diabetes, smoking
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

db.commit()
print(f" {len(df)} rækker indsat i 'medical_students'.")

#fordeling af alder
plt.figure(figsize=(8, 5))
df['age'].hist(bins=30, edgecolor='black')
plt.title("Aldersfordeling blandt medicinstuderende")
plt.xlabel("Alder")
plt.ylabel("Antal")
plt.tight_layout()
plt.show()


#boxplot af BMI
plt.figure(figsize=(6, 5))
df.boxplot(column='bmi')
plt.title("Boxplot, BMI")
plt.ylabel("Body Mass Index")
plt.tight_layout()
plt.show()


cursor.close()
db.close()

