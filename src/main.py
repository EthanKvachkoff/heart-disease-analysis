import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  slope  ca  thal  target
# (Male: 1; Female: 0)
df = pd.read_csv('data/Heart_disease_statlog.csv')
pd.set_option('display.max_rows', None)

df['sex'] = df['sex'].map({0: 'Female', 1: 'Male'})
df['fbs'] = df['fbs'].map({0: 'False', 1: 'True'})
df['target'] = df['target'].map({0: 'Normal', 1: 'Heart Disease'})
df['cp'] = df['cp'].map({0: 'typical angina', 1: 'atypical angina', 2: 'non-anginal pain', 3: 'asymptomatic'})
df['slope'] = df['slope'].map({0: 'up sloping', 1: 'flat', 2: 'down sloping'})
df['thal'] = df['thal'].map({0: 'NULL', 1: 'normal blood flow', 2: 'fixed defect', 3: 'reversible defect'})
df['restecg'] = df['restecg'].map({0: 'normal', 1: 'ST-T wave abnormality', 2: 'probable or definite left ventricular hypertrophyby Estes'})

filtered_df = df.loc[df["target"] == 1]

# Example

fig1 = px.pie(
    filtered_df, 
    names='sex',
    title='Gender Distribution With Heart Disease',
    hover_data= ["target"]
)

fig2 = px.histogram(
    df, 
    x = 'sex',
    color = 'sex',
    title='Gender Distribution',
)

fig3 = px.bar(
    df, 
    x='cp',  # Chest Pain Type
    title='Chest Pain Type Distribution',
    category_orders={'cp': ['typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic']}  # Define custom order
)

fig4 = px.strip(
    df, 
    x='target',
    y='trestbps',
    title='Blood Pressure Levels vs Heart Disease',
    category_orders={'target': ['Normal', 'Heart Disease']}
)

fig5 = px.strip(
    df, 
    x='target',
    y='chol',
    title='Cholesterol Levels vs Heart Disease',
    category_orders={'target': ['Normal', 'Heart Disease']}
)

fig6 = px.bar(
    df, 
    x='target',
    y='fbs',
    title='Fasting Blood Sugar vs Heart Disease',
    category_orders={'target': ['0', '1'], 'fbs': ['False', 'True']},
    labels={'fbs': 'Fasting Blood Sugar (True/False)', 'target': 'Heart Disease (0 = Normal, 1 = Disease)'}
)

fig7 = px.bar(
    df, 
    x='target',
    y='ca',
    title='Number of Major Vessels vs Heart Disease',
    category_orders={'target': ['Normal', 'Heart Disease']},
)

fig8 = px.scatter(
    df, 
    x='age',
    y='thalach',
    color = 'target',
    title='Cholesterol Levels vs Heart Disease',
    category_orders={'target': ['Normal', 'Heart Disease']}
)

fig9 = px.bar(
    df, 
    y='ca',  # Chest Pain Type
    color = 'target',
    title='Chest Pain Type Distribution',
)

fig10 = px.box(
    df, 
    y='thalach',  # Chest Pain Type
    color = 'exang',
    title='Chest Pain Type Distribution',
)

# Show the chart
#fig1.show()
#fig2.update_layout(yaxis=dict(range=[0, 270]))
#fig2.show()
#fig3.show()
#fig4.show()
#fig5.show()
#fig6.show()  FIX
#fig7.update_layout(yaxis=dict(range=[0, 3]))
#fig7.show()
#fig8.show()
#fig9.show()
fig10.show()