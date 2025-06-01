import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("ABUSE_API_KEY")

def is_ip_malicious(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    params = {"ipAddress": ip, "maxAgeInDays": "7"}
    headers = {"Key": API_KEY, "Accept": "application/json"}

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        score = data["data"]["abuseConfidenceScore"]
        return score, score >= 80
    except:
        return 0, False