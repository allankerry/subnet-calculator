import ipaddress
import sys


def main():
    cidr = sys.argv[1]
    net = ipaddress.ip_network(cidr, strict=False)

    print(f"Network:    {net.network_address}")
    print(f"Mask:       {net.netmask}")
    print(f"Broadcast:  {net.broadcast_address}")
    print(f"First host: {net.network_address + 1}")
    print(f"Last host:  {net.broadcast_address - 1}")
    print(f"Usable:     {net.num_addresses - 2}")


if __name__ == "__main__":
    main()