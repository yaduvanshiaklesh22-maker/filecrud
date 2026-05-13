# app.py

import streamlit as st
from pathlib import Path
import os
import shutil

st.title("CRUD File Handling System")


# READ FILES & FOLDERS
def readfileandfolder():
    p = Path('.')
    items = list(p.rglob('*'))
    return items


# CREATE FILE
def create_file(file_name, content):
    p = Path(file_name)

    if p.exists():
        return "FILE ALREADY EXISTS"

    with open(file_name, 'w') as file:
        file.write(content)

    return "FILE CREATED SUCCESSFULLY"


# READ FILE
def read_file(file_name):
    p = Path(file_name)

    if p.exists():
        with open(file_name, 'r') as file:
            return file.read()

    return "FILE NOT FOUND"


# UPDATE FILE
def update_file(file_name, content, mode):
    p = Path(file_name)

    if p.exists():

        if mode == "Overwrite":
            with open(file_name, 'w') as file:
                file.write(content)

        elif mode == "Append":
            with open(file_name, 'a') as file:
                file.write(content)

        return "FILE UPDATED"

    return "FILE NOT FOUND"


# DELETE FILE
def delete_file(file_name):
    p = Path(file_name)

    if p.exists():
        os.remove(p)
        return "FILE DELETED"

    return "FILE NOT FOUND"


# RENAME FILE
def rename_file(old_name, new_name):
    p = Path(old_name)

    if p.exists():
        p.rename(new_name)
        return "FILE RENAMED"

    return "FILE NOT FOUND"


# CREATE FOLDER
def create_folder(folder_name):
    p = Path(folder_name)

    if p.exists():
        return "FOLDER ALREADY EXISTS"

    p.mkdir()
    return "FOLDER CREATED"


# DELETE FOLDER
def delete_folder(folder_name):
    p = Path(folder_name)

    if p.exists():
        shutil.rmtree(p)
        return "FOLDER DELETED"

    return "FOLDER NOT FOUND"


# SIDEBAR MENU
menu = st.sidebar.selectbox(
    "Choose Operation",
    [
        "View Files/Folders",
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder"
    ]
)


# VIEW
if menu == "View Files/Folders":
    items = readfileandfolder()

    for item in items:
        st.write(item)


# CREATE FILE
elif menu == "Create File":
    file_name = st.text_input("Enter File Name")
    content = st.text_area("Enter File Content")

    if st.button("Create File"):
        st.success(create_file(file_name, content))


# READ FILE
elif menu == "Read File":
    file_name = st.text_input("Enter File Name")

    if st.button("Read File"):
        data = read_file(file_name)
        st.text(data)


# UPDATE FILE
elif menu == "Update File":
    file_name = st.text_input("Enter File Name")
    content = st.text_area("Enter Content")
    mode = st.radio("Select Mode", ["Overwrite", "Append"])

    if st.button("Update File"):
        st.success(update_file(file_name, content, mode))


# DELETE FILE
elif menu == "Delete File":
    file_name = st.text_input("Enter File Name")

    if st.button("Delete File"):
        st.success(delete_file(file_name))


# RENAME FILE
elif menu == "Rename File":
    old_name = st.text_input("Enter Old File Name")
    new_name = st.text_input("Enter New File Name")

    if st.button("Rename File"):
        st.success(rename_file(old_name, new_name))


# CREATE FOLDER
elif menu == "Create Folder":
    folder_name = st.text_input("Enter Folder Name")

    if st.button("Create Folder"):
        st.success(create_folder(folder_name))


# DELETE FOLDER
elif menu == "Delete Folder":
    folder_name = st.text_input("Enter Folder Name")

    if st.button("Delete Folder"):
        st.success(delete_folder(folder_name))