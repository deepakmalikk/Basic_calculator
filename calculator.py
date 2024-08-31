import tkinter as tk


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))


def button_clear():
    entry.delete(0, tk.END)


def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# Create the main window
root = tk.Tk()
root.title("Basic Calculator")

# Create the entry widget
entry = tk.Entry(root, width=16, borderwidth=5, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4)

# Define button texts
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create buttons and add them to the grid
row_value = 1
col_value = 0
for button_text in buttons:
    if button_text == '=':
        button = tk.Button(root, text=button_text, padx=40, pady=20, font=('Arial', 18),
                           command=button_equal)
    elif button_text == 'C':
        button = tk.Button(root, text=button_text, padx=40, pady=20, font=('Arial', 18),
                           command=button_clear)
    else:
        button = tk.Button(root, text=button_text, padx=40, pady=20, font=('Arial', 18),
                           command=lambda text=button_text: button_click(text))

    button.grid(row=row_value, column=col_value)

    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

# Create the 'Clear' button
button_clear = tk.Button(root, text='C', padx=40, pady=20, font=('Arial', 18),
                         command=button_clear)
button_clear.grid(row=5, column=0, columnspan=2)

# Run the application
root.mainloop()