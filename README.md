# 🎯 WiFi-Hunter
## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Examples](#-examples)
- [Contributing](#-contributing)
- [License](#-license)
- [Disclaimer](#-disclaimer)

---

## 🎯 Overview

**WiFi-Hunter** is an advanced wireless network reconnaissance tool designed specifically for penetration testers, security researchers, and network administrators. Built for Kali Linux, it provides comprehensive WiFi network analysis with real-time monitoring capabilities, security assessment, and detailed reporting features.

The tool leverages the power of `aircrack-ng` suite and provides an intuitive interface for wireless network discovery and analysis, making it an essential tool for wireless security auditing.

---

## ✨ Features

### 🔍 **Advanced Network Discovery**
- Real-time WiFi network scanning and monitoring
- Comprehensive network information gathering (BSSID, ESSID, Channel, Signal Strength, Encryption)
- Support for hidden network detection
- Signal strength-based network sorting

### 🛡️ **Security Analysis**
- Automated security assessment of discovered networks
- Vulnerability identification (WEP, Open networks)
- Encryption type analysis and reporting
- Security statistics and recommendations

### 🎨 **User-Friendly Interface**
- Color-coded output for easy network categorization
- Real-time network table updates
- Clean and organized terminal display
- Progress indicators and status messages

### 💾 **Data Management**
- JSON export functionality for discovered networks
- Time-stamped network records
- Detailed network metadata storage
- Support for batch analysis

### ⚙️ **Advanced Configuration**
- Automatic wireless interface detection
- Monitor mode management
- Customizable scan duration
- Command-line parameter support

---

## 📋 Requirements

### System Requirements
- **Operating System**: Kali Linux (recommended) or any Debian-based distribution
- **Python Version**: Python 3.8 or higher
- **Root Privileges**: Required for monitor mode operations

### Dependencies
- `aircrack-ng` suite
- `wireless-tools`
- `net-tools`
- Python standard libraries

### Hardware Requirements
- WiFi adapter with monitor mode support
- Recommended: External USB WiFi adapter for better range

---

## 🚀 Installation
### Quick Installation

```bash
# Clone the repository
git clone https://github.com/m7mdatd/wifi-hunter.git

# Navigate to the directory
cd wifi-hunter

# Make the script executable
chmod +x wifi_hunter.py

# Install dependencies (if needed)
sudo apt update
sudo apt install aircrack-ng wireless-tools net-tools
```

### Manual Installation
1. Download the `wifi_hunter.py` script
2. Place it in your preferred directory (e.g., `/opt/wifi-hunter/`)
3. Make it executable: `chmod +x wifi_hunter.py`
4. Ensure all dependencies are installed

---

## 🎮 Usage
### Basic Usage

```bash
# Run with interactive mode
sudo python3 wifi_hunter.py

# Specify interface and scan duration
sudo python3 wifi_hunter.py -i wlan0 -t 60

# Save results to file
sudo python3 wifi_hunter.py -i wlan0 -t 30 -o scan_results.json
```

### Command Line Options
```bash
Usage: wifi_hunter.py [OPTIONS]

Options:
  -i, --interface INTERFACE    Specify wireless interface
  -t, --time DURATION         Scan duration in seconds (default: 30)
  -o, --output FILENAME       Output file for results
  -h, --help                  Show help message
```

### Interactive Mode
When run without parameters, WiFi-Hunter will:
1. Display available wireless interfaces
2. Allow you to select the interface
3. Automatically enable monitor mode
4. Start real-time network scanning
5. Provide security analysis
6. Offer to save results

---

## 💡 Examples
### Example 1: Quick Scan
```bash
sudo python3 wifi_hunter.py -i wlan0 -t 30
```

### Example 2: Extended Monitoring
```bash
sudo python3 wifi_hunter.py -i wlan1 -t 300 -o detailed_scan.json
```

### Example 3: Interactive Mode
```bash
sudo python3 wifi_hunter.py
# Follow the interactive prompts
```

---

## 📸 Screenshots

### Main Interface
```
╔══════════════════════════════════════════════════════════════╗
║                    WiFi Network Analyzer                     ║
║                        WiFi-Hunter                           ║
║                        Kali Linux Tool                       ║
╚══════════════════════════════════════════════════════════════╝

BSSID              ESSID                     CH PWR ENC        TIME    
================================================================================
AA:BB:CC:DD:EE:FF  MyWiFiNetwork            6  -45 WPA2       14:30:15
11:22:33:44:55:66  <Hidden>                 11 -67 WPA2       14:30:16
FF:EE:DD:CC:BB:AA  OpenNetwork              1  -72 Open       14:30:17
```

### Security Analysis
```
Security Analysis:
==================================================
[VULNERABLE] OpenNetwork (FF:EE:DD:CC:BB:AA) - Open
[VULNERABLE] OldRouter (AA:11:BB:22:CC:33) - WEP

Secure networks: 15
Vulnerable networks: 2
Hidden networks: 3
Total networks: 20
```

---

## 🤝 Contributing
We welcome contributions to WiFi-Hunter! Here's how you can help:
### Ways to Contribute
- 🐛 Report bugs and issues
- 💡 Suggest new features
- 📝 Improve documentation
- 🔧 Submit pull requests

### Development Setup
```bash
git clone https://github.com/m7mdatd/wifi-hunter.git
cd wifi-hunter
# Make your changes
# Test thoroughly
# Submit a pull request
```

### Contribution Guidelines
- Follow Python PEP 8 style guidelines
- Add comments for complex code sections
- Test on multiple wireless adapters
- Update documentation as needed

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 m7mdatd

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## ⚠️ Disclaimer
**WiFi-Hunter** is designed for educational purposes and authorized security testing only. Users are responsible for complying with all applicable laws and regulations. The developers assume no liability for misuse of this tool.
### Legal Notice
- Only use on networks you own or have explicit permission to test
- Respect privacy and legal boundaries
- Follow responsible disclosure practices
- Comply with local and international laws

---

## 📞 Support
### Getting Help
- 📖 Check the documentation
- 🐛 Report issues on GitHub: https://github.com/m7mdatd/wifi-hunter/issues
- 💬 Follow us on X: [@m7mdatd](https://x.com/m7mdatd)
- 📧 Contact: m@twal.sa

### Troubleshooting
- Ensure your WiFi adapter supports monitor mode
- Run with root privileges
- Check that all dependencies are installed
- Verify Kali Linux compatibility

---

## 🎖️ Acknowledgments
- Thanks to the `aircrack-ng` team for their excellent tools
- Kali Linux community for testing and feedback
- All contributors and users who help improve WiFi-Hunter

**Author**: [m7mdatd](https://github.com/m7mdatd)  
**Contact**: m@twal.sa  
**X/Twitter**: [@m7mdatd](https://x.com/m7mdatd)

---

<div align="center">

**Made with ❤️ for the cybersecurity community**
[⭐ Star this project](https://github.com/m7mdatd/wifi-hunter) | [🍴 Fork it](https://github.com/m7mdatd/wifi-hunter/fork) | [📝 Report Issues](https://github.com/m7mdatd/wifi-hunter/issues)

</div>
