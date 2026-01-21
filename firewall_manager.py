import json
import os

LOG_FILE = "logs/blocked_ips.json"

def load_logs():
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_logs(logs):
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

def block_ip(ip, port=None, simulate=True):
    """
    Block an IP (optionally on a port). Safe by default.
    """
    if simulate:
        print(f"[SIMULATION] Would block IP {ip} on port {port or 'ALL'}")
    else:
        cmd = f"iptables -A INPUT -s {ip}"
        if port:
            cmd += f" -p tcp --dport {port}"
        cmd += " -j DROP"
        os.system(cmd)
        print(f"[ENFORCED] IP {ip} blocked on port {port or 'ALL'}")

    # Save log
    logs = load_logs()
    logs.append({"ip": ip, "port": port, "simulated": simulate})
    save_logs(logs)

def unblock_ip(ip, port=None, simulate=True):
    """
    Remove a block from an IP (optional port).
    """
    if simulate:
        print(f"[SIMULATION] Would remove block for IP {ip} on port {port or 'ALL'}")
    else:
        cmd = f"iptables -D INPUT -s {ip}"
        if port:
            cmd += f" -p tcp --dport {port}"
        cmd += " -j DROP"
        os.system(cmd)
        print(f"[ENFORCED] Removed block for IP {ip} on port {port or 'ALL'}")
