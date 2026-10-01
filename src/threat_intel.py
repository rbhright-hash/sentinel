"""
Threat Intelligence — Korelasi OSINT + log untuk laporan defensif.
"""
from datetime import datetime

class ThreatIntel:
    def __init__(self, osint_data=None, log_analysis=None):
        self.osint = osint_data or {}
        # Jika data datang sebagai list (dari OSINTCollector.results), bungkus
        if isinstance(self.osint, list):
            self.osint = {"results": self.osint}
        self.log = log_analysis or {}

    def generate_report(self, output_path="docs/threat_report.txt"):
        osint_count = len(self.osint.get("results", [])) if isinstance(self.osint.get("results"), list) else 0
        brute = self.log.get("brute_force_detected", {}) if isinstance(self.log.get("brute_force_detected"), dict) else {}
        status = "HIGH_RISK" if brute else "NORMAL"

        report_lines = [
            "=== SENTINEL THREAT INTELLIGENCE REPORT ===",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Status   : {status}",
            "",
            "--- OSINT FEED SUMMARY ---",
            f"IOC Count: {osint_count}",
            f"Sample IOC: {self.osint.get('results', [{}])[0].get('value', 'N/A') if self.osint.get('results') else 'N/A'}",
            "",
            "--- LOG ANOMALY SUMMARY ---",
            f"Brute Force IPs: {brute}",
            f"Failed Attempts: {self.log.get('failed_attempts', 'N/A')}",
            f"Total Events  : {self.log.get('total_events', 'N/A')}",
            "",
            "--- RECOMMENDATION ---",
            "Jika brute_force_detected > 0: blokir IP terkait, audit kebijakan autentikasi.",
            "Jika IOC terdeteksi: verifikasi terhadap infrastruktur internal.",
            "",
        ]
        report_text = "\n".join(report_lines)
        try:
            with open(output_path, "w") as f:
                f.write(report_text)
            print(f"[THREAT-INTEL] Laporan disimpan ke: {output_path}")
        except Exception as e:
            print(f"[THREAT-INTEL] Gagal simpan laporan: {e}")
        return {"status": status, "brute": brute, "osint_count": osint_count, "report_path": output_path, "raw": report_text}

if __name__ == "__main__":
    from src.osint_collector import OSINTCollector
    from src.log_analyzer import LogAnalyzer
    osint = OSINTCollector()
    osint.fetch_ipsum()
    log = LogAnalyzer()
    log_data = log.analyze_file()
    intel = ThreatIntel(osint.results, log_data)
    result = intel.generate_report()
    print(result["raw"])
