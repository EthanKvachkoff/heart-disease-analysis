# Heart Disease Data Analysis & Visualization

## Overview

This project performs data analysis and visualizations on a dataset related to heart disease. The dataset contains information about patients' medical attributes such as age, sex, cholesterol levels, blood pressure, and more. The goal of this analysis is to explore patterns, relationships, and insights related to the occurrence of heart disease, using various statistical and visual techniques.

We use **Plotly** for interactive visualizations, which allow us to uncover significant trends and relationships within the data.

## Dataset Overview

The dataset consists of the following columns:

- **age**: Age of the patient
- **sex**: Gender of the patient (Male: 1, Female: 0)
- **cp**: Type of chest pain (0: typical angina, 1: atypical angina, 2: non-anginal pain, 3: asymptomatic)
- **trestbps**: Resting blood pressure
- **chol**: Serum cholesterol level
- **fbs**: Fasting blood sugar (1: true, 0: false)
- **restecg**: Resting electrocardiographic results (0: normal, 1: ST-T wave abnormality, 2: left ventricular hypertrophy)
- **thalach**: Maximum heart rate achieved
- **exang**: Exercise-induced angina (1: yes, 0: no)
- **oldpeak**: Depression induced by exercise relative to rest
- **slope**: Slope of the peak exercise ST segment (0: upsloping, 1: flat, 2: downsloping)
- **ca**: Number of major vessels colored by fluoroscopy
- **thal**: Thalassemia (1: normal, 2: fixed defect, 3: reversible defect)
- **target**: Presence of heart disease (1: disease, 0: normal)

## Visualizations and Insights

This project generates 10 different visualizations to analyze various aspects of heart disease, including distribution of patient demographics, chest pain types, and correlations between medical factors and heart disease. The visualizations include:

### 1. **Gender Distribution With Heart Disease**
   - **Visualization Type**: Pie Chart
   - **Insight**: This chart shows the proportion of males and females with heart disease. The visualization reveals whether gender plays a role in the occurrence of heart disease among patients.

### 2. **Gender Distribution**
   - **Visualization Type**: Histogram
   - **Insight**: This histogram shows the overall gender distribution in the dataset, providing a broader understanding of the gender demographics in the study population.

### 3. **Chest Pain Type Distribution**
   - **Visualization Type**: Bar Chart
   - **Insight**: This bar chart illustrates the distribution of chest pain types, highlighting the prevalence of different chest pain categories among patients. It provides a breakdown of how common each type of pain is, helping us to understand potential risk factors associated with each category.

### 4. **Blood Pressure Levels vs Heart Disease**
   - **Visualization Type**: Strip Plot
   - **Insight**: This strip plot compares blood pressure levels across patients with and without heart disease. It helps identify any trends or correlations between high blood pressure and the presence of heart disease.

### 5. **Cholesterol Levels vs Heart Disease**
   - **Visualization Type**: Strip Plot
   - **Insight**: This plot examines cholesterol levels in patients and compares those with heart disease to those without. Elevated cholesterol is often a key risk factor for heart disease, and this chart helps visualize its significance.

### 6. **Fasting Blood Sugar vs Heart Disease**
   - **Visualization Type**: Bar Chart
   - **Insight**: The chart illustrates the relationship between fasting blood sugar levels and heart disease. It shows whether a higher fasting blood sugar level correlates with a greater likelihood of having heart disease.

### 7. **Number of Major Vessels vs Heart Disease**
   - **Visualization Type**: Bar Chart
   - **Insight**: This bar chart explores the relationship between the number of major vessels (identified by fluoroscopy) and heart disease. Fewer vessels visible in fluoroscopy are often indicative of more severe heart disease, making this a critical chart for medical analysis.

### 8. **Age vs Heart Rate**
   - **Visualization Type**: Scatter Plot
   - **Insight**: This scatter plot investigates the relationship between a patient’s age and maximum heart rate achieved during exercise. It helps to identify whether there is any age-related decline in heart rate and if this is associated with the presence of heart disease.

