import re
from urllib.parse import urlparse

class URLDetector:
    def __init__(self):
        # Suspicious keywords commonly found in phishing URLs
        self.suspicious_keywords = [
            'login', 'verify', 'update', 'secure', 'account', 
            'banking', 'confirm', 'signin', 'ebayisapi', 'webscr'
        ]

    def extract_features(self, url: str) -> dict:
        parsed = urlparse(url)
        hostname = parsed.hostname or ""
        path = parsed.path
        
        # Feature calculations
        url_length = len(url)
        has_at_symbol = 1 if '@' in url else 0
        dot_count = hostname.count('.')
        hyphen_count = hostname.count('-')
        
        # Check for IP address in hostname
        ip_pattern = re.compile(
            r'^(?:(?:25[0-5]|2[4][0-9]|[01]?[0-9][0-9]?)\.){3}'
            r'(?:25[0-5]|2[4][0-9]|[01]?[0-9][0-9]?)$'
        )
        has_ip = 1 if ip_pattern.match(hostname) else 0
        
        # Keyword match count
        keyword_matches = sum(1 for kw in self.suspicious_keywords if kw in url.lower())
        
        return {
            "url_length": url_length,
            "has_at_symbol": has_at_symbol,
            "dot_count": dot_count,
            "hyphen_count": hyphen_count,
            "has_ip": has_ip,
            "keyword_matches": keyword_matches
        }

    def classify(self, url: str) -> tuple:
        features = self.extract_features(url)
        
        # Heuristic risk scoring model
        risk_score = 0.0
        
        if features["url_length"] > 75:
            risk_score += 0.25
        if features["has_at_symbol"] == 1:
            risk_score += 0.35
        if features["has_ip"] == 1:
            risk_score += 0.40
        if features["keyword_matches"] > 0:
            risk_score += (0.15 * features["keyword_matches"])
        if features["hyphen_count"] > 2:
            risk_score += 0.20
            
        risk_score = min(risk_score, 1.0)
        
        status = "Potential Phishing" if risk_score >= 0.4 else "Likely Legitimate"
        return status, round(risk_score, 2), features
