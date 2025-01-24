from plotly.subplots import make_subplots
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
from data_processing import load_and_process_data, filter_by_heart_disease
from config import DATA_FILE
import os
os.makedirs("interactive_plots", exist_ok=True)
# Load and process data
df = load_and_process_data(DATA_FILE)
filtered_df = filter_by_heart_disease(df)

# Generate visualizations
fig1 = gender_distribution_with_heart_disease(filtered_df)  # Pie chart
fig2 = gender_distribution(df)
fig3 = chest_pain_distribution(df)
fig4 = blood_pressure_vs_heart_disease(df)
fig5 = cholesterol_vs_heart_disease(df)
fig6 = fasting_blood_sugar_vs_heart_disease(df)
fig7 = vessels_vs_heart_disease(df)
fig8 = age_vs_heart_rate(df)
fig9 = chest_pain_vs_vessels(df)
fig10 = heart_rate_vs_exercise_induced_angina(df)


# Save the visualizations as HTML files
fig1.write_html("interactive_plots/fig1_gender_distribution.html")
fig2.write_html("interactive_plots/fig2_gender_distribution_histogram.html")
fig3.write_html("interactive_plots/fig3_chest_pain_distribution.html")
fig4.write_html("interactive_plots/fig4_blood_pressure_vs_heart_disease.html")
fig5.write_html("interactive_plots/fig5_cholesterol_vs_heart_disease.html")
fig6.write_html("interactive_plots/fig6_fasting_blood_sugar_vs_heart_disease.html")
fig7.write_html("interactive_plots/fig7_vessels_vs_heart_disease.html")
fig8.write_html("interactive_plots/fig8_age_vs_heart_rate.html")
fig9.write_html("interactive_plots/fig9_chest_pain_vs_vessels.html")
fig10.write_html("interactive_plots/fig10_heart_rate_vs_exercise_induced_angina.html")

# Create subplots with specific types for pie charts
fig = make_subplots(
    rows=5, cols=2,  # 5 rows and 2 columns
    specs=[
        [{"type": "domain"}, None],  # Row 1: Pie chart (domain) and empty space
        [{"type": "xy"}, {"type": "xy"}],  # Row 2: Standard XY plots
        [{"type": "xy"}, {"type": "xy"}],  # Row 3: Standard XY plots
        [{"type": "xy"}, {"type": "xy"}],  # Row 4: Standard XY plots
        [{"type": "xy"}, {"type": "xy"}],  # Row 5: Standard XY plots
    ],
    subplot_titles=[
        "Gender Distribution With Heart Disease", "Gender Distribution",
        "Chest Pain Distribution", "Blood Pressure vs Heart Disease",
        "Cholesterol vs Heart Disease", "Fasting Blood Sugar vs Heart Disease",
        "Vessels vs Heart Disease", "Age vs Heart Rate",
        "Chest Pain vs Vessels", "Heart Rate vs Exercise-Induced Angina"
    ],
)

# Add traces to subplots
fig.add_trace(fig1.data[0], row=1, col=1)  # Pie chart
fig.add_trace(fig2.data[0], row=2, col=1)
fig.add_trace(fig3.data[0], row=2, col=2)
fig.add_trace(fig4.data[0], row=3, col=1)
fig.add_trace(fig5.data[0], row=3, col=2)
fig.add_trace(fig6.data[0], row=4, col=1)
fig.add_trace(fig7.data[0], row=4, col=2)
fig.add_trace(fig8.data[0], row=5, col=1)
fig.add_trace(fig9.data[0], row=5, col=2)
fig.add_trace(fig10.data[0], row=5, col=2)

# Shows legend for charts
fig.update_traces(showlegend=True, selector=dict(type='pie'))

# Update layout
fig.update_layout(
    height=1500, width=1200,  # Adjust size
    title_text="All Visualizations Combined",
)

# Show combined plot
fig.show()