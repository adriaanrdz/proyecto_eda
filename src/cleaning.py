import pandas as pd
# Normalización de columnas.
def clean_columns (df):
    df.columns = [i.lower() for i in df.columns]
    df.rename(columns={"hourly_rate (usd)":"hourly_rate"}, inplace=True)
    return df

# Normalización valores gender
def gender_clean (x):
    if str(x).strip().lower() == "female" or str(x).strip().lower() == "f":
        return "Female"
    elif str(x).strip().lower() == "male" or str(x).strip().lower() == "m":
        return "Male"
    else:
        return x
    
# Normalización valores is_active:
def is_active_clean (x):
    if str(x).strip().lower() == "false" or str(x).strip().lower() == "n" or str(x).strip().lower() == "0" or str(x).strip().lower() == "no":
        return False
    elif str(x).strip().lower() == "true" or str(x).strip().lower() == "y" or str(x).strip().lower() == "1" or str(x).strip().lower() == "yes":
        return True
    else:
        return x

# Limpieza de valores mixtos en columnas numéricas
def clean_hourly_rate (df):
    df["hourly_rate"] = df["hourly_rate"].astype(str).replace(r"([a-zA-Z])|(\$)", "", regex=True)
    df["hourly_rate"] = df["hourly_rate"].str.strip()
    df["hourly_rate"] = pd.to_numeric(df["hourly_rate"], errors="coerce")
    return df

def clean_client_satisfaction (df):
    df["client_satisfaction"] = df["client_satisfaction"].astype(str).replace(r"\%", "", regex=True)
    df["client_satisfaction"] = df["client_satisfaction"].str.strip()
    df["client_satisfaction"] = pd.to_numeric(df["client_satisfaction"], errors="coerce")
    return df

# Imputaciones
def imput_age(df):
    mediana_age = df["age"].median()
    df["age"].fillna(mediana_age, inplace=True)
    return df