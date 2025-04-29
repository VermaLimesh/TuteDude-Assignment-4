# Task 1: Read a File and Handle Errors

def read_and_print_file(filename):
    try:
        with open(filename, "r") as file:
            print("Reading file Content:")
            line_number = 1
            for line in file:
                print(f"line {line_number}: {line.strip()}")
                line_number += 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Calling the function

read_and_print_file("sample.txt")