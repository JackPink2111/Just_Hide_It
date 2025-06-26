import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from pathlib import Path
from datetime import datetime
import shutil

LOG_FILE = "extension_change_log.txt"

def log_change(original_path, new_path):
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.now()}] Copied & Renamed: {original_path} → {new_path}\n")

def change_file_extension(filepath):
    file_path = Path(filepath)
    if not file_path.exists():
        messagebox.showerror("Error", "❌ File not found.")
        return

    # Ask for new extension
    new_ext = simpledialog.askstring("New Extension", "Enter new extension (e.g. txt, jpg, py):")
    if not new_ext:
        return

    # Ask where to save the new file
    save_path = filedialog.asksaveasfilename(
        defaultextension=f".{new_ext.lstrip('.')}",
        initialfile=file_path.stem,
        title="Save As",
        filetypes=[("All Files", "*.*")]
    )
    if not save_path:
        return

    new_file_path = Path(save_path)
    
    try:
        # Copy original file
        shutil.copy(file_path, new_file_path)
        messagebox.showinfo("Success", f"✅ Copied and renamed to: {new_file_path.name}")
        log_change(file_path, new_file_path)
    except Exception as e:
        messagebox.showerror("Error", f"❌ Failed to copy & rename file.\n{e}")

# GUI setup
root = tk.Tk()
root.title("File Extension Changer")
root.geometry("450x250")
root.resizable(False, False)

title = tk.Label(root, text="🛠️ Extension Changer (Safe Copy Mode)", font=("Arial", 14, "bold"))
title.pack(pady=10)

desc = tk.Label(root, text="📂 Choose a file → ✏️ Enter extension → 💾 Choose save location", font=("Arial", 10))
desc.pack()

btn = tk.Button(
    root,
    text="📁 Select File to Copy and Change Extension",
    command=lambda: change_file_extension(filedialog.askopenfilename()),
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5
)
btn.pack(pady=30)

footer = tk.Label(root, text="📝 Log saved to extension_change_log.txt", font=("Arial", 9), fg="gray")
footer.pack(side="bottom", pady=10)

root.mainloop()
