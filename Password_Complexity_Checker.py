import tkinter as tk
from tkinter import ttk
import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ At least 8 characters required")

    # Check uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letter (A-Z)")

    # Check lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letter (a-z)")

    # Check numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Add a number (0-9)")

    # Check special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Add a special character (!@#$...)")

    return score, feedback

def update_strength(event=None):
    password = entry.get()

    if not password:
        strength_label.config(text="", fg="white")
        progress['value'] = 0
        feedback_label.config(text="")
        return

    score, feedback = check_password_strength(password)

    # Progress bar
    progress['value'] = score * 20

    # Strength label
    if score <= 2:
        strength_label.config(text="🔴 Weak Password", fg="#FF4444")
        progress_style.configure("TProgressbar", background="#FF4444")
    elif score <= 4:
        strength_label.config(text="🟡 Moderate Password", fg="#FFD700")
        progress_style.configure("TProgressbar", background="#FFD700")
    else:
        strength_label.config(text="🟢 Strong Password!", fg="#00FF88")
        progress_style.configure("TProgressbar", background="#00FF88")

    # Feedback
    if feedback:
        feedback_label.config(text="\n".join(feedback))
    else:
        feedback_label.config(text="✅ Perfect! All criteria met!")

def toggle_password():
    if entry.cget('show') == '*':
        entry.config(show='')
        toggle_btn.config(text="🙈 Hide")
    else:
        entry.config(show='*')
        toggle_btn.config(text="👁 Show")

# ── GUI Setup ──────────────────────────────────────
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("500x450")
root.config(bg="#1a1a2e")
root.resizable(False, False)

progress_style = ttk.Style()
progress_style.theme_use('clam')
progress_style.configure("TProgressbar",
                          troughcolor="#333366",
                          background="#00FF88",
                          thickness=20)

# Title
tk.Label(root, text="🔐 Password Strength Checker",
         font=("Helvetica", 16, "bold"),
         bg="#1a1a2e", fg="#00d4ff").pack(pady=20)

# Password Entry Frame
frame = tk.Frame(root, bg="#1a1a2e")
frame.pack(pady=5)

entry = tk.Entry(frame, show='*', font=("Helvetica", 14),
                 width=25, bg="#16213e", fg="white",
                 insertbackground="white", bd=0,
                 highlightthickness=2,
                 highlightcolor="#00d4ff",
                 highlightbackground="#333366")
entry.pack(side=tk.LEFT, ipady=8, padx=(0, 5))
entry.bind("<KeyRelease>", update_strength)

toggle_btn = tk.Button(frame, text="👁 Show",
                       command=toggle_password,
                       bg="#333366", fg="white",
                       font=("Helvetica", 10),
                       bd=0, padx=8, pady=8,
                       cursor="hand2")
toggle_btn.pack(side=tk.LEFT)

# Progress Bar
progress = ttk.Progressbar(root, style="TProgressbar",
                            length=400, maximum=100)
progress.pack(pady=15)

# Strength Label
strength_label = tk.Label(root, text="",
                           font=("Helvetica", 14, "bold"),
                           bg="#1a1a2e", fg="white")
strength_label.pack(pady=5)

# Feedback Box
feedback_frame = tk.Frame(root, bg="#16213e",
                           bd=0, relief="flat")
feedback_frame.pack(pady=10, padx=30, fill="x")

feedback_label = tk.Label(feedback_frame, text="",
                           font=("Helvetica", 11),
                           bg="#16213e", fg="#aaaacc",
                           justify="left", wraplength=420)
feedback_label.pack(padx=15, pady=10)

# Footer
tk.Label(root, text="Prodigy InfoTech | Task 03",
         font=("Helvetica", 9),
         bg="#1a1a2e", fg="#555577").pack(side="bottom", pady=10)

root.mainloop()
