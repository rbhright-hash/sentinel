"""
Log Analyzer — Parser log keamanan dan deteksi anomali sederhana.
Untuk forensik digital defensif.
"""
import re
from collections import Counter

class LogAnalyzer:
    def __init__(self, filepath=None):
        self.filepath = filepath
        self.events = []

    def parse_auth_log(self, line):
        # Pola dasar log auth (syslog-style)
        match = re.search(r"Failed password|Accepted password|session opened|session closed", line)
        return match.group(0) if match else "unknown"

    def detect_brute_force(self, events):
        failed = [e for e in events if "Failed" in e]
        ip_counts = Counter(failed)
        # Flag jika > 5 percobaan gagal
        return {ip: c for ip, c in ip_counts.items() if c > 5}

    def analyze_file(self):
        if not self.filepath:
            return {"error": "File tidak ditentukan"}
        with open(self.filepath, "r") as f:
            lines = f.readlines()
        events = [self.parse_auth_log(line) for line in lines]
        brute = self.detect_brute_force(events)
        return {"total_lines": len(lines), "brute_force_detected": brute}

if __name__ == "__main__":
    analyzer = LogAnalyzer()
    # Contoh: analyzer.filepath = "samples/auth.log"
    # print(analyzer.analyze_file())
