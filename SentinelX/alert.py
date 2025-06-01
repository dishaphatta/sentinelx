import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_ip_alert(ip, score):
    msg = EmailMessage()
    msg['Subject'] = '🚨 SentinelX: Malicious IP Detected'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content(f"""
Malicious IP Detected:

IP Address: {ip}
Abuse Score: {score}

Reply 'yes' in terminal to block.
""")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print(f"[EMAIL SENT] Alert for IP {ip}")
    except Exception as e:
        print(f"[EMAIL ERROR] {e}")
        
def send_honeypot_alert(username):
    msg = EmailMessage()
    msg['Subject'] = '🪤 SentinelX: Honeypot Access Detected'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content(f"""
ALERT: Honeypot File Accessed!

Username: {username}
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

This could be an insider threat or unauthorized access.
""")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print(f"[EMAIL SENT] Honeypot alert for user {username}")
    except Exception as e:
        print(f"[EMAIL ERROR] {e}")

        
# if __name__ == "__main__":
#     send_alert("1.2.3.4", 95)
