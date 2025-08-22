# //current task's we have

import os

# Define the file path
file_path = "C:/Users/vishn/OneDrive/Desktop/PYTHON.py/todo.txt"  # Replace with your file path

# Check if the file exists
if os.path.exists(file_path):
    try:
        # Open the file in read mode and print its contents
        with open(file_path, "r") as file:
            content = file.read()
            if content.strip():  # Check if the file is not empty
                print("Current contents of the file:")
                print(content)
            else:
                print("The file is empty.")
    except Exception as e:
        print(f"Error reading the file: {e}")
else:
    print(f"The file does not exist: {file_path}")








# //clear file
# import os

# # Define the file path
# file_path = "C:/Users/vishn/OneDrive/Desktop/PYTHON.py/todo.txt"  # Replace with your file path

# # Check if the file exists
# if os.path.exists(file_path):
#     try:
#         # Open the file in write mode to clear its contents
#         with open(file_path, "w") as file:
#             pass  # Opening in write mode clears the file
#         print(f"The file has been cleared: {file_path}")
#     except Exception as e:
#         print(f"Error clearing the file: {e}")
# else:
#     print(f"The file does not exist: {file_path}")