import tkinter as tk
from tkinter import filedialog, messagebox
import os
import datetime

# Create the main window
root = tk.Tk()
root.title("Renamerino")
root.geometry("400x200")  # Optional, sets initial window size

# Label to display the selected folder path
lbl_path = tk.Label(root, text="")
lbl_path.pack(pady=5)

def select_folder():
    selected_folder = filedialog.askdirectory()
    if selected_folder:
        lbl_path.config(text=selected_folder)

# Button to open a dialog for selecting the folder
btn_select_folder = tk.Button(root, text="Select Folder", command=select_folder)
btn_select_folder.pack(pady=5)

# Variables and widgets for user inputs
prefix_var = tk.StringVar()
tk.Label(root, text="Prefix:").pack()
entry_prefix = tk.Entry(root, textvariable=prefix_var)
entry_prefix.pack(pady=5)

include_date_var = tk.BooleanVar(value=False)
chk_date = tk.Checkbutton(root, text="Include current date in file name", variable=include_date_var)
chk_date.pack(pady=5)

def rename_files():
    folder_path = lbl_path.cget("text")
    if not folder_path:
        messagebox.showerror("Error", "No folder selected!")
        return

    prefix = prefix_var.get()
    include_date = include_date_var.get()

    # Dictionary to store the counter for each file extension
    counters_by_extension = {}

    # Get the list of files in the selected folder
    files = os.listdir(folder_path)

    for file_name in files:
        old_path = os.path.join(folder_path, file_name)

        # Only process if it's a file (skip subfolders)
        if os.path.isfile(old_path):
            # Extract the extension
            if "." in file_name:
                extension = "." + file_name.split(".")[-1]
            else:
                extension = ""  # File without an extension

            # Initialize the counter for this extension if it doesn't exist yet
            if extension not in counters_by_extension:
                counters_by_extension[extension] = 0

            # Increment the counter for the current extension
            counters_by_extension[extension] += 1
            counter = counters_by_extension[extension]

            # Build the new file name
            new_name = prefix
            if include_date:
                date_str = datetime.datetime.now().strftime("%Y%m%d")
                new_name += f"_{date_str}"

            new_name += f"_{counter}"  # e.g., prefix_20250321_1

            new_full_name = new_name + extension
            new_path = os.path.join(folder_path, new_full_name)

            if os.path.exists(new_path):
                messagebox.showwarning(
                    "Warning",
                    f"File '{new_full_name}' already exists. Skipping rename."
                )
            else:
                os.rename(old_path, new_path)

    messagebox.showinfo("Operation Completed", "Renaming completed successfully!")

# Button that triggers the renaming function
btn_rename = tk.Button(root, text="Rename Files", command=rename_files)
btn_rename.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
