import socket
import ipaddress

banner = """
+-------------------------------------+
|                                     |
|       P O R T   S C A N N E R       |
|                                     |
+-------------------------------------+
|  A Simple Tool to Scan Open Ports   |
+-------------------------------------+
"""
print(banner)

open_ports = []

ip_to_scan = input("Enter IP address: ")
try:
    ip_obj = ipaddress.ip_address(ip_to_scan)
    print("You entered a valid IP address.")
except ValueError:
    print("You entered an invalid IP address.")
    exit()

ports_input = input("Enter the range of ports you want to scan (start-end): ")
try:
    ports = [int(port) for port in ports_input.split("-")]
except ValueError:
    print("Invalid input for ports.")
    exit()

for i in range(min(ports), max(ports) + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip_to_scan, i))
        open_ports.append(i)  
        s.close()
    except (socket.timeout, socket.error):
        pass

if open_ports:
    for port in open_ports:
        try:
            service = socket.getservbyport(port)
            print(f"Port {port} is open on {ip_to_scan} and running {service}.")
        except OSError:
            print(f"Port {port} is open on {ip_to_scan}.")
else:
    print(f"No open ports found on {ip_to_scan}.")
