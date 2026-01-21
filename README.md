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

## 🔹 Architecture Diagram

```mermaid
flowchart LR
    A[User Request] --> B[FirewallManager]
    B -->|simulate=True| C[Print Simulation Result]
    B -->|simulate=False| D[Linux Firewall (iptables/NACL)]
    B --> E[Logs: blocked_ips.json]
    E --> F[Dashboard: visualize blocked IPs]
    A --> F
