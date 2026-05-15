# Level 1: Basic File Reading and Writing
# This script reads from one file and writes a simple message to another.

input_file = "level1_basic.txt"
output_file = "level1_output.txt"

print(f"--- Reading from {input_file} ---")
# Using 'with' statement ensures the file is properly closed after its suite finishes
with open(input_file, 'r') as file:
    content = file.read()
    print(content)

print(f"\n--- Writing to {output_file} ---")
with open(output_file, 'a') as file:
    file.write("\nThis is a new file created by the Level 1 script.\n")
    file.write("File handling in Python is easy!")
    
print("Done!")
