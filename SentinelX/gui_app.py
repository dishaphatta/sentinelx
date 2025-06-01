import tkinter as tk
import threading
import time
import sentinelx  # Now safe because sentinelx.py doesn’t import this

running_flag = {"running": False}

def start_monitoring():
    if not running_flag["running"]:
        running_flag["running"] = True
        status_label.config(text="🔒 Monitoring started...")
        thread = threading.Thread(target=sentinelx.sentinelx_loop, args=(running_flag,))
        thread.daemon = True
        thread.start()

def stop_monitoring():
    if running_flag["running"]:
        running_flag["running"] = False
        status_label.config(text="🛑 Monitoring stopped.")

# GUI layout
window = tk.Tk()
window.title("SentinelX Controller")
window.geometry("300x200")

tk.Label(window, text="SentinelX Firewall", font=("Helvetica", 16)).pack(pady=10)
tk.Button(window, text="Start Monitoring", command=start_monitoring).pack(pady=5)
tk.Button(window, text="Stop Monitoring", command=stop_monitoring).pack(pady=5)

status_label = tk.Label(window, text="Status: Idle")
status_label.pack(pady=20)

window.mainloop()











# import tkinter as tk
# import threading
# import time
# import sentinelx  # import the monitoring script

# running = False  # flag to control monitoring loop

# def start_monitoring():
#     global running
#     if not running:
#         running = True
#         sentinelx.set_running(True)
#         status_label.config(text="🔒 Monitoring started...")
#         thread = threading.Thread(target=sentinelx.sentinelx_loop)
#         thread.daemon = True
#         thread.start()

# def stop_monitoring():
#     global running
#     if running:
#         running = False
#         sentinelx.set_running(False)
#         status_label.config(text="🛑 Monitoring stopped.")

# # GUI setup
# window = tk.Tk()
# window.title("SentinelX Controller")
# window.geometry("300x200")

# tk.Label(window, text="SentinelX Firewall", font=("Helvetica", 16)).pack(pady=10)

# tk.Button(window, text="Start Monitoring", command=start_monitoring).pack(pady=5)
# tk.Button(window, text="Stop Monitoring", command=stop_monitoring).pack(pady=5)

# status_label = tk.Label(window, text="Status: Idle")
# status_label.pack(pady=20)

# window.mainloop()
