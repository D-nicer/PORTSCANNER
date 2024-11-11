import socket

def scan_ports(hostname, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        print(f"Scanning port {port}...")  # Debugging line to show the port being scanned
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Increase timeout to 2 seconds
        result = sock.connect_ex((hostname, port))  # Returns 0 if connection is successful
        if result == 0:
            open_ports.append(port)
            print(f"Port {port} is open")  # If port is open, print it
        else:
            print(f"Port {port} is closed")  # If port is closed, print it
        sock.close()

    return open_ports

# Test the port scan with a small range (e.g., 20-80)
host = '202.158.139.57'  # Localhost
start_port = 21
end_port = 21  # Testing with fewer ports (from port 20 to port 80)
open_ports = scan_ports(host, start_port, end_port)

# Show the open ports found
print(f"Open ports on {host}: {open_ports}")
