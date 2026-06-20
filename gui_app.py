import tkinter as tk
from tkinter import ttk
import pickle
import pandas as pd

# Load AI Model
model = pickle.load(open("model.pkl", "rb"))

# Solution Database
solutions = {
    "Compass": "Recalibrate compass using Mission Planner.",
    "GPS": "Check GPS wiring and antenna placement.",
    "ESC": "Inspect ESC temperature and recalibrate ESCs.",
    "MotorDirection": "Verify CW and CCW motor rotation.",
    "Propeller": "Inspect and replace damaged propellers."
}

# Predict Function
def predict_fault():

    yaw = 1 if yaw_var.get() == "Yes" else 0
    gps = 1 if gps_var.get() == "Yes" else 0
    motor = 1 if motor_var.get() == "Yes" else 0
    vibration = 1 if vibration_var.get() == "Yes" else 0

    input_data = pd.DataFrame(
        [[yaw, gps, motor, vibration]],
        columns=["yaw", "gps", "motor_hot", "vibration"]
    )

    fault = model.predict(input_data)[0]

    result_label.config(text="Fault: " + fault)

    solution_label.config(
        text="Solution: " + solutions.get(fault, "No solution found")
    )

# GUI Window
root = tk.Tk()
root.title("AI Drone Assistant")
root.geometry("600x450")

title = tk.Label(
    root,
    text="AI Drone Fault Diagnosis Assistant",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

# Variables
yaw_var = tk.StringVar(value="No")
gps_var = tk.StringVar(value="No")
motor_var = tk.StringVar(value="No")
vibration_var = tk.StringVar(value="No")

# Inputs
tk.Label(root, text="Yaw Problem").pack()

ttk.Combobox(
    root,
    textvariable=yaw_var,
    values=["Yes", "No"]
).pack()

tk.Label(root, text="GPS Problem").pack()

ttk.Combobox(
    root,
    textvariable=gps_var,
    values=["Yes", "No"]
).pack()

tk.Label(root, text="Motor Hot").pack()

ttk.Combobox(
    root,
    textvariable=motor_var,
    values=["Yes", "No"]
).pack()

tk.Label(root, text="High Vibration").pack()

ttk.Combobox(
    root,
    textvariable=vibration_var,
    values=["Yes", "No"]
).pack()

# Button
tk.Button(
    root,
    text="Predict Fault",
    command=predict_fault
).pack(pady=15)

# Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold")
)
result_label.pack()

solution_label = tk.Label(
    root,
    text="",
    wraplength=500
)
solution_label.pack(pady=10)

root.mainloop()
