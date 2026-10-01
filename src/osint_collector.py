"""
OSINT Collector — Aggregator IOC publik. Mengambil feed IP berbahaya publik (ipsum).
"""
import requests
from datetime import datetime

IPSUM_URL = "https://raw.githubusercontent.com/stamparm/ipsum/master/levels/1.txt"

class OSINTCollector:
    def __init__(self):
        self.results = []

    def fetch_ipsum(self):
        try:
            r = requests.get(IPSUM_URL, timeout=15)
            r.raise_for_status()
            ips = [line.strip() for line in r.text.splitlines() if line.strip() and not line.startswith("#")]
            self.results = [{"type": "ip", "value": ip, "source": "ipsum_level1", "timestamp": datetime.now().isoformat()} for ip in ips[:50]]  # batasi 50 untuk demo
            print(f"[OSINT] {len(self.results)} IOC berhasil dikumpulkan dari ipsum.")
        except Exception as e:
            print(f"[OSINT] Gagal fetch feed publik: {e}")
            # Fallback: baca dari file lokal jika offline
            try:
                with open("samples/ioc_feed.txt", "r") as f:
                    lines = [l.strip() for l in f if l.strip() and not l.startswith("#")]
                self.results = [{"type": "ip", "value": line, "source": "local_fallback", "timestamp": datetime.now().isoformat()} for line in lines]
                print(f"[OSINT] Fallback lokal: {len(self.results)} IOC.")
            except FileNotFoundError:
                print("[OSINT] Tidak ada feed lokal. Buat samples/ioc_feed.txt.")
        return self.results

if __name__ == "__main__":
    collector = OSINTCollector()
    collector.fetch_ipsum()
    print(f"Contoh IOC: {collector.results[:3]}")
