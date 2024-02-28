'''
Estimation of the pressure of a vessel after a sodium-water interaction
Main Page

Cody Parkinson
Last Update: 02/27/2024

Just for Cody: Make sure to run in python3.9 on Mac
'''





'''
Imports
'''

import tkinter as tk
from tkinter import ttk
from Calculator_Steps import MaximumPressureCalculator





'''
Tkinter
'''

root = tk.Tk()
root.title("Chemical Reaction Calculator")

# Check for float input
def is_float(input):
    if input.isdigit() or input == "":
        return True
    try:
        float(input)
        return True
    except ValueError:
        return False


# Template for entry field
def create_entry_field(root, label_text, row, column):
    # Create a label for the entry
    label = ttk.Label(root, text=label_text)
    label.grid(row=row, column=column)

    # Create a StringVar to hold the text of the entry
    entry_variable = tk.StringVar()

    # Register the validation function
    validate_float = root.register(is_float)

    # Create the entry widget with validation
    entry = ttk.Entry(root, textvariable=entry_variable, validate="key", validatecommand=(validate_float, '%P'))
    entry.grid(row=row, column=column + 1)

    # Return the StringVar associated with the entry, to retrieve its value later
    return entry_variable


# User inputs
water_temperature_var = create_entry_field(root, "Water Temperature (C)", 0, 0)
water_pressure_var = create_entry_field(root, "Water Pressure (MPa)", 1, 0)
outerCapsuleVoidVolume_var = create_entry_field(root, "Outer Capsule Void Volume (cm^3)", 2, 0)
innerCapsuleVoidVolume_var = create_entry_field(root, "Inner Capsule Void Volume (cm^3)", 3, 0)
massOfSodiumCapsule_var = create_entry_field(root, "Sodium Mass within Capsule (g)", 4, 0)
massOfSodiumRodlet_var = create_entry_field(root, "Sodium Mass within Rodlet (g)", 5, 0)





def calculate():
    try:
        # Retrieve and convert values, using 0.0 or any default value if the field is empty
        water_temperature = float(water_temperature_var.get()) if water_temperature_var.get() else 0.0
        water_pressure = float(water_pressure_var.get()) if water_pressure_var.get() else 0.0
        outerCapsuleVoidVolume = float(outerCapsuleVoidVolume_var.get()) if outerCapsuleVoidVolume_var.get() else 0.0
        innerCapsuleVoidVolume = float(innerCapsuleVoidVolume_var.get()) if innerCapsuleVoidVolume_var.get() else 0.0
        massOfSodiumCapsule = float(massOfSodiumCapsule_var.get()) if massOfSodiumCapsule_var.get() else 0.0
        massOfSodiumRodlet = float(massOfSodiumRodlet_var.get()) if massOfSodiumRodlet_var.get() else 0.0

        # Call your calculation function (modify this according to your actual function)
        final_result = MaximumPressureCalculator(water_temperature, water_pressure, outerCapsuleVoidVolume, innerCapsuleVoidVolume, massOfSodiumCapsule, massOfSodiumRodlet)

        # Update the result label with the calculated value
        result_label.config(text=f"Result: {final_result}")

    except ValueError:
        # Update the result label to show the error
        result_label.config(text=f"Error: {str(e)}")

# Attach the `calculate` function to the calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate)








# Calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate)

calculate_button.grid(row=6, column=0, columnspan=2)



result_label = ttk.Label(root, text="Result: ")
result_label.grid(row=7, column=0, columnspan=2)


root.mainloop()

