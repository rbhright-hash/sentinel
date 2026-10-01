"""
Threat Intelligence — Korelasi OSINT + log untuk laporan defensif.
"""
from datetime import datetime

class ThreatIntel:
    def __init__(self, osint_data, log_analysis):
        self.osint = osint_data
        self.log = log_analysis

    def generate_report(self):
        report = {
            "generated_at": datetime.now().isoformat(),
            "osint_feeds": len(self.osint.get("results", [])),
            "log_anomalies": self.log.get("brute_force_detected", {}),
            "status": "defensive_analysis_complete"
        }
        return report

if __name__ == "__main__":
    sample_osint = {"results": [{"source": "test"}]}
    sample_log = {"brute_force_detected": {}}
    intel = ThreatIntel(sample_osint, sample_log)
    print(intel.generate_report())
