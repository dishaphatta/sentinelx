import os

def block_ip(ip):
    print(f"⛔ Blocking IP: {ip}")
    os.system(f'netsh advfirewall firewall add rule name="SentinelX Block {ip}" dir=in action=block remoteip={ip}')