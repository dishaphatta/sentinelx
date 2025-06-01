# 🛡️ SentinelX – Self-Aware AI-Driven Threat Detection & Deception System

**SentinelX** is an intelligent Blue Team cybersecurity application designed to monitor full-device activity, detect threats in real-time, deploy honeypots, and respond to suspicious behaviors with alerts and human-approved automation.

It combines threat intelligence (AbuseIPDB), deception techniques, and behavioral profiling ("Digital DNA") to protect endpoints and networks against external attacks and insider threats — all powered by **free and open-source tools**.

---

## 🔥 Key Features

- 🔍 Detects suspicious/malicious IPs using AbuseIPDB
- 🧬 Generates “Digital DNA” profiles and tracks behavioral deviations
- 🪤 Deploys honeypot trap files to catch insider threats
- 📧 Sends real-time alerts via email and desktop popups
- 🔐 Blocks malicious IPs through Windows Firewall after user approval
- 🧾 Logs all activity to CSV for audits
- 🖥️ Comes with an easy-to-use GUI
- 📦 Built fully with free, open-source tools and APIs

---

## 📦 Project Structure

SentinelX/
├── gui_app.py         # GUI controller to start/stop monitoring
├── sentinelx.py       # Main logic and monitoring loop
├── monitor.py         # Gets active IPs from connections
├── check_ip.py        # Checks IP reputation via AbuseIPDB
├── alert.py           # Sends email alerts for IP and trap activity
├── blocker.py         # Blocks malicious IPs via Windows firewall
├── firewall.py        # (alt) Block script using netsh
├── trap.py            # Creates + detects access to honeypot file
├── gui_notify.py      # GUI alert popups for detection
├── logger.py          # Logs activity to CSV
├── requirements.txt   # Python package dependencies
├── alert_log.csv      # Output file for threat and response logs
├── gui_app.exe        # (Optional) Compiled Windows executable
├── .env               # Environment config (email & API keys)
└── gui_app.spec       # PyInstaller spec file for .exe builds

---

## 🔧 Requirements

- 🪟 Windows OS (tested on Windows 10/11)
- 🐍 Python 3.8+
- 📩 Gmail SMTP (or any SMTP account for alerts)
- 🌐 AbuseIPDB API key (free)

---

## 📥 Installation

Step 1: Clone the Repository
git clone https://github.com/yourusername/sentinelx.git
cd sentinelx

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Create .env File
Create a .env file in the root directory with the following format:
.env
EMAIL_ADDRESS=youremail@gmail.com
EMAIL_PASSWORD=your_app_password
ABUSE_API_KEY=your_abuseipdb_key

⚠️ Use a Gmail App Password, not your main password.
Get a free AbuseIPDB API key here: https://www.abuseipdb.com/

---

## 🖥️ Running the Application
Option 1: Run with Python
python gui_app.py

Option 2: Run the EXE
If you’ve compiled the app with PyInstaller, simply double-click gui_app.exe.

---

## 🧪 How It Works

🔍 IP Monitoring
- Collects active remote IP connections using psutil
- Calls AbuseIPDB to check reputation
- If score ≥ 80 → sends GUI + email alert
- User approves via prompt → IP is blocked using Windows firewall

🪤 Honeypot Monitoring

Creates a fake file: Passwords.txt
If accessed → triggers insider threat alert
Emails and logs the username and timestamp

📧 Alert Example

Subject: 🚨 SentinelX: Malicious IP Detected
IP Address: 185.234.219.65
Abuse Score: 90
Do you want to block this IP?

---

## 🧾 Logs and Reporting

All events are logged into alert_log.csv in this format:
IP,Score,Status
185.234.219.65,90,Blocked
192.168.1.33,100,Trap Triggered
8.8.8.8,45,Ignored

---

## 🧰 Technologies Used

Area	Tool/Library
GUI	Tkinter
Network Analysis	psutil
Threat Intelligence	AbuseIPDB (free API)
Email Alerts	smtplib + Gmail SMTP
File Traps	os, getpass
Popup Alerts	tkinter (popup)
IP Blocking	netsh (Windows)
Logging	csv
Secure Config	python-dotenv

---

## 📌 Security Notes

✅ Does not install agents or modify kernel/network layers
✅ All scanning and blocking is user-approved
✅ No sensitive data is collected
✅ Only local files + AbuseIPDB API used

---

## 📜 License
This project is licensed under the MIT License.
Free to use, modify, and distribute for educational or security use.
