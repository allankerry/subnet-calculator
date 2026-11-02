def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <ip/prefix>  e.g. 192.168.1.10/24")
        return
    try:
        net = ipaddress.ip_network(sys.argv[1], strict=False)
    except ValueError:
        print("Invalid address. Example: 192.168.1.10/24")
        return

    print(f"Network:    {net.network_address}")
    print(f"Mask:       {net.netmask}")
    print(f"Broadcast:  {net.broadcast_address}")
    print(f"First host: {net.network_address + 1}")
    print(f"Last host:  {net.broadcast_address - 1}")
    print(f"Usable:     {net.num_addresses - 2}")