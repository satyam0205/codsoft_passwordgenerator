import tkinter as tk
import random
import string

class PasswordGenGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(master, width=30)
        self.length_entry.pack()

        self.complexity_label = tk.Label(master, text="Complexity Level:")
        self.complexity_label.pack()

        self.complexity_var = tk.StringVar()
        self.complexity_var.set("low")

        self.low_radio = tk.Radiobutton(master, text="Low", variable=self.complexity_var, value="low")
        self.low_radio.pack()

        self.medium_radio = tk.Radiobutton(master, text="Medium", variable=self.complexity_var, value="medium")
        self.medium_radio.pack()

        self.high_radio = tk.Radiobutton(master, text="High", variable=self.complexity_var, value="high")
        self.high_radio.pack()

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password_gui)
        self.generate_button.pack()

        self.password_label = tk.Label(master, text="Generated Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(master, width=40)
        self.password_entry.pack()

    def generate_password_gui(self):
        length = int(self.length_entry.get())
        complexity = self.complexity_var.get()

        password = self.generate_password(length, complexity)
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def generate_password(self, length, complexity):
        # Generate password based on complexity level
        if complexity == "low":
            chars = "1234567890"
        elif complexity == "medium":
            chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        elif complexity == "high":
            chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-=+:;<>,./?"

        password = ''.join(random.choice(chars) for _ in range(length))
        return password

root = tk.Tk()
my_gui = PasswordGenGUI(root)
root.mainloop()