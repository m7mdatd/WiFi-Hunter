# 🎯 WiFi-Hunter

<div align="center">

![WiFi-Hunter Logo](https://img.shields.io/badge/WiFi-Hunter-blue?style=for-the-badge&logo=wifi&logoColor=white)

**Advanced WiFi Network Analysis & Reconnaissance Tool for Kali Linux**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-red.svg)](https://kali.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

*A powerful and comprehensive WiFi network scanner and analyzer with real-time monitoring capabilities*

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Examples](#-examples)
- [Screenshots](#-screenshots)
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

### Method 1: From GitHub (Recommended)

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install aircrack-ng wireless-tools net-tools python3 python3-pip git -y

# Clone the repository
git clone https://github.com/m7mdatd/WiFi-Hunter.git

# Navigate to the directory
cd WiFi-Hunter

# Make the script executable
chmod +x wifi_analyzer.py

# Create symbolic link for easy access (optional)
sudo ln -s $(pwd)/wifi_analyzer.py /usr/local/bin/wifi-hunter
```

### Method 2: Direct Download

```bash
# Create directory for the tool
mkdir -p ~/tools/wifi-hunter
cd ~/tools/wifi-hunter

# Download the script directly
wget https://raw.githubusercontent.com/m7mdatd/WiFi-Hunter/main/wifi_analyzer.py

# Make it executable
chmod +x wifi_analyzer.py
```

### Verify Installation

```bash
# Check wireless interfaces
iwconfig

# Test the tool
sudo python3 wifi_analyzer.py --help
```

---

## 🎮 Usage

### Basic Usage

```bash
# Interactive mode (recommended for beginners)
sudo python3 wifi_analyzer.py

# With specific interface
sudo python3 wifi_analyzer.py -i wlan0

# Specify interface and scan duration
sudo python3 wifi_analyzer.py -i wlan0 -t 60

# Save results to file
sudo python3 wifi_analyzer.py -i wlan0 -t 30 -o scan_results.json

# Using symbolic link (if created)
sudo wifi-hunter
```

### Command Line Options

```bash
Usage: wifi_analyzer.py [OPTIONS]

Options:
  -i, --interface INTERFACE    Specify wireless interface
  -t, --time DURATION         Scan duration in seconds (default: 30)
  -o, --output FILENAME       Output file for results
  -h, --help                  Show help message
```

### Step-by-Step Usage Guide

#### 1. Check Available WiFi Interfaces
```bash
# List wireless interfaces
iwconfig

# Or use ip command
ip link show
```

#### 2. Run WiFi-Hunter
```bash
cd WiFi-Hunter
sudo python3 wifi_analyzer.py
```

#### 3. Interactive Mode Process
1. **Select Interface**: Choose from available WiFi interfaces (e.g., wlan0)
2. **Set Duration**: Enter scan duration in seconds (default: 30)
3. **Monitor Networks**: Real-time network discovery and analysis
4. **Stop Scanning**: Press `Ctrl+C` to stop
5. **Security Analysis**: Review vulnerability assessment
6. **Save Results**: Optionally save scan results to JSON file

#### 4. Understanding the Output

```
BSSID              ESSID                     CH PWR ENC        TIME    
================================================================================
AA:BB:CC:DD:EE:FF  MyWiFiNetwork            6  -45 WPA2       14:30:15
11:22:33:44:55:66  <Hidden>                 11 -67 WPA2       14:30:16
FF:EE:DD:CC:BB:AA  OpenNetwork              1  -72 Open       14:30:17
```

- **BSSID**: MAC address of the access point
- **ESSID**: Network name (SSID)
- **CH**: WiFi channel
- **PWR**: Signal strength (dBm)
- **ENC**: Encryption type
- **TIME**: Discovery time

---

## 💡 Examples

### Example 1: Quick Scan
```bash
sudo python3 wifi_analyzer.py -i wlan0 -t 30
```

### Example 2: Extended Monitoring with Results
```bash
sudo python3 wifi_analyzer.py -i wlan1 -t 300 -o detailed_scan_$(date +%Y%m%d_%H%M%S).json
```

### Example 3: Interactive Mode (Recommended for Beginners)
```bash
sudo python3 wifi_analyzer.py
# Follow the interactive prompts:
# 1. Select wireless interface
# 2. Set scan duration
# 3. Monitor real-time results
# 4. Save results if needed
```

### Example 4: Using Symbolic Link
```bash
sudo wifi-hunter -i wlan0 -t 60 -o my_scan.json
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
git clone https://github.com/m7mdatd/WiFi-Hunter.git
cd WiFi-Hunter
# Make your changes
# Test thoroughly on different wireless adapters
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
- **Only use on networks you own or have explicit permission to test**
- **Respect privacy and legal boundaries**
- **Follow responsible disclosure practices**  
- **Comply with local and international laws**

### Important Tips for Best Results
- Use an external USB WiFi adapter for better range and compatibility
- Ensure you're in an area with multiple WiFi networks for comprehensive testing
- Run longer scans (60+ seconds) for more accurate results
- Stop other network services that might interfere: `sudo systemctl stop NetworkManager`

### Advanced Usage Tips
```bash
# Long scan with detailed logging
sudo python3 wifi_analyzer.py -i wlan0 -t 300 -o detailed_scan_$(date +%Y%m%d_%H%M%S).json

# Quick vulnerability assessment
sudo python3 wifi_analyzer.py -i wlan0 -t 10

# Monitor specific area for extended period
sudo python3 wifi_analyzer.py -i wlan0 -t 1800  # 30 minutes
```

---

## 📞 Support

### Getting Help
- 📖 Check the documentation
- 🐛 Report issues on GitHub: https://github.com/m7mdatd/wifi-hunter/issues
- 💬 Follow us on X: [@m7mdatd](https://x.com/m7mdatd)
- 📧 Contact: m@twal.sa

### Troubleshooting
- Ensure your WiFi adapter supports monitor mode
- Run with root privileges: `sudo python3 wifi_analyzer.py`
- Check that all dependencies are installed: `sudo apt install aircrack-ng wireless-tools net-tools`
- Verify Kali Linux compatibility

### Common Issues and Solutions

#### Issue 1: No WiFi Interfaces Found
```bash
# Check drivers
lsusb
lspci | grep -i network

# Reload WiFi drivers
sudo modprobe -r iwlwifi
sudo modprobe iwlwifi
```

#### Issue 2: Monitor Mode Failed
```bash
# Stop NetworkManager
sudo systemctl stop NetworkManager

# Kill interfering processes
sudo airmon-ng check kill

# Manual monitor mode activation
sudo ip link set wlan0 down
sudo iw wlan0 set type monitor
sudo ip link set wlan0 up
```

#### Issue 3: Permission Denied
```bash
# Ensure running as root
sudo su
python3 wifi_analyzer.py

# Or check file permissions
chmod +x wifi_analyzer.py
```

#### Issue 4: Missing Dependencies
```bash
# Install all required packages
sudo apt update
sudo apt install aircrack-ng wireless-tools net-tools python3 python3-pip git -y
```

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

[⭐ Star this project](https://github.com/m7mdatd/WiFi-Hunter) | [🍴 Fork it](https://github.com/m7mdatd/WiFi-Hunter/fork) | [📝 Report Issues](https://github.com/m7mdatd/WiFi-Hunter/issues)

</div>
