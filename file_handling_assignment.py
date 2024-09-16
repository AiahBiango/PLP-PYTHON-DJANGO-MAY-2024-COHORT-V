# File Creation
with open("my_file.txt", "w") as file:
    file.write("Hello, this is line 1.\n")
    file.write("This is line 2 with a number: 12345\n")
    file.write("And this is line 3 with another number: 67890\n")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("File Contents:\n", content)
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access this file.")
finally:
    print("File operation completed.")

# File Appending
with open("my_file.txt", "a") as file:
    file.write("Appending line 4.\n")
    file.write("Appending line 5 with a number: 54321\n")
    file.write("Appending line 6 with another number: 98765\n")

# File Reading and Display again to show appended content
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("Updated File Contents:\n", content)
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access this file.")
finally:
    print("File operation completed.")
