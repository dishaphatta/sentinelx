import time
from datetime import datetime
import getpass
from monitor import get_active_ips
from check_ip import is_ip_malicious
from alert import send_ip_alert, send_honeypot_alert
from blocker import block_ip
from logger import log_to_csv
from gui_notify import notify_popup
from trap import create_trap, trap_triggered

def sentinelx_loop(running_flag):
    checked_ips = set()
    create_trap()
    print(f"🔒 SentinelX Started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    while running_flag["running"]:
        # Check honeypot access
        if trap_triggered():
            user = getpass.getuser()
            print(f"🪤 HONEYPOT ACCESSED by user: {user}")
            send_honeypot_alert(user)
            notify_popup(user)
            log_to_csv(user, 100, "Trap Triggered")

        # Monitor new IPs
        active_ips = get_active_ips()
        new_ips = active_ips - checked_ips
        checked_ips.update(new_ips)

        for ip in new_ips:
            score, bad = is_ip_malicious(ip)

            if not bad:
                print(f"✅ IP {ip} is clean. Score: {score}")
                continue  # skip safe IPs silently

            # If it's malicious:
            print(f"⚠️ IP {ip} is malicious! Abuse Score: {score}")
            send_ip_alert(ip, score)
            notify_popup(ip)
            
            # Automatically log immediately
            log_to_csv(ip, score, "Alerted")

            choice = input(f"Do you want to block {ip}? (yes/no): ")
            if choice.lower() == 'yes':
                block_ip(ip)
                log_to_csv(ip, score, "Blocked")
            else:
                log_to_csv(ip, score, "Ignored")

        time.sleep(15)




# Simulate a malicious IP test
send_ip_alert("185.234.219.65", 90)


