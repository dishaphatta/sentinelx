import psutil

def get_active_ips():
    active_ips = set()
    for conn in psutil.net_connections(kind='inet'):
        if conn.raddr:
            active_ips.add(conn.raddr.ip)
    return active_ips