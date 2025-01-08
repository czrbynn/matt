import tkinter as tk

# Function to disable the close button (X)
def disable_event():
    pass

# Function to close the popup after 10 seconds
def close_after_delay():
    root.destroy()  # This will close the window

# Create a root window
root = tk.Tk()
root.title("")

# Set the window size
root.geometry("300x150")

# Disable the close button (X)
root.protocol("WM_DELETE_WINDOW", disable_event)

# Create a label
label = tk.Label(root, text="BOOM SHACKA LACKA", font=("Helvetica", 14))
label.pack(pady=50)



# Show the popup window
root.mainloop()
