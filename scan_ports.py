import socket


def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set a timeout for the connection attempt
        try:
            s.connect((host, port))
        except socket.error:
            pass  # Connection failed, port is not open
        else:
            open_ports.append(port)
        finally:
            s.close()
    return open_ports


HOST = 'localhost'
START_PORT = 9000
END_PORT = 9100

open_ports = scan_ports(HOST, START_PORT, END_PORT)
if open_ports:
    print(
        f"Open ports on {HOST} in range {START_PORT}-{END_PORT}: {open_ports}")
else:
    print(f"No open ports found on {HOST} in range {START_PORT}-{END_PORT}.")
