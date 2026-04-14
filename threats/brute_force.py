from threats.base import Threat

class BruteForceThreat(Threat):
    THRESHOLD = 5

    def __init__(self, target, failed_attempts):
        super().__init__("Brute Force Scan", "MEDIUM", target)
        self.failed_attempts = failed_attempts

    def scan(self):
        if self.failed_attempts > self.THRESHOLD:
            self.is_detected = True
            self.details = f"{self.failed_attempts} failed login attempts (limit: {self.THRESHOLD})"