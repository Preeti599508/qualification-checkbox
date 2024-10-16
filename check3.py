import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd

# Function to get the status of checkboxes and create a CSV file
def show_selection():
    selected = []
    if var_10th.get():
        selected.append("10th")
    if var_12th.get():
        selected.append("12th")
    if var_grad.get():
        selected.append("Graduate")
    if var_postgrad.get():
        selected.append("Post Graduate")
    
    print("Selected Qualifications: ", selected)

    # Check if any qualifications are selected
    if selected:
        # Join selected qualifications into a single string separated by commas
        qualifications_str = ', '.join(selected)

        # Create a DataFrame for the qualifications
        df = pd.DataFrame({'Qualification': [qualifications_str]})

        # Write the DataFrame to a CSV file
        csv_file = "qualifications.csv"
        df.to_csv(csv_file, index=False)

        # Show success message
        messagebox.showinfo("Success", f"Data has been successfully saved to {csv_file}.")

        # Display the data in the message box
        messagebox.showinfo("Selected Qualifications", f"Qualifications:\n{qualifications_str}")
    else:
        # Show warning if no qualifications are selected
        messagebox.showwarning("No Selection", "No qualifications selected.")

# Create the main window
root = tk.Tk()
root.title("Qualification Selection")
root.config(bg="blue")

# Define a style for the labels, checkbuttons, and button with a larger font
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 14))
style.configure("TCheckbutton", font=("Helvetica", 14))
style.configure("TButton", font=("Helvetica", 14))

# Create a frame with a bold black border
border_frame = tk.Frame(root, bg="white", highlightbackground="black", highlightthickness=3, bd=5)
border_frame.grid(row=0, column=0, padx=10, pady=10)

# Configure the border_frame grid to expand and center the content
border_frame.grid_rowconfigure(0, weight=1)
border_frame.grid_columnconfigure(0, weight=1)

# Create another frame inside the bordered frame for layout management
frame = ttk.Frame(border_frame, padding="10")
frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Configure the frame grid to center its content
frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)  # Adjusts rows 0-4 to have equal weight for vertical centering
frame.grid_columnconfigure((0, 1, 2), weight=1)     # Adjusts columns 0-2 for horizontal centering

# Create variables for checkboxes
var_10th = tk.IntVar()
var_12th = tk.IntVar()
var_grad = tk.IntVar()
var_postgrad = tk.IntVar()

# Create a label for "Qualification" in the left column, aligned in the middle, with larger text
label_qualification = ttk.Label(frame, text="Qualification")
label_qualification.grid(row=0, column=0, rowspan=4, padx=5, pady=5, sticky='ns')  # Sticky 'ns' aligns it vertically in the middle

# Add a bold black vertical line (separator) using a Canvas between the Qualification label and checkboxes
separator_canvas = tk.Canvas(frame, width=4, bg="black", highlightthickness=0)
separator_canvas.grid(row=0, column=1, rowspan=4, sticky='ns', padx=10, pady=5)

# Create the checkboxes and their labels on the right side (column 2) with larger text
ttk.Checkbutton(frame, text="10th", variable=var_10th).grid(row=0, column=2, padx=5, pady=5, sticky='w')
ttk.Checkbutton(frame, text="12th", variable=var_12th).grid(row=1, column=2, padx=5, pady=5, sticky='w')
ttk.Checkbutton(frame, text="Graduate", variable=var_grad).grid(row=2, column=2, padx=5, pady=5, sticky='w')
ttk.Checkbutton(frame, text="Post Graduate", variable=var_postgrad).grid(row=3, column=2, padx=5, pady=5, sticky='w')

# Create a button to show the selected qualifications with larger text
button = ttk.Button(frame, text="Show Selection", command=show_selection)
button.grid(row=4, column=2, padx=5, pady=10, sticky='ew')

# Start the Tkinter main loop
root.mainloop()
