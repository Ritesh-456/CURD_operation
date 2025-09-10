from pathlib import Path
import os

def show_directory_files():
    path = Path('')
    path = list(path.rglob('*'))
    for i, items in enumerate(path):
        print(f"{i+1}. {items}")

def create_file():
    try:
        show_directory_files()
        user = input("Enter the file name with extension (e.g., myfile.txt): ")
        p = Path(user)
        if not p.exists():
            with open(p, 'w') as file:
                data = input(f"Write something inside {p}: \n")
                file.write(data)
            print("FILE CREATED")
        else:
            print("File already exists.")
    except Exception as err:
        print(f"Error: {err}")

def read_file():
    try:
        show_directory_files()
        user = input("Enter the file name to read (e.g., myfile.txt): ")
        p = Path(user)
        if p.exists() and p.is_file():
            with open(p, 'r') as file:
                print("\n--- File Content ---")
                print(file.read())
                print("--------------------")
            print("READING COMPLETE")
        else:
            print("File not found.")
    except Exception as err:
        print(f"Error: {err}")

def update_file():
    try:
        show_directory_files()
        user = input("Enter the file name to update (e.g., myfile.txt): ")
        p = Path(user)
        if p.exists() and p.is_file():
            changes = int(input("Choose an option:\n"
                                "1. Rename file\n"
                                "2. Overwrite file\n"
                                "3. Append content\n"
                                "Enter (1/2/3): "))

            if changes == 1:
                new_name = input(f"Enter a new name for {p.name}: ")
                p.rename(p.parent / new_name)
                print("FILE RENAMED SUCCESSFULLY")

            elif changes == 2:
                with open(p, 'w') as file:
                    data = input("Write new content (overwrite):\n")
                    file.write(data)
                print("OVERWRITE SUCCESSFULLY")

            elif changes == 3:
                with open(p, 'a') as file:
                    data = input("Write content to append:\n")
                    file.write("\n" + data)
                print("APPENDED SUCCESSFULLY")

        else:
            print("File not found.")
    except Exception as err:
        print(f"Error: {err}")

def delete_file():
    try:
        show_directory_files()
        user = input("Enter the file name to delete (e.g., myfile.txt): ")
        p = Path(user)
        if p.exists() and p.is_file():
            os.remove(p)
            print("FILE DELETED SUCCESSFULLY")
        else:
            print("File not found.")
    except Exception as err:
        print(f"Error: {err}")


user = int(input("Choose an option:\n"
                 "1. Create a file\n"
                 "2. Read a file\n"
                 "3. Update a file\n"
                 "4. Delete a file\n"
                 "Enter (1/2/3/4): "))

try:
    if user == 1:
        create_file()
    elif user == 2:
        read_file()
    elif user == 3:
        update_file()
    elif user == 4:
        delete_file()
    else:
        print("Invalid choice.")
except Exception as err:
    print(f"Some Error Occurred: {err}")