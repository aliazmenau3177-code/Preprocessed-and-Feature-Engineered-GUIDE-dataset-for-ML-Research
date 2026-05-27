# ==========================================================
# GUIDE DATASET SOC OPTIMIZATION PIPELINE
# research on optimizing SOC through Big Data analysis
# ==========================================================

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# ==========================================================
# 1. LOAD DATA
# ==========================================================

DATA_PATH = "/home/ali/guidereduced2ndver.csv"

df = pd.read_csv(DATA_PATH, low_memory=False)
df.columns = df.columns.str.strip()

print("Dataset Shape:", df.shape)
print(df['IncidentGrade'].value_counts())

# ==========================================================
# 2. CREATE BINARY LABEL
# ==========================================================

df['label'] = df['IncidentGrade'].apply(
    lambda x: 0 if x in ['BenignPositive', 'FalsePositive'] else 1
)

print("\nLabel Distribution:")
print(df['label'].value_counts(normalize=True))

# ==========================================================
# 3. REMOVE LEAKAGE COLUMNS
# ==========================================================

leakage_cols = [
    'IncidentGrade',
    'LastVerdict',
    'ActionGrouped',
    'ActionGranular'
]

drop_cols = [
    'Id','AlertId','IncidentId',
    'Sha256','Url','RegistryKey',
    'RegistryValueName','RegistryValueData',
    'FolderPath','AccountSid','AccountUpn',
    'AccountObjectId','NetworkMessageId'
]

df = df.drop(columns=[c for c in leakage_cols + drop_cols if c in df.columns])

# ==========================================================
# 4. FEATURE ENGINEERING
# ==========================================================

# ---- Timestamp Features ----
if 'Timestamp' in df.columns:
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
    df['hour'] = df['Timestamp'].dt.hour
    df['dayofweek'] = df['Timestamp'].dt.dayofweek
    df = df.drop(columns=['Timestamp'])

# ---- MITRE Count ----
if 'MitreTechniques' in df.columns:
    df['MitreCount'] = df['MitreTechniques'].fillna('').apply(
        lambda x: len(str(x).split(';')) if x != '' else 0
    )
    df = df.drop(columns=['MitreTechniques'])

# ==========================================================
# 5. SPLIT FEATURES AND LABEL
# ==========================================================

X = df.drop('label', axis=1)
y = df['label']

# ==========================================================
# 6. ENCODE CATEGORICAL FEATURES (ONCE)
# ==========================================================

categorical_cols = X.select_dtypes(include=['object']).columns.tolist()

X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

print("Encoded Feature Shape:", X.shape)

# ==========================================================
# 6.5 EXPORT OF PREPROCESSED DATASET
# ==========================================================

print("\nDo you want to save the preprocessed & feature engineered dataset?")
user_choice = input("Type YES to save or NO to skip: ").strip().lower()

if user_choice == "yes":

    # Combine features and label for export
    processed_dataset = pd.concat([X, y], axis=1)

    save_path = input(
        "Enter full path where CSV should be saved (e.g., /home/ali/processed_GUIDE.csv): "
    ).strip()

    processed_dataset.to_csv(save_path, index=False)

    print("\nPreprocessed dataset saved successfully at:")
    print(save_path)

else:
    print("\nSkipping dataset export and continuing pipeline...")
