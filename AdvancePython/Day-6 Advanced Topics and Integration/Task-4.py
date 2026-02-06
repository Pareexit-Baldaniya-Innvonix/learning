# Task 4: 'with' statement in file handling
import os

filename = "AdvancePython/Day-6 Advanced Topics and Integration/sample.txt"

if os.path.exists(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())
    except Exception as e:
        print(f"An error occured while reading file: {e}")
else:
    print(f"Error: The file '{filename}' was not found.")
