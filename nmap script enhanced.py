import os

# Prompt for the IP to scan
ip = input("Enter the IP you want to scan: ")

# Prompt for the port to discover (optional)
port = input("Enter the port you want to discover (leave blank if you don't want to specify): ")

# Prompt for the scan mode (optional)
modes = input("Enter the mode you want to use (e.g., -sS, -sV, etc., leave blank to use the default mode): ")

# Build the nmap command based on the inputs
if not port:
    # If no port is specified
    if not modes:
        # No mode, only IP
        os.system(f"nmap {ip}")
    else:
        # With mode
        os.system(f"nmap {modes} {ip}")
else:
    # If port is specified
    if not modes:
        # Only port
        os.system(f"nmap -p{port} {ip}")
    else:
        # Port and mode
        os.system(f"nmap -p {port} {modes} {ip}")