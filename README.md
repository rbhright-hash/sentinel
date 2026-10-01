# Sentinel — OSINT + Log Forensics Toolkit

Toolkit defensif berbasis Python untuk analisis data terbuka (OSINT) dan forensik log keamanan. Dibuat untuk portofolio profesional di bidang siber defensif.

## Modul Defensif
- `osint_collector`: Agregasi IOC publik (`ipsum`)
- `log_analyzer`: Parser log autentikasi + deteksi brute force
- `threat_intel`: Korelasi OSINT + log → laporan defensif

## Install
```bash
git clone https://github.com/rbhright-hash/sentinel.git
cd sentinel
pip install -r requirements.txt
# atau install sebagai package:
pip install .
```

## Cara Jalanin
```bash
# CLI interaktif (paling mudah)
python src/cli.py

# Atau jalankan modul satu per satu
python -m src.osint_collector
python -m src.log_analyzer
python -m src.threat_intel

# Cek laptop sendiri (butuh sudo untuk /var/log/secure)
sudo python -c "from src.log_analyzer import LogAnalyzer; LogAnalyzer('/var/log/secure').print_report()"
```

## Catatan Etis
- Hanya membaca feed publik dan log lokal
- Tidak melakukan eksploitasi, akses ilegal, atau serangan
- Semua modul defensif untuk audit dan analisis ancaman
