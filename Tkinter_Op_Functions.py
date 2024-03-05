'''
Tkinter functions location

Cody Parkinson
Last Update: 02/29/2024

This file is dedicated to creating a space for tkinter specific functions needed
for proper handling.
'''



'''
Imports
'''
import tkinter as tk
from tkinter import ttk








'''
Check for float input. Do not allow letters or other characters to be input
'''
def is_float_value_inputs(input):
    if input.isdigit() or input == "":
        return True
    try:
        float(input)
        return True
    except ValueError:
        return False
    





'''
Template for entry field of User Values
'''
def create_entry_field_UI(root, label_text, row, column):
    # Create a label for the entry
    label = ttk.Label(root, text=label_text)
    label.grid(row=row, column=column)

    # Create a StringVar to hold the text of the entry
    entry_variable = tk.StringVar()

    # Register the validation function
    validate_float = root.register(is_float_value_inputs)

    # Create the entry widget with validation
    entry = ttk.Entry(root, textvariable=entry_variable, validate="key", validatecommand=(validate_float, '%P'))
    entry.grid(row=row, column=column + 1)

    # Return the StringVar associated with the entry, to retrieve its value later
    return entry_variable