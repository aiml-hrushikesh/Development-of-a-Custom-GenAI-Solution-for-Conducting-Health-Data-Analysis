# 🚀 Development of a Custom GenAI Solution for Conducting Health Data Analysis

This project leverages **Generative AI** to analyze health data and provide insights through an interactive interface. It integrates **Google Gemini** with **Gradio** to create a user-friendly application for querying health-related data.

---

## 📖 Overview

- **Generate AI-Powered Insights**: Uses Generative AI to answer health-related questions based on patient data.
- **Interactive Interface**: A Gradio-based interface for seamless interaction.
- **Data Processing Features**: Automatically handles missing data and retrieves patient-specific information.

---

## ✨ Features

- 🔍 **Data Imputation**: Automatically fills missing values in datasets using statistical methods.
- 📂 **Patient Data Retrieval**: Fetches and processes patient-specific data from multiple datasets.
- 🤖 **Generative AI Integration**: Uses Google Gemini to answer health-related questions.
- 🌐 **Interactive Interface**: Provides a Gradio-based interface for easy interaction.

---

## ⚙️ Prerequisites

Ensure you have the following installed and configured:

- 🐍 **Python**: Version 3.8 or higher
- 🔑 **Google Cloud API Key**: With access to Gemini
- 📦 **Required Python Libraries**: Listed in `requirements.txt`

---

## 🛠️ Installation

Follow these steps to set up the project:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd Development-of-a-Custom-GenAI-Solution-for-Conducting-Health-Data-Analysis
   2. **Create a Virtual Environment**:
   python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3.**Install Dependencies:**
pip install -r requirements.txt
4.**Add API Key:**
GOOGLE_API_KEY="your-google-api-key"
5.**Ensure Datasets Are Present:**
Place the following files in the project directory:
Health_data1.xlsm
Health_data2.xlsm

**Usage**
1.**Run the Application:**
python health_data.py
2.Access the Gradio Interface:

Open the provided URL in your browser.
3.Interact with the Application:

Enter a Patient Number in the "Enter Patient Number" field.
Ask a Health-Related Question in the "Ask a health-related question" field.
View the AI-Generated Response based on the patient's data.

Example
Input:

Patient Number: 12345
Question: "What is the average physical activity of this patient?"
Output:
Based on the patient's health records, the average physical activity is 5000 steps per day.

📂 File Descriptions
🧠 health_data.py
Handles the core functionality:

Data Loading: Loads Health_data1.xlsm and Health_data2.xlsm using pandas.
Data Imputation: Handles missing values using SimpleImputer.
Patient Data Fetching: Retrieves patient-specific data from the datasets.
Generative AI Integration: Sends patient data and user questions to Google Gemini for generating responses.
Gradio Interface: Provides an interactive interface for querying patient data.
📜 requirements.txt
Lists all the Python dependencies required for the project:

google-generativeai
pandas
scikit-learn
gradio
openpyxl
python-dotenv
🔒 .env
Stores sensitive environment variables, such as:

GOOGLE_API_KEY
📊 Health_data1.xlsm and Health_data2.xlsm
Excel files containing patient health data.

💡 Key Highlights
Simplifies health data analysis with AI-powered insights.
Easy-to-use interactive interface for healthcare professionals.
Securely integrates with Google Gemini for Generative AI capabilities.



