'''
Create a program that reads in the following list of names:
Ling, Mai
Johnson, Jim
Zarnecki, Sabrina
Jones, Chris
Jones, Aaron
Swift, Geoffrey
Xiong, Fong

Read this program and sort the list alphabetically. 
Then print the sorted list to a file that looks like the following example output.

Example Output
Total of 7 names
-----------------
Ling, Mai
Johnson, Jim
Jones, Aaron
Jones, Chris
Swift, Geoffrey
Xiong, Fong
Zarnecki, Sabrina
'''

names = [
    "Ling, Mai",
    "Swift, Geoffrey",
    "Johnson, Jim",
    "Jones, Aaron",
    "Zarnecki, Sabrina",
    "Jones, Chris",
    "Xiong, Fong"
    ]
sorted_names = sorted(names)
print(sorted_names)

with open("name_sorter.txt", "w") as file:
    file.write(f"Total of {len(sorted_names)} names.\n")
    file.write(10 * "*" + "\n")
    for name in sorted_names:
        file.write(name + "\n")