# Development-of-a-Custom-GenAI-Solution-for-Conducting-Health-Data-Analysis
Development of a Custom GenAI Solution for Conducting Health Data Analysis
## Overview
This project leverages Generative AI to analyze health data and provide insights through an interactive interface. It integrates Google Gemini with Gradio to create a user-friendly application for querying patient health records.

## Features
- **Data Imputation**: Automatically fills missing values in datasets using statistical methods.
- **Patient Data Retrieval**: Fetches and processes patient-specific data from multiple datasets.
- **Generative AI Integration**: Uses Google Gemini to answer health-related questions based on patient data.
- **Interactive Interface**: Provides a Gradio-based interface for easy interaction.

## Prerequisites
- Python 3.8 or higher
- Google Cloud API key with access to Gemini
- Required Python libraries (see `requirements.txt`)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Development-of-a-Custom-GenAI-Solution-for-Conducting-Health-Data-Analysis
   2. Create a virtual environment and activate it
   3. Install dependencies:
   pip install -r requirements.txt
   4.Add your Google API key to the .env file:GOOGLE_API_KEY="your-google-api-key"
   5.Ensure the datasets (Health_data1.xlsm and Health_data2.xlsm) are in the project directory.
   Usage
Run the application:
python [health_data.py](http://_vscodecontentref_/1)
Open the Gradio interface in your browser using the provided URL.

Enter a patient number and ask a health-related question to get AI-generated insights.
Example
Input:
Patient Number: 12345
Question: "What is the average physical activity of this patient?"
Based on the patient's health records, the average physical activity is 5000 steps per day.

Usage
Enter a patient number in the "Enter Patient Number" field.
Ask a health-related question in the "Ask a health-related question" field.
View the AI-generated response based on the patient's data.

File Descriptions
health_data.py
Data Loading: Loads Health_data1.xlsm and Health_data2.xlsm using pandas.
Data Imputation: Handles missing values using SimpleImputer.
Patient Data Fetching: Retrieves patient-specific data from the datasets.
Generative AI Integration: Sends patient data and user questions to Google Gemini for generating responses.
Gradio Interface: Provides an interactive interface for querying patient data.

requirements.txt
Lists all the Python dependencies required for the project:

google-generativeai
pandas
scikit-learn
gradio
openpyxl
python-dotenv
.env
Stores sensitive environment variables, such as the Google API key.

Health_data1.xlsm and Health_data2.xlsm
Excel files containing patient health data.

