import tkinter as tk

# Create a main window
root = tk.Tk()
root.title("Custom Window UI")

# Configure the window size
root.geometry("300x200")

# Create a custom frame for the window content
custom_frame = tk.Frame(root, bg="grey")
custom_frame.pack(fill=tk.BOTH, expand=True)

# Create a title label
title_label = tk.Label(custom_frame, text="Custom Window", font=("Arial", 16), bg="blue", fg="black")
title_label.pack(fill=tk.X)

# Create a content label
content_label = tk.Label(custom_frame, text="This is a custom window UI.", padx=10, pady=10)
content_label.pack(fill=tk.BOTH, expand=True)

# Create buttons (e.g., Minimize and Close)
minimize_button = tk.Button(custom_frame, text="-", font=("Arial", 12), command=root.iconify)
minimize_button.pack(side=tk.LEFT)

close_button = tk.Button(custom_frame, text="x", font=("Arial", 12), command=root.destroy)
close_button.pack(side=tk.RIGHT)

# Start the GUI main loop
root.mainloop()