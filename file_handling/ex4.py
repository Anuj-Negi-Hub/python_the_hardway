# Exercise 4 — Count Total Lines

# Goal
# Count number of lines in a file.

num_line = []

with open("ex3.txt", "r") as file:
    for line in file:
        num_line += 1
        print(num_line)


