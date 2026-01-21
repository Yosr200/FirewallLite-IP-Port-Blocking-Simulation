# FirewallLite – IP & Port Blocking Simulation

FirewallLite is a **Python-based simulation platform** for learning and testing network-level security actions.  
It allows you to **simulate or enforce IP and port blocking**, log blocked attempts, and visualize activity through a dashboard.

---

## 🔹 Features

- Block/unblock IP addresses safely (**simulation mode by default**)  
- Optional enforcement with Linux **iptables** or simulated NACL rules  
- Logs blocked attempts to a JSON file (`logs/blocked_ips.json`)  
- Optional **Flask dashboard** to visualize active rules and blocked IPs  
- Safe-by-default design prevents accidental server lockouts  

---
## 🔹Dashboard View (Mock Table)
| IP Address    | Port | Status    | Timestamp        |
| ------------- | ---- | --------- | ---------------- |
| 192.168.1.100 | ALL  | Simulated | 2026-01-21 12:00 |
| 10.0.0.50     | 22   | Enforced  | 2026-01-21 12:05 |
| 172.16.0.20   | 80   | Simulated | 2026-01-21 12:10 |

## 🔹Dashboard Screenshot
dashboard/dashboard.png
## 🔹 Architecture Diagram

```mermaid
flowchart LR
    A[User Request] --> B[FirewallManager]
    B -->|simulate=True| C[Print Simulation Result]
    B -->|simulate=False| D[Linux Firewall ]
    B --> E[Logs: blocked_ips.json]
    E --> F[Dashboard: visualize blocked IPs]
    A --> F
