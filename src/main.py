import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  slope  ca  thal  target
# (Male: 1; Female: 0)
df = pd.read_csv('data/Heart_disease_statlog.csv')

pd.set_option('display.max_rows', None)

df['sex'] = df['sex'].map({0: 'Female', 1: 'Male'})
df['cp'] = df['cp'].map({0: 'typical angina', 1: 'atypical angina', 2: 'non-anginal pain', 3: 'asymptomatic'})
df['slope'] = df['slope'].map({0: 'up sloping', 1: 'flat', 2: 'down sloping'})
df['thal'] = df['thal'].map({0: 'NULL', 1: 'normal blood flow', 2: 'fixed defect', 3: 'reversible defect'})
filtered_df = df.loc[df["target"] == 1]

# Example

fig = px.pie(
    filtered_df, 
    names='sex',  # Use Gender for labels
    title='Gender Distribution',
    hover_data= ["target"]
)

# Show the chart
fig.show()
#print(row) 
#print(df)