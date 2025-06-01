import tkinter as tk

def notify_popup(ip):
    win = tk.Tk()
    win.title("SentinelX Alert")
    win.geometry("300x100")
    label = tk.Label(win, text=f"⚠️ Malicious IP detected: {ip}")
    label.pack(pady=20)
    win.after(7000, lambda: win.destroy())
    win.mainloop()