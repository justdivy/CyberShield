from threats.base import Threat

class PhishingThreat(Threat):
    SUSPICIOUS_KEYWORDS = ["login", "verify", "secure", "update", "bank", "account", "confirm"]

    def __init__(self, target, url):
        super().__init__("Phishing Scan", "CRITICAL", target)
        self.url = url

    def scan(self):
        found = [kw for kw in self.SUSPICIOUS_KEYWORDS if kw in self.url.lower()]
        if found:
            self.is_detected = True
            self.details = f"Suspicious keywords in URL: {found}"