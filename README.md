# 🔍 NetworkScanner

A lightweight network scanner written in Python for discovering live hosts and gathering basic recon information on a network.

![Python](https://img.shields.io/badge/python-3.x-blue)
![Purpose](https://img.shields.io/badge/purpose-pentesting%20%7C%20recon-red)
![License](https://img.shields.io/badge/license-MIT-green)

## 📖 Overview

NetworkScanner discovers devices on a network and reports useful recon details. It was built to practice network reconnaissance for pentesting and bug bounty work.

## ✨ Features

- Discover live hosts on a subnet (e.g. `192.168.1.0/24`)
- Show IP and MAC addresses of connected devices
- <!-- Port scanning / service detection, if implemented -->
- <!-- Hostname resolution, if implemented -->
- <!-- Export results to TXT/CSV/JSON, if implemented -->

## ⚙️ Installation

```bash
git clone https://github.com/shivabalaj/NeteworkScanner.git
cd NeteworkScanner
pip install -r requirements.txt
```

> Some scans (e.g. ARP) need root/admin privileges: use `sudo` on Linux/macOS.

## ▶️ Usage

```bash
python3 scanner.py -t <target>
```

Example:

```bash
sudo python3 scanner.py -t 192.168.1.0/24
```

| Option | Description |
|--------|-------------|
| `-t`, `--target` | Target IP or network range |
| `-h`, `--help` | Show help message |

## 📸 Sample Output

```
IP Address        MAC Address
------------------------------------
192.168.1.1       AA:BB:CC:DD:EE:FF
192.168.1.14      11:22:33:44:55:66
```

## 🗂️ Project Structure

```
NeteworkScanner/
├── scanner.py
├── requirements.txt
└── README.md
```

## 🛠️ Built With

- Python 3
- <!-- scapy / socket / argparse / etc. -->

## 🗺️ Roadmap

- [ ] Port scanning
- [ ] Service/banner detection
- [ ] Multithreading for faster scans
- [ ] Export reports (CSV/JSON)

## ⚠️ Disclaimer

This tool is for **educational purposes and authorized security testing only**. Only scan networks you own or have explicit written permission to test. The author is not responsible for any misuse or damage.

## 👤 Author

**Balaji** · [GitHub](https://github.com/shivabalaj) · [LinkedIn](https://www.linkedin.com/in/balaji-chandrashekar-aeluri-a47a852b7/)

⭐ If you found this useful, consider starring the repo!
