import tkinter as tk

dev = tk.Tk()

dev.geometry("700x400")

dev.config(background='yellow')


def calculate_double():
    try:
        number = int(entry_1.get())
        result = number * 2
        entry_2.delete(0, tk.END)  # Clear the entry_2 widget
        entry_2.insert(tk.END, result)  # Insert the result into the entry_2 widget
    except ValueError:
        entry_2.delete(0, tk.END)  # Clear the entry_2 widget
        entry_2.insert(tk.END, "Please enter a valid number")  # Display an error message in the entry_2 widget

label_1 = tk.Label(dev, text="Enter the number:", font=("Arial", 14))
label_1.place(x=30, y=70)
entry_1 = tk.Entry(dev)
entry_1.place(x=190, y=70)

label_2 = tk.Label(dev, text="Result:", font=("Arial", 14))
label_2.place(x=70, y=120)
entry_2 = tk.Entry(dev)
entry_2.place(x=190, y=120)

button = tk.Button(dev, text="Calculate", command=calculate_double)
button.place(x=150, y=200)

dev.mainloop()