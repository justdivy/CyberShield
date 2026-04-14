from colorama import Fore, Style

class Threat:
    def __init__(self, name, severity, target):
        self.name = name
        self.severity = severity   # "LOW" | "MEDIUM" | "HIGH" | "CRITICAL"
        self.target = target
        self.is_detected = False
        self.details = ""

    def scan(self):
        raise NotImplementedError("Each threat must implement scan()")

    def report(self):
        colors = {
            "LOW": Fore.GREEN,
            "MEDIUM": Fore.YELLOW,
            "HIGH": Fore.RED,
            "CRITICAL": Fore.MAGENTA
        }
        color = colors.get(self.severity, Fore.WHITE)
        status = "⚠  DETECTED" if self.is_detected else "✔  CLEAN"
        print(f"{color}[{self.severity}]{Style.RESET_ALL} {self.name:<18} | {status:<14} | Target: {self.target}")
        if self.is_detected and self.details:
            print(f"         └─ {self.details}")