import re
from url_detector import URLDetector

class EmailDetector:
    def __init__(self):
        self.url_detector = URLDetector()
        self.suspicious_phrases = [
            'urgent action required', 'verify your account', 'password expiration',
            'immediate suspension', 'click the link below', 'confirm your identity',
            'unauthorized login attempt', 'update payment details'
        ]

    def extract_links(self, text: str) -> list:
        url_pattern = re.compile(r'https?://[^\s<>"]+|www\.[^\s<>"]+')
        return list(set(url_pattern.findall(text)))

    def analyze_email(self, subject: str, body: str) -> dict:
        full_text = f"{subject} \n {body}".lower()
        
        # Check suspicious phrases
        matched_phrases = [phrase for phrase in self.suspicious_phrases if phrase in full_text]
        
        # Extract and scan embedded URLs
        extracted_links = self.extract_links(full_text)
        link_analysis = []
        
        max_link_risk = 0.0
        for link in extracted_links:
            status, score, features = self.url_detector.classify(link)
            link_analysis.append({"url": link, "status": status, "score": score})
            if score > max_link_risk:
                max_link_risk = score

        # Email Risk Calculation
        phrase_score = len(matched_phrases) * 0.25
        total_risk = min(max(phrase_score, max_link_risk), 1.0)
        
        email_status = "Malicious / Phishing Email" if total_risk >= 0.4 else "Safe / Legitimate Email"

        return {
            "status": email_status,
            "risk_score": round(total_risk, 2),
            "matched_phrases": matched_phrases,
            "extracted_links": link_analysis
        }
