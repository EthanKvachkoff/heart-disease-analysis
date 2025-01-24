import plotly.express as px

def gender_distribution_with_heart_disease(filtered_df):
    return px.pie(
        filtered_df, 
        names='sex',
        title='Gender Distribution With Heart Disease',
        hover_data=["target"]
    )

def gender_distribution(df):
    return px.histogram(
        df, 
        x='sex',
        color='sex',
        title='Gender Distribution'
    )

def chest_pain_distribution(df):
    return px.bar(
        df, 
        x='cp',  # Chest Pain Type
        title='Chest Pain Type Distribution',
        category_orders={
            'cp': ['typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic']
        }
    )

def blood_pressure_vs_heart_disease(df):
    return px.strip(
        df, 
        x='target',
        y='trestbps',
        title='Blood Pressure Levels vs Heart Disease',
        category_orders={'target': ['Normal', 'Heart Disease']}
    )

def cholesterol_vs_heart_disease(df):
    return px.strip(
        df, 
        x='target',
        y='chol',
        title='Cholesterol Levels vs Heart Disease',
        category_orders={'target': ['Normal', 'Heart Disease']}
    )

def fasting_blood_sugar_vs_heart_disease(df):
    return px.bar(
        df, 
        x='target',
        y='fbs',
        title='Fasting Blood Sugar vs Heart Disease',
        category_orders={'target': ['0', '1'], 'fbs': ['False', 'True']},
        labels={
            'fbs': 'Fasting Blood Sugar (True/False)', 
            'target': 'Heart Disease (0 = Normal, 1 = Disease)'
        }
    )

def vessels_vs_heart_disease(df):
    return px.bar(
        df, 
        x='target',
        y='ca',
        title='Number of Major Vessels vs Heart Disease',
        category_orders={'target': ['Normal', 'Heart Disease']}
    )

def age_vs_heart_rate(df):
    return px.scatter(
        df, 
        x='age',
        y='thalach',
        color='target',
        title='Age vs Maximum Heart Rate',
        category_orders={'target': ['Normal', 'Heart Disease']}
    )

def chest_pain_vs_vessels(df):
    return px.bar(
        df,
        x='cp',  # Chest Pain Type
        y='ca',  # Number of Major Vessels (0–3)
        color='target',
        title='Chest Pain Type vs. Number of Major Vessels',
        labels={
            'cp': 'Chest Pain Type',
            'ca': 'Number of Major Vessels (0–3)',
            'target': 'Heart Disease Presence'
        }
    )

def heart_rate_vs_exercise_induced_angina(df):
    return px.box(
        df, 
        y='thalach',  # Maximum Heart Rate
        color='exang',
        title='Heart Rate vs Exercise-Induced Angina',
    )