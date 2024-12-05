import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        name = entry_name.get()
        age = int(entry_age.get())
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        bmi_index = weight / height**2

        if bmi_index <= 18.4:
            status = 'Underweight'
        elif bmi_index > 18.5 and bmi_index < 24.9:
            status = 'Normal'
        elif bmi_index > 25.0 and bmi_index < 39.9:
            status = 'Overweight'
        else:
            status = 'Obese'

        result = (
            f"Hi {name}!\n"
            f"Age: {age}, Height: {height}m, Weight: {weight}kg\n"
            f"Your BMI is {bmi_index:.3f}, which is considered {status}."
        )
        messagebox.showinfo("BMI Result", result)
    except Exception as e:
        messagebox.showerror("Error", "Please enter valid inputs.")

app = tk.Tk()
app.title("BMI Calculator")

tk.Label(app, text="Enter your name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(app)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(app, text="Enter your age:").grid(row=1, column=0, padx=10, pady=5)
entry_age = tk.Entry(app)
entry_age.grid(row=1, column=1, padx=10, pady=5)

tk.Label(app, text="Enter your height (meters):").grid(row=2, column=0, padx=10, pady=5)
entry_height = tk.Entry(app)
entry_height.grid(row=2, column=1, padx=10, pady=5)

tk.Label(app, text="Enter your weight (kg):").grid(row=3, column=0, padx=10, pady=5)
entry_weight = tk.Entry(app)
entry_weight.grid(row=3, column=1, padx=10, pady=5)

tk.Button(app, text="Calculate BMI", command=calculate_bmi).grid(row=4, column=0, columnspan=2, pady=10)

app.mainloop()