# Exercise 5 — Count Words in File

# Goal
# Count total words.
count_word = []
with open("ex3.txt", "r") as file:
    content = file.read()
word = content.split()
print(len(word))
print(word)