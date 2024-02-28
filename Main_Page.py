'''
Estimation of the pressure of a vessel after a sodium-water interaction
Main Page

Cody Parkinson
Last Update: 02/28/2024

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
root.title("Sodium and Water Reaction Calculator - Cody Parkinson")









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

        # Update each label with the corresponding value from the dictionary
        for key, value in final_result.items():
            result_labels[key].config(text=f"{value}")

    except ValueError as e:
        # Update the result label to show the error
        result_label_error.config(text=f"Error: {str(e)}")

# Attach the `calculate` function to the calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate)










# Calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate)

calculate_button.grid(row=6, column=0, columnspan=2)



def create_result_labels(root, keys, row_start):
    labels = {}
    for i, key in enumerate(keys):
        # Create a label for the key
        ttk.Label(root, text=f"{key}: ").grid(row=row_start + i, column=0, sticky="w")

        # Create a label for the value and store it in a dictionary
        value_label = ttk.Label(root, text="")
        value_label.grid(row=row_start + i, column=1, sticky="w")
        labels[key] = value_label
    return labels

# Create labels for each result
keys = ["DensityOfWater", "DensityOfSodium", "DensityOfNaOH", "TotalSodiumMass", "NaOHwt%", "NaOHVolume", "NetVoidChange", "FinalOpenCapsulePlenumVolume", "finalHydrogrenPressurePSI"]
result_labels = create_result_labels(root, keys, 8)  # Adjust row_start as needed



# LOOK AT GPT FOR THE CODE TO UPDATE THE LABEL INCASE THERE IS AN ERROR 

result_label_error = ttk.Label(root, text="Result: ")



result_label_error = ttk.Label(root, text="Result: ")





root.mainloop()

