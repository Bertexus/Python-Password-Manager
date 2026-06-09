import sys
from pathlib import Path
import json

# This function will either encrypt or decrypt a password using rot3 ceasar encryption
def rot3(pw, shift):
    encrypted_pw = ""
    for char in pw:
        if char.isupper():
            encrypted_pw += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            encrypted_pw += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_pw += char
    
    return encrypted_pw

# File path of the file containing all the credentials
file_path = Path("Credentials.txt")

# This function will store credentials and encrypt the password by calling the rot3 function
def encrypt(username, password, shift):
    data = {
        "Username": username,
        "Password": rot3(password, shift)
    }

    mode = "a" if file_path.is_file() else "w"

    with open(file_path, mode) as file:
        file.write(json.dumps(data) + "\n")
        print("Data Stored Successfully \n")
    
# This function will decrypt the password by calling the rot3 function and display all credentials
def decrypt():
    print("--------------------------------------- All User Credentials ---------------------------------------")
    try:
        with open("Credentials.txt", "r") as file:
            for conts in file:
                data = json.loads(conts)
                print(f"Username: {data["Username"]}")
                print(f"Password: {rot3(data["Password"], -3)}" )
                print("-" * 20)
    except FileNotFoundError:
        print("The file does not exist. Please check the file path.")

# This function will display all choices available for the user
def menu():
    while True:
        print("Please select an option: \n")
        print("[1] Add Credentials (Username and Password)")
        print("[2] Read All Credentials")
        print("[3] Terminate Program")

        # This will read the user input and store it in a variable
        choice = input("> ")

        # User input will be matched according to the switch cases
        match choice:
            # Case 1 will ask for username and input and will call encrypt function to store data
            case "1":
                username = input("Please enter Username: ")
                password = input("Please enter Password: ")
                encrypt(username, password, 3)
            
            # Case 2 will call decrypt function to decrypt password and display data
            case "2":
                decrypt()

            # Case 3 will terminate the program immediately
            case "3":
                print("Program Terminated")
                sys.exit(0)

            # This will display if the user enters an input different from the choices
            case _:
                print("Unknown Input. Please try again.\n")


print("-------------------------------------------- Password Manager --------------------------------------------\n")
print("This is a program for storing and displaying user credentials. Please select from the choices displayed below. Any other inputs will result in error.\n")

# Starts the program
menu()
