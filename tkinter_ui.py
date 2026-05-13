# tkinter_app.py

from tkinter import *
from tkinter import messagebox
from pathlib import Path
import os
import shutil


root = Tk()
root.title("CRUD File Handling System")
root.geometry("500x500")


# FUNCTIONS

def create_file():
    file_name = entry1.get()
    content = text.get("1.0", END)

    p = Path(file_name)

    if p.exists():
        messagebox.showerror("Error", "FILE ALREADY EXISTS")

    else:
        with open(file_name, 'w') as file:
            file.write(content)

        messagebox.showinfo("Success", "FILE CREATED")


def read_file():
    file_name = entry1.get()

    p = Path(file_name)

    if p.exists():

        with open(file_name, 'r') as file:
            data = file.read()

        text.delete("1.0", END)
        text.insert(END, data)

    else:
        messagebox.showerror("Error", "FILE NOT FOUND")


def update_file():
    file_name = entry1.get()
    content = text.get("1.0", END)

    p = Path(file_name)

    if p.exists():

        with open(file_name, 'w') as file:
            file.write(content)

        messagebox.showinfo("Success", "FILE UPDATED")

    else:
        messagebox.showerror("Error", "FILE NOT FOUND")


def delete_file():
    file_name = entry1.get()

    p = Path(file_name)

    if p.exists():
        os.remove(p)
        messagebox.showinfo("Success", "FILE DELETED")

    else:
        messagebox.showerror("Error", "FILE NOT FOUND")


def create_folder():
    folder_name = entry1.get()

    p = Path(folder_name)

    if p.exists():
        messagebox.showerror("Error", "FOLDER ALREADY EXISTS")

    else:
        p.mkdir()
        messagebox.showinfo("Success", "FOLDER CREATED")


def delete_folder():
    folder_name = entry1.get()

    p = Path(folder_name)

    if p.exists():
        shutil.rmtree(p)
        messagebox.showinfo("Success", "FOLDER DELETED")

    else:
        messagebox.showerror("Error", "FOLDER NOT FOUND")


# UI

Label(root, text="Enter File/Folder Name", font=("Arial", 14)).pack(pady=10)

entry1 = Entry(root, width=40, font=("Arial", 12))
entry1.pack(pady=10)

Label(root, text="Content", font=("Arial", 14)).pack()

text = Text(root, height=10, width=50)
text.pack(pady=10)


Button(root, text="Create File", width=20, command=create_file).pack(pady=5)

Button(root, text="Read File", width=20, command=read_file).pack(pady=5)

Button(root, text="Update File", width=20, command=update_file).pack(pady=5)

Button(root, text="Delete File", width=20, command=delete_file).pack(pady=5)

Button(root, text="Create Folder", width=20, command=create_folder).pack(pady=5)

Button(root, text="Delete Folder", width=20, command=delete_folder).pack(pady=5)


root.mainloop()