### 9. **Chest Pain Type vs Number of Major Vessels**
   - **Visualization Type**: Bar Chart
   - **Insight**: This chart compares chest pain types with the number of major vessels seen in fluoroscopy. It can help determine whether certain types of chest pain are linked to a higher number of blocked vessels.

### 10. **Heart Rate vs Exercise-Induced Angina**
   - **Visualization Type**: Box Plot
   - **Insight**: This box plot visualizes the relationship between exercise-induced angina and heart rate. It can provide insights into how exercise-induced angina might correlate with heart disease severity, as patients experiencing angina may have lower heart rates during exercise.

## Key Findings

From these visualizations, the following key findings emerge:

1. **Gender and Heart Disease**: While the gender distribution of heart disease is relatively even, further analysis suggests males tend to have more severe heart disease (higher number of blocked vessels).

2. **Cholesterol and Blood Pressure**: Elevated cholesterol and high blood pressure are strongly associated with the presence of heart disease. Patients with heart disease consistently show higher blood pressure and cholesterol levels.

3. **Chest Pain Type**: Patients with 'typical angina' chest pain type tend to show higher occurrences of heart disease, while 'asymptomatic' patients seem to have lower incidences of the disease.

4. **Fasting Blood Sugar**: There is a noticeable relationship between higher fasting blood sugar levels and a greater likelihood of heart disease, aligning with known risk factors for cardiovascular conditions.

5. **Exercise-Induced Angina**: The presence of exercise-induced angina correlates with lower heart rates during exercise, potentially indicating a lack of cardiac reserve in these patients.

## Conclusion

This project highlights the important relationships between various factors (such as cholesterol, blood pressure, gender, and chest pain type) and heart disease. By visualizing these relationships, the project provides valuable insights into how medical variables correlate with the likelihood of heart disease and the severity of the condition.

## Installation & Usage

### Requirements

- Python 3.x
- Pandas
- Plotly
- Other dependencies (as listed in the `requirements.txt` file)

### To Run the Project

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/EthanKvachkoff/heart-disease-analysis.git
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the script to generate and display the visualizations:
    ```bash
    python analysis_script.py

## Data File

The dataset used for analysis, `Heart_disease_statlog.csv`, contains various medical attributes related to heart disease. To run this project, make sure to place the dataset in the `data/` directory. If you store the file in a different location, ensure to adjust the file path accordingly in the code where the dataset is loaded. For example:

    df = load_and_process_data('path_to_your_data_file/Heart_disease_statlog.csv') 

## Future Work

There are several areas for potential expansion and improvement in this project:

### 1. **Data Cleaning**
The dataset may contain missing or incorrect values, which can affect the analysis and visualizations. Future work could focus on:
   - **Handling Missing Values**: Implement techniques like imputation or removal of missing data to improve dataset quality.
   - **Outlier Detection**: Identify and address outliers that could skew analysis results.
   - **Ensuring Consistency**: Standardize the data types and check for any inconsistencies in the features.

### 2. **Machine Learning**
Implementing a machine learning model could be a valuable next step. The goal would be to predict the likelihood of heart disease based on the input medical features. Potential approaches include:
   - **Classification Models**: Train models such as Logistic Regression, Decision Trees, or Random Forests.
   - **Model Evaluation**: Assess the performance of the models using metrics like accuracy, precision, recall, and F1-score.
   - **Integration with Visualizations**: Once trained, the model results could be used to create new visualizations that provide predictive insights.

### 3. **Additional Visualizations**
While the current visualizations provide valuable insights, further exploration of the data could be done through more advanced visualizations:
   - **3D Plots**: Use 3D scatter or surface plots to explore relationships between multiple variables simultaneously.
   - **Animations**: Create animated visualizations to track how key metrics (such as age, cholesterol levels, etc.) change over time or across heart disease severity.
   - **Heatmaps**: Display correlation matrices or pairwise relationships between features using heatmaps to gain a better understanding of data dependencies.
   - **Interactive Dashboards**: Build an interactive dashboard to allow users to filter and explore the data in real-time, which would provide more dynamic insights.

These enhancements would provide deeper insights into the dataset and could be valuable in predicting and understanding heart disease, potentially aiding in preventative healthcare measures.