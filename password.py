import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    username = username_entry.get().strip()
    try:
        length = int(password_length_entry.get())
        if not username:
            raise ValueError("Please enter a username.")
        if length < 4:
            raise ValueError("Password length must be at least 4.")

        # Define character pools
        all_characters = string.ascii_letters + string.digits + string.punctuation

        # Generate password
        password = ''.join(random.choice(all_characters) for _ in range(length))
        password_output.config(state='normal')  # Enable text widget
        password_output.delete(1.0, tk.END)    # Clear previous output
        password_output.insert(tk.END, f"Username: {username}\nPassword: {password}")  # Display result
        password_output.config(state='disabled')  # Disable text widget
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x300")
root.resizable(False, False)
root.configure(bg="#f0f0f0")  # Light background

# Title Label
title_label = tk.Label(root, text="Strong Password Generator", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

# Username Entry
username_frame = tk.Frame(root, bg="#f0f0f0")
username_frame.pack(pady=5)
username_label = tk.Label(username_frame, text="Enter Username:", font=("Arial", 12), bg="#f0f0f0", fg="#555")
username_label.pack(side=tk.LEFT, padx=5)
username_entry = tk.Entry(username_frame, width=20, font=("Arial", 12))
username_entry.pack(side=tk.LEFT, padx=5)

# Password Length Entry
length_frame = tk.Frame(root, bg="#f0f0f0")
length_frame.pack(pady=5)
length_label = tk.Label(length_frame, text="Password Length:", font=("Arial", 12), bg="#f0f0f0", fg="#555")
length_label.pack(side=tk.LEFT, padx=5)
password_length_entry = tk.Entry(length_frame, width=10, font=("Arial", 12))
password_length_entry.pack(side=tk.LEFT, padx=5)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12), bg="#4caf50", fg="white", command=generate_password)
generate_button.pack(pady=15)

# Password Output Display
password_output = tk.Text(root, height=3, width=40, font=("Arial", 12), state='disabled', wrap=tk.WORD, bg="#e0f7fa", fg="#000")
password_output.pack(pady=10)

# Footer
footer_label = tk.Label(root, text="secure password", font=("Arial", 10), bg="#f0f0f0", fg="#777")
footer_label.pack(pady=5)

# Run the application
root.mainloop()
