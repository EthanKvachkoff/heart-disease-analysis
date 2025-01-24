from data_processing import load_and_process_data, filter_by_heart_disease
from visualizations import (
    gender_distribution_with_heart_disease,
    gender_distribution,
    chest_pain_distribution,
    blood_pressure_vs_heart_disease,
    cholesterol_vs_heart_disease,
    fasting_blood_sugar_vs_heart_disease,
    vessels_vs_heart_disease,
    age_vs_heart_rate,
    chest_pain_vs_vessels,
    heart_rate_vs_exercise_induced_angina
)
from config import DATA_FILE

# Load and process data
df = load_and_process_data(DATA_FILE)
filtered_df = filter_by_heart_disease(df)

# Generate visualizations
fig1 = gender_distribution_with_heart_disease(filtered_df)
fig2 = gender_distribution(df)
fig3 = chest_pain_distribution(df)
fig4 = blood_pressure_vs_heart_disease(df)
fig5 = cholesterol_vs_heart_disease(df)
fig6 = fasting_blood_sugar_vs_heart_disease(df)
fig7 = vessels_vs_heart_disease(df)
fig8 = age_vs_heart_rate(df)
fig9 = chest_pain_vs_vessels(df)
fig10 = heart_rate_vs_exercise_induced_angina(df)

# Display visualizations
fig1.show()
fig2.show()
fig3.show()
fig4.show()
fig5.show()
fig6.show()
fig7.show()
fig8.show()
fig9.show()
fig10.show()