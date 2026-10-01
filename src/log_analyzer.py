"""
Log Analyzer — Parser log autentikasi dan deteksi brute force.
"""
import re
from collections import Counter
from datetime import datetime

class LogAnalyzer:
    def __init__(self, filepath="samples/auth.log"):
        self.filepath = filepath
        self.events = []
        self.summary = {}

    def parse_line(self, line):
        ip_match = re.search(r"from ([\d\.]+)", line)
        status_match = re.search(r"Failed password|Accepted password|session (opened|closed)", line)
        ip = ip_match.group(1) if ip_match else "unknown"
        status = status_match.group(0) if status_match else "unknown"
        return {"ip": ip, "status": status, "raw": line.strip()}

    def analyze_file(self):
        try:
            with open(self.filepath, "r") as f:
                lines = f.read().splitlines()
        except FileNotFoundError:
            return {"error": f"File tidak ditemukan: {self.filepath}"}

        events = [self.parse_line(line) for line in lines if line.strip()]
        failed_events = [e for e in events if "Failed" in e["status"]]
        failed_by_ip = Counter([e["ip"] for e in failed_events])
        brute = {ip: count for ip, count in failed_by_ip.items() if count >= 3}

        self.events = events
        self.summary = {
            "file": self.filepath,
            "analyzed_at": datetime.now().isoformat(),
            "total_events": len(events),
            "failed_attempts": len(failed_events),
            "unique_failed_ips": len(failed_by_ip),
            "brute_force_detected": brute,
            "sample_failed_ips": list(failed_by_ip.keys())[:5]
        }
        return self.summary

    def print_report(self):
        res = self.analyze_file()
        if "error" in res:
            print(res)
            return
        print(f"=== Log Analysis Report ===")
        print(f"File      : {res['file']}")
        print(f"Events    : {res['total_events']}")
        print(f"Failed    : {res['failed_attempts']} dari {res['unique_failed_ips']} IP unik")
        print(f"Brute     : {res['brute_force_detected']}")
        print(f"IP contoh : {res['sample_failed_ips']}")

if __name__ == "__main__":
    analyzer = LogAnalyzer()
    analyzer.print_report()
