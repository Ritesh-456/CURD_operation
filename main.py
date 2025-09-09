from pathlib import Path
import os

def show_directory_files():
    pass

def create_file():
    
    try:
        
        pass

    except Exception as err:
        print(f"Some error occurs as {err}")

def read_file():
    
    try:
        
        pass

    except Exception as err:
        print(f"Some error occurs as {err}")

def update_file():
    
    try:
        
        pass

    except Exception as err:
        print(f"Some error occurs as {err}")

def delete_file():
    
    try:
        
        pass

    except Exception as err:
        print(f"Some error occurs as {err}")


user = int(input("Enter 1 for creating a file:\n" \
"enter 2 for reading a file:\n" \
"enter 3 for updating a file:\n" \
"enter 4 for deleting a file:\n" \
"Press ( 1/ 2/ 3/ 4 ): "))

try:

    if user == 1:
        create_file()
    elif user == 2:
        read_file()
    elif user == 3:
        update_file()
    elif user == 4:
        delete_file()

except Exception as err:
    print(f"Some Error Happens as {err}")