import tkinter as tk
from tkinter import messagebox

# Function to calculate FLAMES
def calculate_flames(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    # Remove common letters
    for letter in name1:
        if letter in name2:
            name1 = name1.replace(letter, "", 1)
            name2 = name2.replace(letter, "", 1)

    # Calculate remaining letters count
    count = len(name1 + name2)

    # FLAMES logic
    flames = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]
    while len(flames) > 1:
        index = (count % len(flames)) - 1
        if index >= 0:
            flames = flames[index + 1:] + flames[:index]
        else:
            flames = flames[:-1]

    return flames[0]

# Button click event
def on_calculate():
    name1 = entry_name1.get()
    name2 = entry_name2.get()

    if not name1 or not name2:
        messagebox.showerror("Input Error", "Please enter both names!")
        return

    result = calculate_flames(name1, name2)
    result_label.config(text=f"Relationship: {result}")

# GUI setup
root = tk.Tk()
root.title("Saro' FLAMES Game")
root.geometry("400x300")
root.configure(bg="#FFD1DC")  # Light pink background

# Title
title_label = tk.Label(root, text="FLAMES Game", font=("Helvetica", 20, "bold"), bg="#FFD1DC", fg="#D11D53")
title_label.pack(pady=10)

# Input fields
frame = tk.Frame(root, bg="#FFD1DC")
frame.pack()

label_name1 = tk.Label(frame, text="Name 1:", font=("Helvetica", 12), bg="#FFD1DC")
label_name1.grid(row=0, column=0, padx=10, pady=5)

entry_name1 = tk.Entry(frame, font=("Helvetica", 12))
entry_name1.grid(row=0, column=1, padx=10, pady=5)

label_name2 = tk.Label(frame, text="Name 2:", font=("Helvetica", 12), bg="#FFD1DC")
label_name2.grid(row=1, column=0, padx=10, pady=5)

entry_name2 = tk.Entry(frame, font=("Helvetica", 12))
entry_name2.grid(row=1, column=1, padx=10, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", font=("Helvetica", 14), bg="#FFB6C1", fg="black", command=on_calculate)
calculate_button.pack(pady=10)

# Result display
result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#FFD1DC", fg="#D11D53")
result_label.pack(pady=10)

# Run the app
root.mainloop()
