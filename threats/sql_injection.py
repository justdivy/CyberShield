from threats.base import Threat

class SQLInjectionThreat(Threat):
    SQL_PATTERNS = ["'", "--", ";", "DROP", "SELECT", "OR 1=1", "UNION", "INSERT"]

    def __init__(self, target, input_data):
        super().__init__("SQL Injection Scan", "CRITICAL", target)
        self.input_data = input_data

    def scan(self):
        found = [p for p in self.SQL_PATTERNS if p.upper() in self.input_data.upper()]
        if found:
            self.is_detected = True
            self.details = f"Malicious SQL patterns: {found}"