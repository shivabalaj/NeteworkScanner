import socket
import subprocess
import platform
import ipaddress
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

# -------- Host Discovery --------
def is_host_alive(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", str(ip)]
    result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

# -------- Port Scanning --------
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((str(ip), port))
            if result == 0:
                return port
    except:
        pass
    return None

def scan_ports(ip, ports):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in ports]
        for future in as_completed(futures):
            port = future.result()
            if port:
                open_ports.append(port)
    return open_ports

# -------- Main Function --------
def main():
    parser = argparse.ArgumentParser(description="Simple Python Network Scanner")
    parser.add_argument("-n", "--network", help="Target network/subnet (e.g. 192.168.1.0/24)", required=True)
    parser.add_argument("-p", "--ports", help="Comma-separated ports to scan (default common ports)", default="21,22,23,25,53,80,110,139,143,443,445,8080")
    args = parser.parse_args()

    subnet = ipaddress.ip_network(args.network, strict=False)
    ports_to_scan = [int(p.strip()) for p in args.ports.split(",")]

    print(f"\n🔍 Scanning network: {subnet}")
    print("📡 Discovering live hosts...\n")

    live_hosts = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(is_host_alive, ip): ip for ip in subnet.hosts()}
        for future in as_completed(futures):
            ip = futures[future]
            if future.result():
                print(f"[+] Host up: {ip}")
                live_hosts.append(ip)

    print("\n🚪 Starting port scan...\n")
    for host in live_hosts:
        print(f"[+] Scanning {host}...")
        open_ports = scan_ports(host, ports_to_scan)
        if open_ports:
            print(f"    Open ports: {open_ports}")
        else:
            print("    No open ports found.")

if __name__ == "__main__":
    main()
