'''
Estimation of the pressure of a vessel after a sodium-water interaction
Main Page

Cody Parkinson
Last Update: 02/29/2024

Just for Cody: Make sure to run in python3.9 on Mac
'''






'''
Imports
'''
import tkinter as tk
from tkinter import ttk
from Calculator_Steps import MaximumPressureCalculator, plot_graph_PvsT
from Tkinter_Op_Functions import create_entry_field_UI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



canvas_widget = None


'''
Tkinter Page Layout
'''
root = tk.Tk()
root.title("Sodium and Water Reaction Calculator - Cody Parkinson")




# User inputs
water_temperature_var = create_entry_field_UI(root, "Water Temperature (C)", 0, 0)
water_pressure_var = create_entry_field_UI(root, "Water Pressure (MPa)", 1, 0)
outerCapsuleVoidVolume_var = create_entry_field_UI(root, "Outer Capsule Void Volume (cm^3)", 2, 0)
innerCapsuleVoidVolume_var = create_entry_field_UI(root, "Inner Capsule Void Volume (cm^3)", 3, 0)
massOfSodiumCapsule_var = create_entry_field_UI(root, "Sodium Mass within Capsule (g)", 4, 0)
massOfSodiumRodlet_var = create_entry_field_UI(root, "Sodium Mass within Rodlet (g)", 5, 0)





def calculate():

    global canvas_widget  # Declare that you're using the global variable


    try:
        # Retrieve and convert values, using 0.0 or any default value if the field is empty
        water_temperature = float(water_temperature_var.get()) if water_temperature_var.get() else 0.0
        water_pressure = float(water_pressure_var.get()) if water_pressure_var.get() else 0.0
        outerCapsuleVoidVolume = float(outerCapsuleVoidVolume_var.get()) if outerCapsuleVoidVolume_var.get() else 0.0
        innerCapsuleVoidVolume = float(innerCapsuleVoidVolume_var.get()) if innerCapsuleVoidVolume_var.get() else 0.0
        massOfSodiumCapsule = float(massOfSodiumCapsule_var.get()) if massOfSodiumCapsule_var.get() else 0.0
        massOfSodiumRodlet = float(massOfSodiumRodlet_var.get()) if massOfSodiumRodlet_var.get() else 0.0

        # Call your calculation function (modify this according to your actual function)
        final_result, graphInfo = MaximumPressureCalculator(water_temperature, water_pressure, outerCapsuleVoidVolume, innerCapsuleVoidVolume, massOfSodiumCapsule, massOfSodiumRodlet)

        # Update each label with the corresponding value from the dictionary
        for key, value in final_result.items():
            result_labels[key].config(text=str(value[0]) + " " + "[" + value[1] + "]")


        # Prepare the graph based on the calculated results or input values
        fig = plot_graph_PvsT(graphInfo["molesOfHydrogen"], graphInfo["finalPlenumVolume"])

        # Check if canvas_widget is already created
        if canvas_widget is not None:
            # Clear the previous canvas (if it exists)
            canvas_widget.get_tk_widget().destroy()



        # Create a new canvas and add the updated graph
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas_widget = canvas  # Update the global variable
        canvas_widget_widget = canvas.get_tk_widget()
        canvas_widget_widget.grid(row=20, column=0, columnspan=10, sticky="nsew")  # Use grid






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





result_label_error = ttk.Label(root, text="Result: ")



# Calculate the row position for the result_label_error
error_label_row = 8 + len(keys) + 3  # +3 for two spaces and the next row

# Place the result_label_error
result_label_error = ttk.Label(root, text="ERRORS: ")
result_label_error.grid(row=error_label_row, column=0, columnspan=2, sticky="w")















root.mainloop()

