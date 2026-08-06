'''
Create a program that reads in a file and counts the frequency of words in the file.
Then construct a histogram displaying the words and the frequency, and display the histogram to the screen.

Example Output
Given the text file words.txt with this content:

badger badger badger badger mushroom mushroom
snake badger badger badger

The program would produce the following output:
badger: *******
mushroom: **
snake: *
'''

#first read the file

with open("ex46_word_freq_finder.txt", "r") as file:
    file_cont = file.read()
    print(file_cont)

# split the content and save them in a list
split_count = file_cont.split()

#create an empty dictionary to count the each word in a sentence
word_count = {}

for word in split_count:
    if word in word_count:
        word_count[word]  += 1
    else:
        word_count[word] = 1

# unpack the dictionary and split each word with the value
for word, count in word_count.items():
    print(f"{word:<10} {count}")

# print(word_count)