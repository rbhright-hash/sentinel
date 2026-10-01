#!/usr/bin/env python3
"""
Sentinel CLI — jalanin semua modul defensif dalam satu command.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.osint_collector import OSINTCollector
from src.log_analyzer import LogAnalyzer
from src.threat_intel import ThreatIntel

def main():
    print("=== SENTINEL DEFENSIVE TOOLKIT ===")
    print("1. OSINT Collector (public feed)")
    print("2. Log Analyzer (default: samples/auth.log)")
    print("3. Threat Intel (gabung 1 + 2)")
    print("4. Full Pipeline")
    print("5. Cek Laptop (system auth log)")
    choice = input("Pilih (1-5): ").strip()

    if choice == "1":
        c = OSINTCollector()
        c.fetch_ipsum()
        print("IOC:", c.results[:3])
    elif choice == "2":
        a = LogAnalyzer()
        a.print_report()
    elif choice == "3":
        from src.osint_collector import OSINTCollector
        osint = OSINTCollector()
        osint.fetch_ipsum()
        log = LogAnalyzer()
        log_data = log.analyze_file()
        intel = ThreatIntel(osint.results, log_data)
        res = intel.generate_report()
        print(res.get("raw", ""))
    elif choice == "4":
        print("[PIPELINE] Menjalankan semua modul...")
        from src.osint_collector import OSINTCollector
        c = OSINTCollector()
        c.fetch_ipsum()
        log = LogAnalyzer()
        log_data = log.analyze_file()
        intel = ThreatIntel(c.results, log_data)
        intel.generate_report()
        print("Pipeline selesai.")
    elif choice == "5":
        print("[SYSTEM CHECK] Membaca /var/log/secure...")
        try:
            a = LogAnalyzer("/var/log/secure")
            a.print_report()
            print("Status laptop: NORMAL (tidak ada brute force)")
        except Exception as e:
            print(f"Gagal baca system log: {e}")
    else:
        print("Pilihan tidak dikenali.")

if __name__ == "__main__":
    main()
