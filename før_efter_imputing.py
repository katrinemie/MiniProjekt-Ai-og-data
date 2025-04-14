import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from xgboost import XGBClassifier

 
df_raw = pd.read_csv("medical_students_dataset.csv")
df_imputed = pd.read_csv("medical_students_dataset_imputed.csv")

#Fjern rækker hvor target 'Diabetes' mangler
df_raw = df_raw[df_raw['Diabetes'].notna()]
df_imputed = df_imputed[df_imputed['Diabetes'].notna()]

#Konverter og kod alle kategoriske kolonner med LabelEncoder
def encode_categoricals(df):
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str)
        df[col] = LabelEncoder().fit_transform(df[col])
    return df

df_raw = encode_categoricals(df_raw)
df_imputed = encode_categoricals(df_imputed)

#Funktion til træning og evaluering 
def train_and_evaluate(df, label="Før imputering"):
    df = df.dropna()  
    X = df.drop(columns="Diabetes")
    y = df["Diabetes"]

    #Skaler numeriske værdier
    numeric_cols = X.select_dtypes(include='number').columns
    scaler = StandardScaler()
    X[numeric_cols] = scaler.fit_transform(X[numeric_cols])

    #Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

    #Brug XGBoost Classifier i stedet for Logistic Regression 
    model = XGBClassifier(
        use_label_encoder=False,
        eval_metric='logloss',
        scale_pos_weight=(len(y_train) - sum(y_train)) / sum(y_train),  
        random_state=42
    )

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f"\n Resultater  {label}")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}")
    print(classification_report(y_test, y_pred))

#Kør modeller 
train_and_evaluate(df_raw, label="FØR imputering")
train_and_evaluate(df_imputed, label="EFTER imputering")