import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Cannot divide by zero"
        else:
            result = "Invalid operator"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input")

# Create the main window
window = tk.Tk()
window.title("GUI Calculator")

# Entry widgets for input
entry_num1 = tk.Entry(window)
entry_num2 = tk.Entry(window)

# Dropdown menu for operator selection
operator_var = tk.StringVar()
operator_var.set('+')  # Default operator
operator_menu = tk.OptionMenu(window, operator_var, '+', '-', '*', '/')

# Button to trigger calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)

# Label to display result
result_label = tk.Label(window, text="Result: ")

# Arrange widgets using grid layout
entry_num1.grid(row=0, column=0)
operator_menu.grid(row=0, column=1)
entry_num2.grid(row=0, column=2)
calculate_button.grid(row=1, column=0, columnspan=3)
result_label.grid(row=2, column=0, columnspan=3)

# Run the GUI
window.mainloop()