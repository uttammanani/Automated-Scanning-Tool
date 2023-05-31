import os
import sys
import tkinter as tk
from tkinter import messagebox, filedialog

# Define the commands for different categories
commands = {
    "Network Command": [
        "ip address",
        "ip monitor",
        "traceroute google.com",
        "tracepath google.com",
        "ping google.com",
        "ss -at",
        "ss -au",
        "ss -s",
        "dig egrasps.in",
        "host egrasps.in",
        "whois egrasps.in",
        "ifplugstatus",
        "nmap egrasps.in"
    ],
    "Information Gathering Command": [
        "uname -a",
    ],
    "System Command": [
        "ps -aux",
    ]
}

# Function to execute the selected commands
def execute_commands():
    folder_name = folder_entry.get()
    if not folder_name:
        messagebox.showwarning("Folder Name Missing", "Please enter a folder name.")
        return

    # Create the folder in the current directory
    folder_path = os.path.join(os.getcwd(), folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Create sub-folders for each command category
    for category, cmds in commands.items():
        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)
        for cmd in cmds:
            output_file = os.path.join(category_folder, f"{cmd}.txt")
            command = cmd  # Replace with the actual command to execute
            if sys.platform.startswith("win"):
                os.system(f"cmd /c {command} > {output_file}")
            elif sys.platform.startswith("linux"):
                os.system(f"{command} > {output_file}")
            elif sys.platform.startswith("darwin"):
                os.system(f"{command} > {output_file}")
            else:
                messagebox.showwarning("Unsupported OS", "This program does not support your operating system.")
                return

    output_path_entry.delete(0, tk.END)
    output_path_entry.insert(tk.END, folder_path)

# Create the main window
window = tk.Tk()
window.title("Command Executor")

# Folder Name input, textbox, and button in the same line
input_frame = tk.Frame(window)
input_frame.pack(anchor="w")

folder_label = tk.Label(input_frame, text="Folder Name:")
folder_label.pack(side="left")
folder_entry = tk.Entry(input_frame)
folder_entry.pack(side="left")

execute_button = tk.Button(input_frame, text="Execute", command=execute_commands)
execute_button.pack(side="left")

# Command Categories Checkboxes
categories_frame = tk.Frame(window)
categories_frame.pack(anchor="w")

categories_label = tk.Label(categories_frame, text="Command Categories:")
categories_label.pack(anchor="w")
checkboxes = []
for category in commands:
    var = tk.IntVar()
    checkbox = tk.Checkbutton(categories_frame, text=category, variable=var)
    checkbox.pack(anchor="w")
    checkboxes.append(var)

# Output Folder textbox and label at the end
output_path_frame = tk.Frame(window)
output_path_frame.pack(anchor="w")

output_path_label = tk.Label(output_path_frame, text="Output Folder:")
output_path_label.pack(side="left")
output_path_entry = tk.Entry(output_path_frame)
output_path_entry.pack(side="left")

window.mainloop()