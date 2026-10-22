# 🛡️ CyberShield Threat Intelligence Platform

An enterprise-grade, real-time cybersecurity platform designed for **Phishing URL Detection, Malicious Email Analysis, and Batch Security Auditing** built with Python and Streamlit.

## 📌 Project Overview

CyberShield Threat Detector is an integrated security tool built to combat digital phishing and social engineering attacks. By leveraging lexical feature extraction, heuristic analysis, and Natural Language Processing (NLP) pattern detection, the application enables users to:

- Evaluate individual suspicious URLs.
- Analyze incoming email content for embedded threats.
- Conduct batch audits on datasets.

## 📊 Dataset Link

**Dataset Used:** Phishing Site URLs & Malicious Email Detection Dataset

**Access / Link:** Kaggle - Phishing Websites Dataset / Included locally as `sample_urls.csv` for Module 3 batch analysis.

## 🛠️ Technologies Used

- **Programming Language:** Python 3.9+
- **Web Application Framework:** Streamlit
- **Data Processing & Analysis:** Pandas, NumPy
- **Interactive Visualizations:** Plotly Express, Matplotlib, Seaborn
- **Pattern Matching & NLP Engine:** Python `re` (Regular Expressions) & `urllib.parse`

## 🚀 Setup & Run Instructions

### 1. Prerequisites

Ensure Python 3.9 or higher is installed on your operating system.

### 2. Extract / Clone Project

Extract the project ZIP file or clone the repository using Git:

```bash
git clone https://github.com/divyanshishah/cybersecurity-threat-detector.git
cd cybersecurity-threat-detector
```

### 3. Install Dependencies

Install all required libraries using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Execute the Streamlit application using the main submission script:

```bash
streamlit run Divyanshi_PhishingDetection.py
```

**Note:** The web application will automatically open in your default browser at:

[http://localhost:8501](http://localhost:8501)

## 📁 Key Files & Project Structure

```text
phishing_email_detection_project/
│
├── Divyanshi_PhishingDetection.py  # Main Streamlit Application Source Code
├── email_detector.py               # Module 2: Email NLP Analysis Engine
├── url_detector.py                 # Module 1: Heuristic URL Feature Extractor
├── sample_urls.csv                 # Sample Dataset for Batch Auditing
├── requirements.txt                # Python Library Dependencies
├── Divyanshi_ProjectReport.docx    # Formal Project Documentation Report
└── README.md                       # Project Overview and Instructions
```

## 🔑 Key Features

### 1. Real-Time URL Risk Scoring

Evaluates structural indicators, including:

- IP address presence.
- `@` symbols.
- Domain hyphens.
- Suspicious keywords.

### 2. Email Content Extraction

- Automatically scans email text.
- Extracts embedded links.
- Highlights suspicious urgency triggers.

### 3. Batch CSV Audit

- Allows batch processing of external datasets.
- Provides interactive visual dashboards.
- Supports downloadable scan reports.

---

**Project:** CyberShield Threat Intelligence Platform  
**Framework:** Streamlit  
**Language:** Python 3.9+
