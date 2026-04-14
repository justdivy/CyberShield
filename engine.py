class ThreatEngine:
    def __init__(self):
        self.threats = []

    def load(self, *threat_objects):
        self.threats.extend(threat_objects)

    def run_all(self):
        for threat in self.threats:
            threat.scan()

    def get_summary(self):
        total = len(self.threats)
        detected = sum(1 for t in self.threats if t.is_detected)
        return total, detected