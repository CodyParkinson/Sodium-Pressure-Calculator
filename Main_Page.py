'''
Estimation of the pressure of a vessel after a sodium-water interaction
Main Page

Cody Parkinson
Last Update: 02/26/2024

Just for Cody: Make sure to run in python3.9
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

# Template for creating an entry field
def create_entry_field(root, label_text, row, column):
    # Create a label for the entry
    label = ttk.Label(root, text=label_text)
    label.grid(row=row, column=column)

    # Create a StringVar to hold the text of the entry
    entry_variable = tk.StringVar()

    # Create the entry widget and attach it to the StringVar
    entry = ttk.Entry(root, textvariable=entry_variable)
    entry.grid(row=row, column=column + 1)

    # Return the StringVar associated with the entry, to retrieve its value later
    return entry_variable

# Example usage of the template to create an entry field
# The returned StringVar can be used to get the value entered by the user
water_temperature_var = create_entry_field(root, "Water Temperature (C)", 0, 0)
# You can create more entry fields using the same template

# Calculate button
calculate_button = ttk.Button(root, text="Calculate", command=MaximumPressureCalculator(1,1,1,1,1,1))
calculate_button.grid(row=10, column=0, columnspan=2)  # Adjust the row and column as needed

root.mainloop()

