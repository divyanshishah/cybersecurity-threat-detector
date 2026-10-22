# 🛡️ CyberShield Threat Intelligence Platform

> An enterprise-grade, real-time cybersecurity platform designed for **Phishing URL Detection**, **Malicious Email Analysis**, and **Batch Security Auditing** built with Python and Streamlit.

---

## 📌 Features & Key Modules

### 🔗 Module 1: Phishing URL Detector
- **Feature Extraction**: Extracts character patterns, lexical attributes, sub-domain structures, and protocol parameters.
- **Heuristic & Rule-Based Engine**: Identifies IP address usage, suspicious keywords (`login`, `verify`, `account`, etc.), excessive hyphens, and high-entropy parameters.
- **Real-Time Risk Scoring**: Generates instant threat classification (*Potential Phishing* vs. *Likely Legitimate*) with a calculated risk score percentage.

### 📧 Module 2: Malicious Email Detector
- **NLP Suspicious Pattern Analysis**: Scans email headers, subjects, and body text against known social-engineering triggers (e.g., urgency flags, account suspension notices).
- **Embedded Link Extraction**: Automatically extracts hidden and visible URLs from email content and passes them directly to the URL Scanner engine.
- **Combined Threat Assessment**: Computes a unified threat score factoring in both text semantics and embedded URL risks.

### 📊 Module 3: Security Dashboard & Batch CSV Scanner
- **Bulk Auditing**: Upload CSV datasets containing batches of URLs for enterprise-level security audits.
- **Interactive Visualizations**: View threat distributions with real-time interactive Pie Charts (powered by Plotly).
- **Report Export**: Export complete security scan results and audit trails to downloadable CSV reports.

---

## 🛠️ Tech Stack & Architecture

- **Frontend / UI**: [Streamlit](https://streamlit.io/) (Enhanced with custom dark cyber-themed CSS)
- **Data Processing**: `pandas`, `numpy`
- **Visualization**: `plotly`, `matplotlib`, `seaborn`
- **Regex & NLP Rules**: Built-in Python `re` engine & URL parsing libraries

---

## 📁 Project Structure

```text
cybersecurity_scanner/
│
├── app.py                  # Main Streamlit CyberShield Security Application
├── url_detector.py         # Module 1: Heuristic Engine for Phishing URL Scanning
├── email_detector.py       # Module 2: Email NLP Analysis & Embedded Link Extractor
├── sample_urls.csv         # Sample dataset for Batch CSV testing
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation

---

## 🚀 Quick Start Guide

### 1. Prerequisites
Ensure you have Python 3.9+ installed on your system.

### 2. Extract & Setup
1. Extract the downloaded ZIP archive.
2. Open your terminal inside the extracted project folder.

### 3. Install Dependencies
```bash
pip install -r requirements.txt

### 4. Run the application:
   ```bash
   streamlit run app.py
   ```
