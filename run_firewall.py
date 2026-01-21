from firewall_manager import block_ip, unblock_ip

if __name__ == "__main__":
    test_ip = "192.168.1.100"

    # Simulate blocking IP
    block_ip(test_ip)

    # Simulate removing IP block
    unblock_ip(test_ip)

    # Enforce (real blocking) - only if you are on Linux and root
    # block_ip(test_ip, simulate=False)
