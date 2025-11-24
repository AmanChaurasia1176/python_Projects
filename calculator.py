import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")
        master.geometry("300x400") # Set initial window size
        master.resizable(False, False) # Prevent resizing for a cleaner layout

        # Variable to store the current input/result
        self.expression = ""
        
        # --- 1. Create the display screen ---
        self.display = tk.Entry(master, 
                                font=('Arial', 24), 
                                textvariable=tk.StringVar(), # Use StringVar for dynamic updates
                                justify='right',             # Align text to the right
                                bd=10,                       # Border width
                                relief='groove')             # Border style
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        self.display.config(state='readonly') # Make it read-only so user can't type directly

        # Ensure the StringVar is linked to the display
        self.display_var = tk.StringVar()
        self.display.config(textvariable=self.display_var)
        self.display_var.set("0") # Initial display value

        # --- 2. Create the buttons ---
        self.create_buttons()

        # Configure row and column weights for a responsive grid layout
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

    def create_buttons(self):
        # Define button texts and their positions in the grid
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Special buttons
        tk.Button(self.master, text="C", font=('Arial', 18), 
                  command=self.clear_display).grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        tk.Button(self.master, text="DEL", font=('Arial', 18), 
                  command=self.delete_last_char).grid(row=5, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)


        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, font=('Arial', 18),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

    def on_button_click(self, char):
        if char == '=':
            try:
                # Evaluate the expression
                result = str(eval(self.expression))
                self.expression = result
                self.display_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.display_var.set("0")
        else:
            if self.expression == "0" and char not in ('+', '-', '*', '/', '.'): # Handle initial '0'
                self.expression = char
            else:
                self.expression += str(char)
            self.display_var.set(self.expression)

    def clear_display(self):
        self.expression = ""
        self.display_var.set("0")

    def delete_last_char(self):
        if self.expression: # Only delete if there's something to delete
            self.expression = self.expression[:-1] # Remove the last character
            if not self.expression: # If expression becomes empty, set to "0"
                self.expression = "0"
            self.display_var.set(self.expression)


# --- Main execution block ---
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()