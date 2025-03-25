import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import messagebox, Listbox, END
from secure_delete import secure_delete
from secure_folder import secure_delete_folder

def process_items(file_list):
    """Delete selected files/folders securely."""
    for item in file_list.get(0, END):
        item = item.strip("{}")  # Fix path format for dropped files
        if os.path.isfile(item):
            secure_delete(item)
        elif os.path.isdir(item):
            secure_delete_folder(item)
    
    file_list.delete(0, END)  # Clear UI list
    messagebox.showinfo("Done", "Files and folders securely deleted!")

def drop(event, file_list):
    """Handle drag-and-drop files."""
    files = event.data.split()
    for file in files:
        file_list.insert(END, file.strip("{}"))  # Fix TkinterDnD path format

def run_gui():
    """Creates and runs the UI."""
    root = TkinterDnD.Tk()
    root.title("Secure File Wiper")
    root.geometry("500x400")

    tk.Label(root, text="Drag & Drop Files or Folders Below:", font=("Arial", 12)).pack(pady=10)
    file_list = Listbox(root, width=60, height=10, selectmode=tk.MULTIPLE)
    file_list.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    file_list.drop_target_register(DND_FILES)
    file_list.dnd_bind("<<Drop>>", lambda event: drop(event, file_list))

    delete_button = tk.Button(root, text="Secure Delete", command=lambda: process_items(file_list), fg="white", bg="red", font=("Arial", 12))
    delete_button.pack(pady=20)

    root.mainloop()