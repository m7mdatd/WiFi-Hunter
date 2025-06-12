#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
WiFi Network Analyzer Tool
أداة تحليل شبكات WiFi المتقدمة
Created for Kali Linux
"""

import subprocess
import re
import json
import time
import sys
import os
from datetime import datetime
import argparse
from collections import defaultdict
import threading

class Colors:
    """ألوان للعرض في Terminal"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

class WiFiAnalyzer:
    def __init__(self):
        self.networks = {}
        self.interface = None
        self.monitor_mode = False
        self.scanning = False
        
    def banner(self):
        """عرض البانر"""
        banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                    WiFi Network Analyzer                     ║
║                   أداة تحليل شبكات WiFi                      ║
║                        Kali Linux Tool                       ║
╚══════════════════════════════════════════════════════════════╝
{Colors.END}
        """
        print(banner)
    
    def check_root(self):
        """فحص صلاحيات الروت"""
        if os.geteuid() != 0:
            print(f"{Colors.RED}[!] يجب تشغيل الأداة بصلاحيات root{Colors.END}")
            print(f"{Colors.YELLOW}[*] استخدم: sudo python3 {sys.argv[0]}{Colors.END}")
            sys.exit(1)
    
    def get_interfaces(self):
        """الحصول على قائمة واجهات الشبكة"""
        interfaces = []
        
        # الطريقة الأولى: iwconfig
        try:
            result = subprocess.run(['iwconfig'], capture_output=True, text=True, stderr=subprocess.DEVNULL)
            for line in result.stdout.split('\n'):
                if 'IEEE 802.11' in line:
                    interface = line.split()[0]
                    interfaces.append(interface)
        except:
            pass
        
        # الطريقة الثانية: البحث في /sys/class/net
        try:
            import glob
            for interface_path in glob.glob('/sys/class/net/*/wireless'):
                interface = interface_path.split('/')[-2]
                if interface not in interfaces:
                    interfaces.append(interface)
        except:
            pass
        
        # الطريقة الثالثة: ip link show
        try:
            result = subprocess.run(['ip', 'link', 'show'], capture_output=True, text=True)
            for line in result.stdout.split('\n'):
                if 'wlan' in line or 'wlp' in line:
                    parts = line.split(':')
                    if len(parts) >= 2:
                        interface = parts[1].strip().split('@')[0]
                        if interface not in interfaces:
                            interfaces.append(interface)
        except:
            pass
        
        return interfaces
    
    def enable_monitor_mode(self, interface):
        """تفعيل وضع المراقبة"""
        print(f"{Colors.YELLOW}[*] تفعيل وضع المراقبة على {interface}...{Colors.END}")
        try:
            # إيقاف الواجهة
            subprocess.run(['airmon-ng', 'check', 'kill'], capture_output=True)
            subprocess.run(['ifconfig', interface, 'down'], capture_output=True)
            
            # تفعيل وضع المراقبة
            subprocess.run(['iwconfig', interface, 'mode', 'monitor'], capture_output=True)
            subprocess.run(['ifconfig', interface, 'up'], capture_output=True)
            
            # فحص الوضع
            result = subprocess.run(['iwconfig', interface], capture_output=True, text=True)
            if 'Mode:Monitor' in result.stdout:
                print(f"{Colors.GREEN}[+] تم تفعيل وضع المراقبة بنجاح{Colors.END}")
                self.monitor_mode = True
                return True
            else:
                print(f"{Colors.RED}[!] فشل في تفعيل وضع المراقبة{Colors.END}")
                return False
        except Exception as e:
            print(f"{Colors.RED}[!] خطأ في تفعيل وضع المراقبة: {e}{Colors.END}")
            return False
    
    def disable_monitor_mode(self, interface):
        """إلغاء وضع المراقبة"""
        try:
            subprocess.run(['ifconfig', interface, 'down'], capture_output=True)
            subprocess.run(['iwconfig', interface, 'mode', 'managed'], capture_output=True)
            subprocess.run(['ifconfig', interface, 'up'], capture_output=True)
            print(f"{Colors.GREEN}[+] تم إلغاء وضع المراقبة{Colors.END}")
            self.monitor_mode = False
        except:
            pass
    
    def scan_networks(self, interface, duration=30):
        """فحص الشبكات"""
        print(f"{Colors.YELLOW}[*] بدء فحص الشبكات لمدة {duration} ثانية...{Colors.END}")
        print(f"{Colors.CYAN}[*] اضغط Ctrl+C لإيقاف الفحص{Colors.END}")
        
        self.scanning = True
        scan_thread = threading.Thread(target=self._scan_worker, args=(interface, duration))
        scan_thread.daemon = True
        scan_thread.start()
        
        try:
            while self.scanning:
                self.display_networks()
                time.sleep(2)
        except KeyboardInterrupt:
            self.scanning = False
            print(f"\n{Colors.YELLOW}[*] إيقاف الفحص...{Colors.END}")
    
    def _scan_worker(self, interface, duration):
        """عامل الفحص في thread منفصل"""
        try:
            cmd = f"timeout {duration} airodump-ng {interface} --write /tmp/scan --output-format csv"
            subprocess.run(cmd, shell=True, capture_output=True)
        except:
            pass
        finally:
            self.scanning = False
            self.parse_airodump_results()
    
    def parse_airodump_results(self):
        """تحليل نتائج airodump"""
        try:
            with open('/tmp/scan-01.csv', 'r', encoding='latin-1') as f:
                content = f.read()
            
            # تحليل الشبكات
            lines = content.split('\n')
            network_section = True
            
            for line in lines:
                if 'Station MAC' in line:
                    network_section = False
                    continue
                
                if network_section and line.strip() and not line.startswith('BSSID'):
                    parts = [p.strip() for p in line.split(',')]
                    if len(parts) >= 14:
                        bssid = parts[0]
                        power = parts[8]
                        essid = parts[13] if parts[13] else '<Hidden>'
                        channel = parts[3]
                        encryption = parts[5]
                        
                        if bssid and bssid != 'BSSID':
                            self.networks[bssid] = {
                                'essid': essid,
                                'channel': channel,
                                'power': power,
                                'encryption': encryption,
                                'first_seen': datetime.now().strftime('%H:%M:%S')
                            }
            
            # حذف ملف مؤقت
            for f in ['/tmp/scan-01.csv', '/tmp/scan-01.cap', '/tmp/scan-01.kismet.csv']:
                if os.path.exists(f):
                    os.remove(f)
                    
        except Exception as e:
            print(f"{Colors.RED}[!] خطأ في تحليل النتائج: {e}{Colors.END}")
    
    def display_networks(self):
        """عرض الشبكات المكتشفة"""
        os.system('clear')
        self.banner()
        
        if not self.networks:
            print(f"{Colors.YELLOW}[*] لا توجد شبكات مكتشفة حتى الآن...{Colors.END}")
            return
        
        print(f"{Colors.BOLD}{'BSSID':<18} {'ESSID':<25} {'CH':<3} {'PWR':<4} {'ENC':<10} {'TIME':<8}{Colors.END}")
        print("=" * 80)
        
        sorted_networks = sorted(self.networks.items(), key=lambda x: int(x[1]['power']) if x[1]['power'].lstrip('-').isdigit() else -100, reverse=True)
        
        for bssid, info in sorted_networks:
            power_color = Colors.GREEN if int(info['power']) > -50 else Colors.YELLOW if int(info['power']) > -70 else Colors.RED
            enc_color = Colors.RED if 'WEP' in info['encryption'] or info['encryption'] == '' else Colors.GREEN
            
            print(f"{Colors.CYAN}{bssid}{Colors.END} {info['essid']:<25} {info['channel']:<3} {power_color}{info['power']:<4}{Colors.END} {enc_color}{info['encryption']:<10}{Colors.END} {info['first_seen']}")
    
    def analyze_security(self):
        """تحليل أمان الشبكات"""
        if not self.networks:
            print(f"{Colors.RED}[!] لا توجد شبكات للتحليل{Colors.END}")
            return
        
        print(f"\n{Colors.BOLD}تحليل الأمان:{Colors.END}")
        print("=" * 50)
        
        vulnerable = 0
        secure = 0
        hidden = 0
        
        for bssid, info in self.networks.items():
            if info['essid'] == '<Hidden>':
                hidden += 1
            elif 'WEP' in info['encryption'] or info['encryption'] == '':
                vulnerable += 1
                print(f"{Colors.RED}[VULNERABLE] {info['essid']} ({bssid}) - {info['encryption']}{Colors.END}")
            else:
                secure += 1
        
        print(f"\n{Colors.GREEN}شبكات آمنة: {secure}{Colors.END}")
        print(f"{Colors.RED}شبكات ضعيفة: {vulnerable}{Colors.END}")
        print(f"{Colors.YELLOW}شبكات مخفية: {hidden}{Colors.END}")
        print(f"{Colors.CYAN}إجمالي الشبكات: {len(self.networks)}{Colors.END}")
    
    def save_results(self, filename):
        """حفظ النتائج"""
        try:
            data = {
                'scan_time': datetime.now().isoformat(),
                'networks': self.networks,
                'total_networks': len(self.networks)
            }
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"{Colors.GREEN}[+] تم حفظ النتائج في {filename}{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}[!] خطأ في حفظ النتائج: {e}{Colors.END}")
    
    def run(self):
        """تشغيل الأداة"""
        try:
            self.banner()
            self.check_root()
            
            # الحصول على واجهات الشبكة
            interfaces = self.get_interfaces()
            if not interfaces:
                print(f"{Colors.RED}[!] لم يتم العثور على واجهات WiFi{Colors.END}")
                print(f"{Colors.YELLOW}[*] نصائح لحل المشكلة:{Colors.END}")
                print(f"  1. تحقق من واجهات الشبكة: {Colors.CYAN}ip link show{Colors.END}")
                print(f"  2. فعل واجهة WiFi: {Colors.CYAN}sudo ip link set wlan0 up{Colors.END}")
                print(f"  3. تثبيت برامج التشغيل: {Colors.CYAN}sudo apt install firmware-iwlwifi{Colors.END}")
                print(f"  4. إعادة تحميل برامج التشغيل: {Colors.CYAN}sudo modprobe -r iwlwifi && sudo modprobe iwlwifi{Colors.END}")
                print(f"  5. استخدم USB WiFi adapter إذا كنت في VM{Colors.END}")
                
                # محاولة عرض واجهات الشبكة الموجودة
                print(f"\n{Colors.CYAN}[*] واجهات الشبكة الموجودة:{Colors.END}")
                try:
                    result = subprocess.run(['ip', 'link', 'show'], capture_output=True, text=True)
                    for line in result.stdout.split('\n'):
                        if ': ' in line and ('wlan' in line or 'wlp' in line or 'enp' in line or 'eth' in line):
                            print(f"  {line.strip()}")
                except:
                    pass
                return
            
            print(f"{Colors.CYAN}[*] واجهات WiFi المتاحة:{Colors.END}")
            for i, iface in enumerate(interfaces):
                print(f"  [{i}] {iface}")
            
            # اختيار الواجهة
            try:
                choice = int(input(f"\n{Colors.YELLOW}اختر رقم الواجهة: {Colors.END}"))
                self.interface = interfaces[choice]
            except (ValueError, IndexError):
                print(f"{Colors.RED}[!] اختيار غير صحيح{Colors.END}")
                return
            
            # تفعيل وضع المراقبة
            if not self.enable_monitor_mode(self.interface):
                return
            
            try:
                # بدء الفحص
                duration = int(input(f"{Colors.YELLOW}مدة الفحص بالثواني (افتراضي 30): {Colors.END}") or "30")
                self.scan_networks(self.interface, duration)
                
                # عرض التحليل
                self.analyze_security()
                
                # حفظ النتائج
                save = input(f"\n{Colors.YELLOW}هل تريد حفظ النتائج؟ (y/n): {Colors.END}").lower()
                if save == 'y':
                    filename = input(f"{Colors.YELLOW}اسم الملف (افتراضي wifi_scan.json): {Colors.END}") or "wifi_scan.json"
                    self.save_results(filename)
                
            finally:
                # إعادة تعيين الواجهة
                self.disable_monitor_mode(self.interface)
                
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}[*] تم إيقاف الأداة{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}[!] خطأ: {e}{Colors.END}")

def main():
    parser = argparse.ArgumentParser(description='أداة تحليل شبكات WiFi المتقدمة')
    parser.add_argument('-i', '--interface', help='واجهة الشبكة')
    parser.add_argument('-t', '--time', type=int, default=30, help='مدة الفحص بالثواني')
    parser.add_argument('-o', '--output', help='ملف حفظ النتائج')
    
    args = parser.parse_args()
    
    analyzer = WiFiAnalyzer()
    
    if args.interface:
        analyzer.interface = args.interface
        analyzer.enable_monitor_mode(args.interface)
        try:
            analyzer.scan_networks(args.interface, args.time)
            analyzer.analyze_security()
            if args.output:
                analyzer.save_results(args.output)
        finally:
            analyzer.disable_monitor_mode(args.interface)
    else:
        analyzer.run()

if __name__ == "__main__":
    main()
