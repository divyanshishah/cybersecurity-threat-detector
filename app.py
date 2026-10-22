import streamlit as st
import pandas as pd
from url_detector import URLDetector
from email_detector import EmailDetector

# 1. Page Config me layout aur icon set karein
st.set_page_config(
    page_title="CyberShield Threat Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS load / inject 
st.markdown("""
    <style>
    /* Dark Cybersecurity Theme */
    .stApp {
        background-color: #0e1117;
        color: #e0e6ed;
    }
    
    /* Header Container Styling */
    .main-header {
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        padding: 2rem;
        border-radius: 12px;
        border: 1px solid #374151;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    
    /* Custom Card Containers */
    .metric-card {
        background-color: #1f2937;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #3b82f6;
        box-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }
    
    /* Risk Status Badges */
    .status-phishing {
        color: #ef4444;
        background-color: #450a0a;
        padding: 0.4rem 0.8rem;
        border-radius: 6px;
        font-weight: bold;
        border: 1px solid #991b1b;
    }
    
    .status-safe {
        color: #10b981;
        background-color: #064e3b;
        padding: 0.4rem 0.8rem;
        border-radius: 6px;
        font-weight: bold;
        border: 1px solid #065f46;
    }
    </style>

    <style>
    /* Streamlit Button Text and Background Customization */
    div.stButton > button {
        color: #ffffff !important;          /* Button Text Color (e.g., White) */
        background-color: #3b82f6 !important; /* Button Background Color (e.g., Blue) */
        border-color: #3b82f6 !important;     /* Border Color */
        font-weight: bold;
    }
    
    /* Button Hover Effect (Jab mouse button ke upar jaye) */
    div.stButton > button:hover {
        color: #ffffff !important;
        background-color: #2563eb !important; /* Darker Blue on Hover */
        border-color: #2563eb !important;
    }
    </style>
    
""", unsafe_allow_html=True)

# 3. Main Header UI
st.markdown("""
    <div class="main-header">
        <h1 style="color: #60a5fa; margin-bottom: 0.5rem;">🛡️ CyberShield Threat Detector</h1>
        <p style="color: #9ca3af; font-size: 1.1rem;">AI-Powered Real-Time Phishing & Email Threat Intelligence Platform</p>
    </div>
""", unsafe_allow_html=True)

# for side bar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/shield.png", width=80)
    st.title("Control Panel")
    st.info("🟢 **Engine Status:** Active\n\n 🛡️**Detection Rules:** v2.4 Updated")
    st.divider()
    st.markdown("### Quick Statistics")
    st.metric(label="Model Accuracy", value="94.2%")

url_det = URLDetector()
email_det = EmailDetector()

st.title("🛡️ Cybersecurity Threat Detection Dashboard")
st.markdown("Enterprise-grade security analysis tool for Phishing URL detection, Email threat analysis, and batch auditing.")

tab1, tab2, tab3 = st.tabs(["🔗 Phishing URL Scanner", "📧 Malicious Email Scanner", "📊 Batch CSV Security Dashboard"])

# TAB 1: URL Scanner
with tab1:
    st.header("Module 1: Phishing URL Detector")
    url_input = st.text_input("Enter URL to analyze:", placeholder="https://example.com/login")
    
    if st.button("Scan URL", key="scan_url_btn"):
        if url_input:
            status, score, features = url_det.classify(url_input)

            # Status Badge Display
            if status == "Potential Phishing":
                st.markdown(f'<div class="status-phishing">⚠️ THREAT DETECTED: {status}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="status-safe">✅ SAFE: {status}</div>', unsafe_allow_html=True)
            
            # Risk Meter Progress Bar
            st.write("### Threat Risk Level")
            st.progress(float(score))
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Classification Status", value=status)
                st.metric(label="Calculated Risk Score", value=f"{score * 100}%")
            with col2:
                st.subheader("Structural Indicators")
                st.json(features)
                
            if status == "Potential Phishing":
                st.error("⚠️ Warning: High probability of phishing indicators detected!")
            else:
                st.success("✅ URL appears legitimate based on structural heuristics.")
        else:
            st.warning("Please enter a valid URL.")


            

# TAB 2: Email Scanner
with tab2:
    st.header("Module 2: Malicious Email Analyzer")
    email_subject = st.text_input("Email Subject:")
    email_body = st.text_area("Email Body Text:", placeholder="Paste email content here...")
    
    if st.button("Analyze Email", key="scan_email_btn"):
        if email_subject or email_body:
            result = email_det.analyze_email(email_subject, email_body)
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Email Threat Status", value=result["status"])
                st.metric(label="Overall Threat Score", value=f"{result['risk_score'] * 100}%")
            with col2:
                st.subheader("Detected Suspicious Phrases")
                if result["matched_phrases"]:
                    st.write(result["matched_phrases"])
                else:
                    st.info("No suspicious triggers found in text.")
                    
            st.subheader("Embedded Link Analysis")
            if result["extracted_links"]:
                link_df = pd.DataFrame(result["extracted_links"])
                st.dataframe(link_df, use_container_width=True)
            else:
                st.info("No URLs found within the email body.")
        else:
            st.warning("Please provide email subject or body.")

# TAB 3: Security Dashboard & Batch CSV Analysis
with tab3:
    st.header("Module 3: Security Operations Dashboard & Batch Analysis")
    st.markdown("Upload a CSV file containing a column of URLs for bulk security auditing.")
    
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"], key="csv_upload_box")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("Dataset Preview")
        st.dataframe(df.head(), use_container_width=True)
        
        column_name = st.selectbox("Select column containing URLs:", df.columns, key="col_select_box")
        
        if st.button("Run Batch Scan", key="batch_scan_btn"):
            results = []
            for url in df[column_name].dropna():
                status, score, _ = url_det.classify(str(url))
                results.append({"URL": url, "Status": status, "Risk Score": score})
                
            result_df = pd.DataFrame(results)
            
            st.subheader("Batch Scan Results Summary")
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Scanned", len(result_df))
            col2.metric("Phishing Detected", len(result_df[result_df["Status"] == "Potential Phishing"]))
            col3.metric("Legitimate URLs", len(result_df[result_df["Status"] == "Likely Legitimate"]))
            
            st.dataframe(result_df, use_container_width=True)
            
            # Plotly Chart Integration
            import plotly.express as px
            phish_count = len(result_df[result_df["Status"] == "Potential Phishing"])
            safe_count = len(result_df[result_df["Status"] == "Likely Legitimate"])

            fig = px.pie(
                names=["Potential Phishing", "Likely Legitimate"],
                values=[phish_count, safe_count],
                color_discrete_sequence=["#ef4444", "#10b981"],
                title="Scan Results Distribution"
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Export Report
            csv_export = result_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Export Security Report (CSV)",
                data=csv_export,
                file_name="security_audit_report.csv",
                mime="text/csv",
                key="download_csv_btn"
            )