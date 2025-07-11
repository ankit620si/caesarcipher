import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = shift if mode == "Encrypt" else -shift
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char
    return result

def process_cipher():
    text = text_entry.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift must be an integer.")
        return

    mode = cipher_mode.get()
    if not text:
        messagebox.showwarning("Input Required", "Please enter some text.")
        return

    result = caesar_cipher(text, shift, mode)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)
    output_text.config(state=tk.DISABLED)

# GUI setup
root = tk.Tk()
root.title("🔐 Caesar Cipher GUI")
root.geometry("500x500")
root.configure(bg="#1e1e2f")

# Title
title = tk.Label(root, text="Caesar Cipher", font=("Helvetica", 20, "bold"),
                 fg="#61dafb", bg="#1e1e2f")
title.pack(pady=10)

# Input Text
tk.Label(root, text="Enter Text:", bg="#1e1e2f", fg="white", font=("Helvetica", 12)).pack()
text_entry = tk.Text(root, height=5, font=("Helvetica", 12), wrap=tk.WORD)
text_entry.pack(padx=20, pady=5, fill=tk.X)

# Shift Value
tk.Label(root, text="Shift Value:", bg="#1e1e2f", fg="white", font=("Helvetica", 12)).pack()
shift_entry = tk.Entry(root, font=("Helvetica", 12))
shift_entry.pack(pady=5)

# Mode Selection
cipher_mode = tk.StringVar(value="Encrypt")
mode_frame = tk.Frame(root, bg="#1e1e2f")
tk.Radiobutton(mode_frame, text="Encrypt", variable=cipher_mode, value="Encrypt", bg="#1e1e2f", fg="white").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(mode_frame, text="Decrypt", variable=cipher_mode, value="Decrypt", bg="#1e1e2f", fg="white").pack(side=tk.LEFT, padx=10)
mode_frame.pack(pady=10)

# Button
process_button = tk.Button(root, text="🔄 Process", font=("Helvetica", 12, "bold"),
                           bg="#61dafb", fg="black", command=process_cipher)
process_button.pack(pady=10)

# Output
tk.Label(root, text="Output:", bg="#1e1e2f", fg="white", font=("Helvetica", 12)).pack()
output_text = tk.Text(root, height=5, font=("Helvetica", 12), wrap=tk.WORD, state=tk.DISABLED)
output_text.pack(padx=20, pady=5, fill=tk.X)

# Run the GUI
root.mainloop()
