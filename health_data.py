# health_data_app.py

import pandas as pd
import gradio as gr
import google.generativeai as genai
from sklearn.impute import SimpleImputer
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# Load data
df1 = pd.read_excel("Health_data1.xlsm", engine='openpyxl')
df2 = pd.read_excel("Health_data2.xlsm", engine='openpyxl')

# Imputation function
def impute_missing_values(df):
    imputer_dict = {}
    for column in df.columns:
        if df[column].dtype == 'object' or df[column].nunique() < 10:
            imputer_dict[column] = SimpleImputer(strategy='most_frequent')
        else:
            imputer_dict[column] = SimpleImputer(strategy='median')
    for column, imputer in imputer_dict.items():
        df[column] = imputer.fit_transform(df[[column]])
    return df

# Impute missing data
df1 = impute_missing_values(df1)
df2 = impute_missing_values(df2)

# Patient data fetch
def get_patient_data(patient_id):
    row1 = df1[df1['Patient_Number'] == patient_id]
    row2 = df2[df2['Patient_Number'] == patient_id]
    if row1.empty or row2.empty:
        return None
    steps_avg = row2['Physical_activity'].mean()
    row1 = row1.copy()
    row1['Avg_Physical_Activity'] = steps_avg
    return row1

# Ask Gemini
def ask_gemini(patient_id, question):
    data = get_patient_data(patient_id)
    if data is None:
        return "❌ Patient not found in one of the datasets."
    context = data.to_string(index=False)
    prompt = f"""You are a medical assistant analyzing health records. Based on the following patient data, answer the user's question.\n\nPatient Data:\n{context}\n\nUser Question:\n{question}"""
    response = model.generate_content(prompt)
    return response.text

# Gradio Interface
def interface(patient_id, question):
    return ask_gemini(int(patient_id), question)

gr.Interface(fn=interface,
             inputs=[
                 gr.Number(label="Enter Patient Number"),
                 gr.Textbox(label="Ask a health-related question")
             ],
             outputs="text",
             title="🧬 GenAI Health Advisor (Gemini + Gradio)"
).launch(share=True)