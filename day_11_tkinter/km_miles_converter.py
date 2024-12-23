import tkinter as tk

def convert_km_to_miles(event=None):
    try:
        km = float(entry_km.get())
        miles = km * 0.621371
        label_result.config(text=f"{miles:.2f} Miles")
    except ValueError:
        label_result.config(text="Invalid input")

# Create the main window
root = tk.Tk()
root.title("Kilometers to Miles Converter")

# Create and place the widgets
label_km = tk.Label(root, text="Enter kilometers:")
label_km.grid(row=0, column=0, padx=10, pady=10)

entry_km = tk.Entry(root)
entry_km.grid(row=0, column=1, padx=10, pady=10)
entry_km.bind("<KeyRelease>", convert_km_to_miles)  # Bind key release event

button_convert = tk.Button(root, text="Convert", command=convert_km_to_miles)
button_convert.grid(row=1, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="")
label_result.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
