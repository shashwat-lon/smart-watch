import tkinter as tk
from tkinter import ttk
import time
import random

class SmartWatch:
    def __init__(self, root):
        self.root = root
        self.root.title("⌚ Smart Watch")
        self.root.geometry("300x300")
        self.root.resizable(False, False)
        self.root.configure(bg="black")
        
        # Time Label
        self.time_label = tk.Label(root, font=("Helvetica", 20, "bold"), fg="lime", bg="black")
        self.time_label.pack(pady=10)

        # Date Label
        self.date_label = tk.Label(root, font=("Helvetica", 12), fg="cyan", bg="black")
        self.date_label.pack(pady=5)

        # Heart Rate
        self.heart_label = tk.Label(root, text=" Heart Rate: -- bpm", font=("Helvetica", 14), fg="red", bg="black")
        self.heart_label.pack(pady=10)

        # Step Counter
        self.steps_label = tk.Label(root, text="👣 Steps: --", font=("Helvetica", 14), fg="yellow", bg="black")
        self.steps_label.pack(pady=10)

        # Refresh Button
        self.refresh_btn = ttk.Button(root, text="🔄 Refresh Health Data", command=self.update_health_data)
        self.refresh_btn.pack(pady=15)

        # Start Clock
        self.update_clock()
        self.update_health_data()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%A, %d %B %Y")
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        self.root.after(1000, self.update_clock)  # update every 1 sec

    def update_health_data(self):
        heart_rate = random.randint(60, 100)   # simulate heart rate
        steps = random.randint(1000, 15000)    # simulate steps
        self.heart_label.config(text=f" Heart Rate: {heart_rate} bpm")
        self.steps_label.config(text=f" Steps: {steps}")

# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = SmartWatch(root)
    root.mainloop()
