import csv
import os

def log_to_csv(ip, score, status):
    file_exists = os.path.isfile("alert_log.csv")
    with open("alert_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["IP", "Score", "Status"])
        writer.writerow([ip, score, status])
        
        
#         # Test this function directly
# if __name__ == "__main__":
#     log_to_csv("111.222.111.222", 99, "Blocked")