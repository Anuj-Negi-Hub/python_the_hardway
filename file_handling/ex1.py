# Exercise 1 — File Not Found Handling
# Problem

# Read a file safely.

# If file does not exist, show proper error message.

input_file = "level1_basic.txt"

try:
    with open(input_file, "r") as file:
        content = file.read()
        print(content)

except IOError as e:
    print(f"The file cannot be opened: {e}.")
except Exception as e:
    print(f"An unexpected error occured: {e}")
