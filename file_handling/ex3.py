# Exercise 3 — Append Data to File

# Goal
# Add new content without deleting old content.

try:
    with open("ex2.txt", "r") as file:
        content = file.read()
        print("The data is successfully copied.")

    with open("ex3.txt", "a") as file:
        file.write(f"\n{content}")
        print("The data is ssuccessully added.")

except FileNotFoundError as e:
    print(f"The file is missing, {e}")

except IOError as e:
    print(f"The file cannot be opened, {e}")