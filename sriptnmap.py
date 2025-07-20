import os
ip = input("Enter the IP you want to scan: ")
mode = input("Enter the mode you want to use: ")
port = input("Enter the port you want to discover: ")
os.system(f"sudo nmap -p {port} {mode} {ip}")

