'''
Given an input file, read the file and look for all occurrences of the word utilize.
Replace each occurrence with use. Write the modified file to a new file.

Example Output
Given the input file of One should never utilize the word "utilize" in writing. Use "use" instead.

The program should generate One should never use the word "use" in writing. Use "use" instead.
'''


with open("ex45_word_finder_input_file.txt", "r") as file:
    file_txt = file.read()

# count the occurences
count_lower = file_txt.count("utilize")
count_upper = file_txt.count("Utilize")
total_count = count_upper + count_lower

#replace the utilize occurences with use
new_sentence = file_txt.replace("utilize", "use")
new_sentence = new_sentence.replace("Utilize", "Use")

print(new_sentence)
# count the total occurences of utilize 
print(f"Total count: {total_count}")

with open("ex45_word_finder_output_file.txt", "a") as file:
    file.write(new_sentence + "\n")