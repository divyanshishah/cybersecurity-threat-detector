🛡️ CyberShield Threat Intelligence Platform

An enterprise-grade, real-time cybersecurity platform designed for Phishing URL Detection, Malicious Email Analysis, and Batch Security Auditing built with Python and Streamlit.

📌 Project Overview

CyberShield Threat Detector is an integrated security tool built to combat digital phishing and social engineering attacks. By leveraging lexical feature extraction, heuristic analysis, and Natural Language Processing (NLP) pattern detection, the application enables users to evaluate individual suspicious URLs, analyze incoming email content for embedded threats, and conduct batch audits on datasets.

📊 Dataset Link

Dataset Used: Phishing Site URLs & Malicious Email Detection Dataset

Access / Link: Kaggle - Phishing Websites Dataset / Included locally as sample_urls.csv for Module 3 batch analysis.

🛠️ Technologies Used

Programming Language: Python 3.9+

Web Application Framework: Streamlit

Data Processing & Analysis: Pandas, NumPy

Interactive Visualizations: Plotly Express, Matplotlib, Seaborn

Pattern Matching & NLP Engine: Python re (Regular Expressions) & urllib.parse

🚀 Setup & Run Instructions

1. Prerequisites

Ensure Python 3.9 or higher is installed on your operating system.

2. Extract / Clone Project

Extract the project ZIP file or clone the repository using Git:

git clone https://github.com/YOUR_USERNAME/phishing_email_detection_project.git
cd phishing_email_detection_project


3. Install Dependencies

Install all required libraries using the provided requirements.txt:

pip install -r requirements.txt


4. Run the Application

Execute the Streamlit application using the main submission script:

streamlit run Divyanshi_PhishingDetection.py


Note: The web application will automatically open in your default browser at http://localhost:8501.

📁 Key Files & Project Structure

phishing_email_detection_project/
│
├── Divyanshi_PhishingDetection.py  # Main Streamlit Application Source Code
├── email_detector.py               # Module 2: Email NLP Analysis Engine
├── url_detector.py                 # Module 1: Heuristic URL Feature Extractor
├── sample_urls.csv                 # Sample Dataset for Batch Auditing
├── requirements.txt                # Python Library Dependencies
├── Divyanshi_ProjectReport.docx    # Formal Project Documentation Report
└── README.md                       # Project Overview and Instructions


🔑 Key Features

Real-Time URL Risk Scoring: Evaluates structural indicators (IP presence, @ symbols, domain hyphens, keywords).

Email Content Extraction: Automatically scans email text, extracts embedded links, and highlights suspicious urgency triggers.

Batch CSV Audit: Allows batch processing of external datasets with interactive visual dashboards and downloadable scan reports.