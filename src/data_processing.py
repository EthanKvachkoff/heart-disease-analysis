import pandas as pd

def load_and_process_data(file_path):
    df = pd.read_csv(file_path)
    df['sex'] = df['sex'].map({0: 'Female', 1: 'Male'})
    df['fbs'] = df['fbs'].map({0: 'False', 1: 'True'})
    df['target'] = df['target'].map({0: 'Normal', 1: 'Heart Disease'})
    df['cp'] = df['cp'].map({0: 'typical angina', 1: 'atypical angina', 2: 'non-anginal pain', 3: 'asymptomatic'})
    df['slope'] = df['slope'].map({0: 'up sloping', 1: 'flat', 2: 'down sloping'})
    df['thal'] = df['thal'].map({0: 'NULL', 1: 'normal blood flow', 2: 'fixed defect', 3: 'reversible defect'})
    df['restecg'] = df['restecg'].map({0: 'normal', 1: 'ST-T wave abnormality', 2: 'probable or definite left ventricular hypertrophyby Estes'})
    return df

def filter_by_heart_disease(df):
    return df.loc[df["target"] == 1]